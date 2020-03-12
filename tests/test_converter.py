import json

from converter import work_based_program_converter
from expects import equal, expect
from tests.conftest import pprint_diff


def test_work_based_program_converter_all(program_provider_address_data, offers, training_salary, salary_upon_completion, required_fields_as_jsonld):
    kwargs = {
        "program_description": "desc",
        "program_name": "name",
        "program_url": "url",
        "provider_name": "provider name",
        "provider_url": "provider url",
        "provider_telephone": "telephone",
        "provider_address": program_provider_address_data,
        "program_prerequisites": {
            "credential_category": "HighSchool",
            "eligible_groups": "Youth",
            "max_income_eligibility": "20000",
            "other_program_prerequisites": "other"
        },
        "end_date": "2020",
        "start_date": "2019",
        "maximumEnrollment": "maximumEnrollment",
        "occupationalCredentialAwarded": "occupationalCredentialAwarded",
        "timeOfDay": "timeOfDay",
        "timeToComplete": "timeToComplete",
        "offers_price": offers['priceSpecification']['price'],
        "training_salary": training_salary['median'],
        "salary_upon_completion": salary_upon_completion['median']
    }

    recommended_fields = {
        "programPrerequisites": [
            {
                "@type": "EducationalOccupationalCredential", 
                "credentialCategory": "HighSchool"
            },
            {
                "@type": "Text",
                "eligibleGroups": "Youth"
            },
            {
                "@type": "Text",
                "maxIncomeEligibility": "20000"
            },
            {
                "@type": "Text",
                "otherProgramPrerequisites": "other"
            }
        ],
        "endDate": "2020",
        "startDate": "2019",
        "maximumEnrollment": "maximumEnrollment",
        "occupationalCredentialAwarded": "occupationalCredentialAwarded",
        "timeOfDay": "timeOfDay",
        "timeToComplete": "timeToComplete",
        "offers": offers,
        "trainingSalary": training_salary,
        "salaryUponCompletion": salary_upon_completion
    }

    required_fields_as_jsonld.update(recommended_fields)

    output = work_based_program_converter(**kwargs)

    pprint_diff(required_fields_as_jsonld, output)

    json_expected_output = json.dumps(required_fields_as_jsonld, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)
    expect(json_output).to(equal(json_expected_output))


def test_work_based_program_converter_required(program_provider_address_data, required_fields_as_jsonld):
    kwargs = {
        "program_description": "desc",
        "program_name": "name",
        "program_url": "url",
        "provider_name": "provider name",
        "provider_url": "provider url",
        "provider_telephone": "telephone",
        "provider_address": program_provider_address_data
    }

    output = work_based_program_converter(**kwargs)

    pprint_diff(required_fields_as_jsonld, output)

    json_expected_output = json.dumps(required_fields_as_jsonld, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)
    expect(json_output).to(equal(json_expected_output))
