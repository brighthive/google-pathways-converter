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
            "street_address": "1 Grickle Grass Lane",
            "address_locality": "Springfield",
            "address_region": "MA",
            "postal_code": "88881"
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
def work_based_input_kwargs(program_provider_address_data, offers, training_salary, salary_upon_completion):
    '''
    This fixture provides all kwargs (required and recommended) that
    can be passed into the converter for WorkBasedPrograms.
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
            "competency_required": "Valid driver’s license"
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
def educational_input_kwargs(program_provider_address_data, offers, training_salary, salary_upon_completion):
    '''
    This fixture provides all kwargs (required and recommended) that
    can be passed into the converter for EducationalOccupationalPrograms.
    '''
    return {
        "application_deadline": "2020-04-01",
        "program_description": "A description of a Goodwill program",
        "program_name": "Goodwill Program",
        "offers_price": 2000,
        "program_url": "goodwill.org",
        "provider_name": "Goodwill of Tucson",
        "provider_url": "goodwill.org",
        "provider_telephone": "333-343-4444",
        "provider_address": program_provider_address_data,
        "time_to_complete": "P6M",
        "identifier_cip": "51.3902", # Must include CIP or Program Identifier
        "identifier_program_id": "5688",
        "application_start_date": "2020-01-01",
        "program_prerequisites": {
            "credential_category": "HighSchool",
            "competency_required": "Valid driver’s license"
        },
        "end_date": "2020-12-01",
        "occupational_credential_awarded": "Associate Degree",
        "maximum_enrollment": "50",
        "offers_price": offers['priceSpecification']['price'],
        "start_date": "2020-04-01",
        "time_of_day": "Evening",
    }