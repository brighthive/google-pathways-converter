import json

import pytest
from expects import equal, expect

from converter.helper import add_prerequisite, add_prerequisites_data


def test_add_prerequisites_data(work_based_input_kwargs):
    input_kwargs = work_based_input_kwargs["program_prerequisites"]
    
    expected_output = {
        "programPrerequisites": [
            {
                "@type": "EducationalOccupationalCredential",
                "credentialCategory": work_based_input_kwargs["program_prerequisites"]["credential_category"]
            },
            {
                "@type": "Text",
                "eligibleGroups": work_based_input_kwargs["program_prerequisites"]["eligible_groups"]
            },
            {
                "@type": "Text",
                "maxIncomeEligibility": work_based_input_kwargs["program_prerequisites"]["max_income_eligibility"]
            },
            {
                "@type": "Text",
                "otherProgramPrerequisites": work_based_input_kwargs["program_prerequisites"]["other_program_prerequisites"]
            }
        ]
    }

    output = add_prerequisites_data({}, input_kwargs)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisite_credential_category():
    output = add_prerequisite({'programPrerequisites': []}, "credential_category", "HighSchool")

    expected_output = {
        'programPrerequisites': [
            {
                '@type': 'EducationalOccupationalCredential', 
                'credentialCategory': 'HighSchool'
            }
        ]
    }
    
    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisite_other():
    output = add_prerequisite({'programPrerequisites': []}, 'eligible_groups', 'Youth')

    expected_output = {
        'programPrerequisites': [
            {
                '@type': 'Text', 
                'eligibleGroups': 'Youth'
            }
        ]
    }
    
    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))
