import pytest
from pprint import pprint
from deepdiff import DeepDiff


def pprint_diff(expected_output, output):
    ddiff = DeepDiff(expected_output, output, ignore_order=True)
    pprint(ddiff, indent=4)


@pytest.fixture
def program_provider_address():
    program_provider_address_data = [
        {
            "street_address": "1940 East Silverlake Rd",
            "address_locality": "Tucson",
            "address_region": "AZ",
            "postal_code": "85713"
        }
    ]

    return program_provider_address_data


@pytest.fixture
def offers():
    offers_data = {
        "@type": "Offer",
        "category": "Total Cost",
        "priceSpecification": {
            "@type": "PriceSpecification",
            "price": 2000,
            "priceCurrency": "USD"
        }
    }

    return offers_data


@pytest.fixture
def training_salary():
    training_salary_data = {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1H",
        "median": "11.00"
    }

    return training_salary_data


@pytest.fixture
def salary_upon_completion():
    salary_upon_completion_data = {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1Y",
        "median": "40000.00"
    }

    return salary_upon_completion_data