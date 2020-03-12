import json

from converter.helper import (add_offers_data, add_basic_keywords, add_prerequisites_data,
                              add_provider_data,
                              add_salary_upon_completion_data,
                              add_training_salary_data)
from expects import equal, expect
from tests.conftest import pprint_diff


def test_add_basic_keywords(program_provider_address_data, offers, training_salary, salary_upon_completion):
    input_kwargs = {
        "program_description": "A description of a Goodwill program",
        "program_name": "Goodwill Program",
        "program_url": "goodwill.org",
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
        "end_date": "2020-12-01",
        "start_date": "2020-04-01",
        "maximum_enrollment": "50",
        "occupationalCredentialAwarded": "Associate Degree",
        "time_of_day": "Evening",
        "time_to_complete": "P6M",
        "offers_price": offers['priceSpecification']['price'],
        "training_salary": training_salary['median'],
        "salary_upon_completion": salary_upon_completion['median']
    }

    expected_output = {
        "description": "A description of a Goodwill program",
        "name": "Goodwill Program",
        "url": "goodwill.org",
        "endDate": "2020-12-01",
        "startDate": "2020-04-01",
        "maximumEnrollment": "50",
        "occupationalCredentialAwarded": "Associate Degree",
        "timeOfDay": "Evening",
        "timeToComplete": "P6M",
    }

    output = add_basic_keywords({}, input_kwargs)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))



def test_add_provider_data(program_provider_address_data):
    kwargs = {
        "provider_name": "provider name",
        "provider_address": program_provider_address_data
    }

    expected_output = {
        "provider": {
            "@type": "EducationalOrganization",
            "name": "provider name",
            "address": [
                {
                    "@type": "PostalAddress", 
                    "streetAddress": "1940 East Silverlake Rd",
                    "addressLocality": "Tucson",
                    "addressRegion": "AZ",
                    "postalCode": "85713"
                }
            ]
        },
    }

    output = add_provider_data({}, kwargs)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisites_data():
    kwargs = {}

    expected_output = {
        "programPrerequisites": []
    }

    output = add_prerequisites_data({}, kwargs)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_offers_data(offers):
    offers_price = offers['priceSpecification']['price']
    expected_output = {
        "offers": offers
    }

    output = add_offers_data({}, offers_price)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_training_salary_data(training_salary):
    median = training_salary['median']
    expected_output = {
        "trainingSalary": training_salary
    }

    output = add_training_salary_data({}, median)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_salary_upon_completion_data(salary_upon_completion):
    median = salary_upon_completion['median']
    expected_output = {
        "salaryUponCompletion": salary_upon_completion
    }

    output = add_salary_upon_completion_data({}, median)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))
