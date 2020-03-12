import json

from converter.helper import (add_offers_data, add_basic_keywords, add_prerequisites_data,
                              add_provider_data,
                              add_salary_upon_completion_data,
                              add_training_salary_data,
                              add_data_keywords,
                              add_header)
from expects import equal, expect
from tests.conftest import pprint_diff
import pytest


def test_add_basic_keywords(input_kwargs):

    kwarg_to_schema_key_mapper = {
        "program_description": "description",
        "program_name": "name",
        "program_url": "url"
    }

    basic_keywords = [
        "description",
        "name",
        "url",
        "endDate",  # Dates should use ISO-8601 format – do we need to validate?
        "startDate",
        "maximumEnrollment",
        "occupationalCredentialAwarded",
        "timeOfDay",
        "timeToComplete",  # Again, should be ISO-8601 format (for durations) – should this library validate for this?
    ]
    expected_output = {
        "description": input_kwargs['program_description'],
        "name": input_kwargs['program_name'],
        "url": input_kwargs['program_url'],
        "endDate": input_kwargs['end_date'],
        "startDate": input_kwargs['start_date'],
        "maximumEnrollment": input_kwargs['maximum_enrollment'],
        "occupationalCredentialAwarded": input_kwargs['occupational_credential_awarded'],
        "timeOfDay": input_kwargs['time_of_day'],
        "timeToComplete": input_kwargs['time_to_complete']
    }

    output = add_basic_keywords({}, input_kwargs, basic_keywords, kwarg_to_schema_key_mapper)

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


def test_add_data_keywords(input_kwargs):
    data_keywords_mapper = {
        "program_prerequisites": lambda output, kwargs: add_prerequisites_data(output, kwargs['program_prerequisites']),
        "offers_price": lambda output, kwargs: add_offers_data(output, kwargs['offers_price']),
        "training_salary": lambda output, kwargs: add_training_salary_data(output, kwargs['training_salary']),
        "salary_upon_completion": lambda output, kwargs: add_salary_upon_completion_data(output, kwargs['salary_upon_completion']),
        "all": [
            lambda output, kwargs: add_header(output, "WorkBasedProgram"),
            lambda output, kwargs: add_provider_data(output, kwargs)
        ]
    }

    expected_output = {'@context': 'http://schema.org/', '@type': 'WorkBasedProgram', 'provider': {'@type': 'EducationalOrganization', 'name': 'Goodwill of Tucson', 'url': 'goodwill.org', 'contactPoint': {'@type': 'ContactPoint', 'telephone': '333-343-4444'}, 'address': [{'@type': 'PostalAddress', 'streetAddress': '1940 East Silverlake Rd', 'addressLocality': 'Tucson', 'addressRegion': 'AZ', 'postalCode': '85713'}]}, 'programPrerequisites': [{'@type': 'EducationalOccupationalCredential', 'credentialCategory': 'HighSchool'}, {'@type': 'Text', 'eligibleGroups': 'Youth'}, {'@type': 'Text', 'maxIncomeEligibility': '20000'}, {'@type': 'Text', 'otherProgramPrerequisites': 'other'}], 'offers': {'@type': 'Offer', 'category': 'Total Cost', 'priceSpecification': {'@type': 'PriceSpecification', 'price': 2000, 'priceCurrency': 'USD'}}, 'trainingSalary': {'@type': 'MonetaryAmountDistribution', 'currency': 'USD', 'duration': 'P1H', 'median': '11.00'}, 'salaryUponCompletion': {'@type': 'MonetaryAmountDistribution', 'currency': 'USD', 'duration': 'P1Y', 'median': '40000.00'}}

    output = add_data_keywords({}, input_kwargs, data_keywords_mapper)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


@pytest.mark.xfail
def test_add_header():
    pass
