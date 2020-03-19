import json

from expects import equal, expect

from converter.helper import add_provider_data, add_address_data
from tests.conftest import pprint_diff

def test_add_provider_data_all_fields(work_based_input_kwargs, program_provider_address_data):
    kwargs = {
        "provider_name": work_based_input_kwargs['provider_name'],
        "provider_url": work_based_input_kwargs['provider_url'],
        "provider_telephone": work_based_input_kwargs['provider_telephone'],
        "provider_address": program_provider_address_data
    }

    expected_output = {
        "provider": {
            "@type": "EducationalOrganization",
            "name": work_based_input_kwargs['provider_name'],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": work_based_input_kwargs['provider_address'][0]['street_address'],
                    "addressLocality": work_based_input_kwargs['provider_address'][0]['address_locality'],
                    "addressRegion": work_based_input_kwargs['provider_address'][0]['address_region'],
                    "postalCode": work_based_input_kwargs['provider_address'][0]['postal_code']
                }
            ],
            "url": work_based_input_kwargs['provider_url'],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": work_based_input_kwargs['provider_telephone']
            }
        },
    }

    output = add_provider_data({}, kwargs)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_provider_data_only_required_fields(work_based_input_kwargs, program_provider_address_data):
    kwargs = {
        "provider_address": program_provider_address_data
    }

    expected_output = {
        "provider": {
            "@type": "EducationalOrganization",
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": work_based_input_kwargs['provider_address'][0]['street_address'],
                    "addressLocality": work_based_input_kwargs['provider_address'][0]['address_locality'],
                    "addressRegion": work_based_input_kwargs['provider_address'][0]['address_region'],
                    "postalCode": work_based_input_kwargs['provider_address'][0]['postal_code']
                }
            ],
        },
    }

    output = add_provider_data({}, kwargs)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))

def test_add_address_data(program_provider_address_data):
    """
    `add_provider_data` calls `add_address_data`. 
    This test and the following one unit test that `add_address_data` populates the 
    address property and allows optional values.
    """
    expected_output = {
        "provider": {
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": program_provider_address_data[0]['street_address'],
                    "addressLocality": program_provider_address_data[0]['address_locality'],
                    "addressRegion": program_provider_address_data[0]['address_region'],
                    "postalCode": program_provider_address_data[0]['postal_code']
                }
            ]
        }
    }

    output = add_address_data({"provider": {}}, program_provider_address_data[0])

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))

def test_add_address_data_empty_values():
    expected_output = {
        "provider": {
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": "",
                    "addressLocality": "",
                    "addressRegion": "",
                    "postalCode": ""
                }
            ]
        }
    }

    output = add_address_data({"provider": {}}, {})

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))



