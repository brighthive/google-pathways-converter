from converter.helper import (
    add_provider_data,
    add_prerequisites_data,
    add_offers_data,
    add_training_salary_data)
import json
from expects import expect, equal
from tests.conftest import pprint_diff


def test_add_provider_data(program_provider_address):
    kwargs = {
        "provider_name": "provider name",
        "provider_address": program_provider_address
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

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = add_provider_data({}, kwargs)

    json_output = json.dumps(output, sort_keys=True)

    pprint_diff(expected_output, output)

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisites_data():
    kwargs = {}

    expected_output = { "programPrerequisites": [] }

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = add_prerequisites_data({}, kwargs)

    json_output = json.dumps(output, sort_keys=True)

    pprint_diff(expected_output, output)

    expect(json_output).to(equal(json_expected_output))


def test_add_offers_data():
    offers_price = 123

    expected_output = {
        "offers": {
            "@type": "Offer",
            "category": "Total Cost",
            "priceSpecification": {
                "@type": "PriceSpecification",
                "price": 123,
                "priceCurrency": "USD"
            }
        }
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = add_offers_data({}, offers_price)

    json_output = json.dumps(output, sort_keys=True)

    pprint_diff(expected_output, output)

    expect(json_output).to(equal(json_expected_output))


def test_add_training_salary_data(program_provider_address):
    training_salary = "123.0"
    expected_output = {
        "trainingSalary": {
            "@type": "MonetaryAmountDistribution",
            "currency": "USD",
            "duration": "P1H",
            "median": "123.00"
        },
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = add_training_salary_data({}, training_salary)

    json_output = json.dumps(output, sort_keys=True)

    pprint_diff(expected_output, output)

    expect(json_output).to(equal(json_expected_output))