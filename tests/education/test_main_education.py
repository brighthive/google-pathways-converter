import json

import pytest
from expects import equal, expect

from converter import educational_occupational_programs_converter
from tests.conftest import pprint_diff


@pytest.mark.skip
def test_educational_occupational_converter_all():
    kwargs = {
    #     "applicationDeadline"
    }

    expected_output = {

    }

    output = educational_occupational_programs_converter(kwargs)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_educational_occupational_converter_recommended(educational_input_kwargs, offers):
    expected_output = {
        "@context": "http://schema.org/",
        "@type": "EducationalOccupationalProgram",
        "applicationDeadline": educational_input_kwargs['application_deadline'],
        "name": educational_input_kwargs['program_name'],
        "identifier": [
            {
                "@type": "PropertyValue",
                "propertyID": "CIP2010",
                "value": educational_input_kwargs["identifier_cip"]
            },
            {
                "@type": "PropertyValue",
                "propertyID": "ProgramID",
                "value": educational_input_kwargs["identifier_program_id"]
            }
        ],
        "offers": offers,
        "url": educational_input_kwargs["program_url"],
        "provider": {
            "@type": "EducationalOrganization",
            "name": educational_input_kwargs['provider_name'],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": educational_input_kwargs['provider_address'][0]['street_address'],
                    "addressLocality": educational_input_kwargs['provider_address'][0]['address_locality'],
                    "addressRegion": educational_input_kwargs['provider_address'][0]['address_region'],
                    "postalCode": educational_input_kwargs['provider_address'][0]['postal_code']
                }
            ],
            "url": educational_input_kwargs['provider_url'],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": educational_input_kwargs['provider_telephone']
            }
        },
        "timeToComplete": educational_input_kwargs['time_to_complete']
    }

    output = educational_occupational_programs_converter(educational_input_kwargs)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))
