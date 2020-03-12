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
def required_fields_as_jsonld():
    return {
        "@context": "http://schema.org/",
        "@type": "WorkBasedProgram",
        "description": "desc",
        "name": "name",
        "url": "url",
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
            ],
            "url": "provider url",
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": "telephone"
            }
        }
    }