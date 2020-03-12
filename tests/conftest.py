from pprint import pprint

import pytest
from deepdiff import DeepDiff


def pprint_diff(expected_output, output):
    ddiff = DeepDiff(expected_output, output, ignore_order=True)
    pprint(ddiff, indent=4)


@pytest.fixture
def program_provider_address_data():
    return [
        {
            "street_address": "1940 East Silverlake Rd",
            "address_locality": "Tucson",
            "address_region": "AZ",
            "postal_code": "85713"
        }
    ]


@pytest.fixture
def offers():
    return {
        "@type": "Offer",
        "category": "Total Cost",
        "priceSpecification": {
            "@type": "PriceSpecification",
            "price": 2000,
            "priceCurrency": "USD"
        }
    }


@pytest.fixture
def training_salary():
    return {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1H",
        "median": "11.00"
    }


@pytest.fixture
def salary_upon_completion():
    return {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1Y",
        "median": "40000.00"
    }


@pytest.fixture
def input_kwargs(program_provider_address_data, offers, training_salary, salary_upon_completion):
    '''
    This fixture provides all kwargs (required and recommended) that
    can be passed into the converter.
    '''
    return {
        "program_description": "A description of a Goodwill program",
        "program_name": "Goodwill Program",
        "program_url": "goodwill.org",
        "provider_name": "Goodwill of Tucson",
        "provider_url": "goodwill.org",
        "provider_telephone": "333-343-4444",
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
        "occupational_credential_awarded": "Associate Degree",
        "time_of_day": "Evening",
        "time_to_complete": "P6M",
        "offers_price": offers['priceSpecification']['price'],
        "training_salary": training_salary['median'],
        "salary_upon_completion": salary_upon_completion['median']
    }

@pytest.fixture
def required_fields_as_jsonld(input_kwargs):
    return {
        "@context": "http://schema.org/",
        "@type": "WorkBasedProgram",
        "description": input_kwargs['program_description'],
        "name": input_kwargs['program_name'],
        "url": input_kwargs['program_url'],
        "provider": {
            "@type": "EducationalOrganization",
            "name": input_kwargs['provider_name'],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": "1940 East Silverlake Rd",
                    "addressLocality": "Tucson",
                    "addressRegion": "AZ",
                    "postalCode": "85713"
                }
            ],
            "url": input_kwargs['provider_url'],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": input_kwargs['provider_telephone']
            }
        }
    }