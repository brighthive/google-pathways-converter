import json

from converter import work_based_program_converter
from expects import equal, expect
from tests.conftest import pprint_diff


def test_work_based_program_converter_all(input_kwargs, offers, training_salary, salary_upon_completion, required_fields_as_jsonld):
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
        "endDate": input_kwargs['end_date'],
        "startDate": input_kwargs['start_date'],
        "maximumEnrollment": input_kwargs['maximum_enrollment'],
        "occupationalCredentialAwarded": input_kwargs['occupational_credential_awarded'],
        "timeOfDay": input_kwargs['time_of_day'],
        "timeToComplete": input_kwargs['time_to_complete'],
        "offers": offers,
        "trainingSalary": training_salary,
        "salaryUponCompletion": salary_upon_completion
    }

    required_fields_as_jsonld.update(recommended_fields)

    output = work_based_program_converter(**input_kwargs)

    pprint_diff(required_fields_as_jsonld, output)

    json_expected_output = json.dumps(required_fields_as_jsonld, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    print(json.dumps(output, indent=4, sort_keys=True))
    expect(json_output).to(equal(json_expected_output))


def test_work_based_program_converter_required(input_kwargs, required_fields_as_jsonld):
    kwargs = {
        "program_description": input_kwargs['program_description'],
        "program_name": input_kwargs['program_name'],
        "program_url": input_kwargs['program_url'],
        "provider_name": input_kwargs['provider_name'],
        "provider_url": input_kwargs['provider_url'],
        "provider_telephone": input_kwargs['provider_telephone'],
        "provider_address": input_kwargs['provider_address']
    }

    output = work_based_program_converter(**kwargs)

    pprint_diff(required_fields_as_jsonld, output)

    json_expected_output = json.dumps(required_fields_as_jsonld, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)
    expect(json_output).to(equal(json_expected_output))
