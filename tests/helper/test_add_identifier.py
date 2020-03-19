import json

import pytest
from expects import equal, expect

from converter.helper import add_identifier_data


def test_add_identifier_data(educational_input_kwargs):
    cip = educational_input_kwargs['identifier_cip']
    program_id = educational_input_kwargs['identifier_program_id']

    output = add_identifier_data({}, cip=cip, program_id=program_id)

    expected_output = {
        "identifier": [
            {
                "@type": "PropertyValue",
                "propertyID": "CIP2010",
                "value": cip
            },
            {
                "@type": "PropertyValue",
                "propertyID": "ProgramID",
                "value": program_id
            }
        ]
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_identifier_data_no_values():
    output = add_identifier_data({})

    expected_output = {
        "identifier": []
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_identifier_data_one_value(educational_input_kwargs):
    cip = educational_input_kwargs['identifier_cip']

    output = add_identifier_data({}, cip=cip)

    expected_output = {
        "identifier": [
            {
                "@type": "PropertyValue",
                "propertyID": "CIP2010",
                "value": cip
            }
        ]
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))