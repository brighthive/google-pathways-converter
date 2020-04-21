import json

import pytest
from expects import equal, expect

from converter.helper import add_prerequisites_data


def test_add_prerequisites_data(work_based_input_kwargs):
    input_kwargs = work_based_input_kwargs["program_prerequisites"]

    expected_output = {
        "programPrerequisites": {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": work_based_input_kwargs["program_prerequisites"]["credential_category"],
            "competencyRequired": work_based_input_kwargs["program_prerequisites"]["competency_required"]
        }
    }

    output = add_prerequisites_data({}, input_kwargs)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisites_credential(work_based_input_kwargs):
    input_kwargs = {
        "credential_category": "HighSchool"
    }

    expected_output = {
        "programPrerequisites": {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "HighSchool"
        }
    }

    output = add_prerequisites_data({}, input_kwargs)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisites_competency(work_based_input_kwargs):
    input_kwargs = {
        "competency_required": "Valid driver’s license"
    }

    expected_output = {
        "programPrerequisites": {
            "@type": "EducationalOccupationalCredential",
            "competencyRequired": "Valid driver’s license"
        }
    }

    output = add_prerequisites_data({}, input_kwargs)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisites_empty(work_based_input_kwargs):
    input_kwargs = {}
    expected_output = {}
    output = add_prerequisites_data({}, input_kwargs)

    expect(output).to(equal(expected_output))