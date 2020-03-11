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
