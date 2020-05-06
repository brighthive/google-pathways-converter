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


def test_add_data_keywords(work_based_input_kwargs, training_salary, salary_upon_completion):
    data_keywords_mapper = {
        "program_prerequisites": lambda output, kwargs: add_prerequisites_data(output, kwargs["program_prerequisites"]),
        "offers_price": lambda output, kwargs: add_offers_data(output, kwargs["offers_price"]),
        "training_salary": lambda output, kwargs: add_training_salary_data(output, kwargs["training_salary"]),
        "salary_upon_completion": lambda output, kwargs: add_salary_upon_completion_data(output, kwargs["salary_upon_completion"]),
        "all": [
            lambda output, kwargs: add_header(output, "WorkBasedProgram"),
            lambda output, kwargs: add_provider_data(output, kwargs)
        ]
    }

    expected_output = {
        "@context": "http://schema.org/",
        "@type": "WorkBasedProgram",
        "offers": {
            "@type": "Offer",
            "category": "Total Cost",
            "priceSpecification": {
                "@type": "PriceSpecification",
                "price": work_based_input_kwargs["offers_price"],
                "priceCurrency": "USD"
            }
        },
        "programPrerequisites": {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": work_based_input_kwargs["program_prerequisites"]["credential_category"],
            "competencyRequired": work_based_input_kwargs["program_prerequisites"]["competency_required"]
        },
        "provider": {
            "@type": "EducationalOrganization",
            "name": work_based_input_kwargs['provider_name'],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": work_based_input_kwargs['provider_address'][0]['street_address'],
                    "addressLocality": work_based_input_kwargs['provider_address'][0]['address_locality'],
                    "addressRegion": work_based_input_kwargs['provider_address'][0]['address_region'],
                    "addressCountry": work_based_input_kwargs['provider_address'][0]['address_country'],
                    "postalCode": work_based_input_kwargs['provider_address'][0]['postal_code']
                }
            ],
            "url": work_based_input_kwargs['provider_url'],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "Admissions",
                "telephone": work_based_input_kwargs['provider_telephone']
            }
        },
        "trainingSalary": training_salary,
        "salaryUponCompletion": salary_upon_completion
    }
    
    output = add_data_keywords({}, work_based_input_kwargs, data_keywords_mapper)

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

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


@pytest.mark.parametrize("program_type", [
    ("EducationalOccupationalProgram"),
    ("WorkBasedProgram")
])
def test_add_header(program_type):
    output = add_header({}, program_type)

    expected_output = {
        "@context": "http://schema.org/",
        "@type": program_type
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))
