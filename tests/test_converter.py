from expects import expect, equal
from converter import work_based_program_converter
import json


def test_work_based_program_converter(program_provider_address):
    kwargs = {
        "program_description": "desc",
        "program_name": "name",
        "program_url": "url",
        "provider_name": "provider name",
        "provider_url": "provider url",
        "provider_telephone": "telephone",
        "provider_address": program_provider_address,
        "program_prerequisites": {
            "credential_category": "HighSchool",
            "eligible_groups": "Youth",
            "max_income_eligibility": "20000",
            "other_program_prerequisites": "other"
        }
    }


    # Schema org 
    expected_output = {
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
            #     // ProgramAddress: "",
            ],
            "url": "provider url",
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": "telephone"
            }
        },
        "programPrerequisites": [
            {
                "@type": "EducationalOccupationalCredential", 
                "credentialCategory": "HighSchool"
            },
            {
                "@type": "Text",
                "eligibleGroups": "Youth"
            },
            {
                "@type": "Text",
                "maxIncomeEligibility": "20000"
            },
            {
                "@type": "Text",
                "otherProgramPrerequisites": "other"
            }
        ],
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = work_based_program_converter(**kwargs)

    json_output = json.dumps(output, sort_keys=True)

    print(json.dumps(expected_output, sort_keys=True, indent=4))
    print(json.dumps(output, sort_keys=True, indent=4))

    expect(json_output).to(equal(json_expected_output))
