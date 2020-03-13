import json

import pytest
from expects import equal, expect

from converter.helper import (add_basic_keywords, add_data_keywords,
                              add_header, add_identifier_data, add_offers_data,
                              add_prerequisites_data, add_provider_data,
                              add_salary_upon_completion_data,
                              add_training_salary_data)
from tests.conftest import pprint_diff


def test_add_basic_keywords(work_based_input_kwargs):

    kwarg_to_schema_key_mapper = {
        "program_description": "description",
        "program_name": "name",
        "program_url": "url"
    }

    expected_output = {
        "description": work_based_input_kwargs['program_description'],
        "name": work_based_input_kwargs['program_name'],
        "url": work_based_input_kwargs['program_url'],
        "endDate": work_based_input_kwargs['end_date'],
        "startDate": work_based_input_kwargs['start_date'],
        "maximumEnrollment": work_based_input_kwargs['maximum_enrollment'],
        "occupationalCredentialAwarded": work_based_input_kwargs['occupational_credential_awarded'],
        "timeOfDay": work_based_input_kwargs['time_of_day'],
        "timeToComplete": work_based_input_kwargs['time_to_complete']
    }

    output = add_basic_keywords({}, work_based_input_kwargs,  kwarg_to_schema_key_mapper)

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


@pytest.mark.xfail
def test_add_data_keywords(work_based_input_kwargs, required_fields_as_jsonld, offers, training_salary, salary_upon_completion):
    # This test should not be an integration test?
    data_keywords_mapper = {
        "program_prerequisites": lambda output, value: add_prerequisites_data(output, kwargs['program_prerequisites']),
        "offers_price": lambda output, kwargs: add_offers_data(output, kwargs['offers_price']),
        "training_salary": lambda output, kwargs: add_training_salary_data(output, kwargs['training_salary']),
        "salary_upon_completion": lambda output, kwargs: add_salary_upon_completion_data(output, kwargs['salary_upon_completion']),
        "all": [
            lambda output, kwargs: add_header(output, "WorkBasedProgram"),
            lambda output, kwargs: add_provider_data(output, kwargs)
        ]
    }

    recommend_fields = {
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
        "offers": offers,
        "trainingSalary": training_salary,
        "salaryUponCompletion": salary_upon_completion
    }
    required_fields_as_jsonld.update(recommend_fields)
    expected_output = required_fields_as_jsonld

    output = add_data_keywords({}, work_based_input_kwargs, data_keywords_mapper)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


@pytest.mark.xfail
def test_add_header():
    pass


def test_add_identifier_data(educational_input_kwargs):
    cip = educational_input_kwargs['identifier_cip']
    program_id = educational_input_kwargs['identifier_program_id']

    output = add_identifier_data({}, cip=cip, program_id=program_id)

    expected_output = {
        "identifier": [
            {
                "@type": "PropertyValue",
                "propertyID": "CIP2010",
                "value": cip
            },
            {
                "@type": "PropertyValue",
                "propertyID": "ProgramID",
                "value": program_id
            }
        ]
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))



