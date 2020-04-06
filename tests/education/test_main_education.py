import json

import pytest
from expects import equal, expect

from converter import educational_occupational_programs_converter
from tests.conftest import pprint_diff


def test_educational_occupational_converter_all(educational_input_kwargs, offers):
    output = educational_occupational_programs_converter(**educational_input_kwargs)
    expected_output = {
        "@context": "http://schema.org/",
        "@type": "EducationalOccupationalProgram",
        "description": educational_input_kwargs["program_description"],
        "applicationDeadline": educational_input_kwargs["application_deadline"],
        "name": educational_input_kwargs["program_name"],
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
            "name": educational_input_kwargs["provider_name"],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": educational_input_kwargs["provider_address"][0]["street_address"],
                    "addressLocality": educational_input_kwargs["provider_address"][0]["address_locality"],
                    "addressRegion": educational_input_kwargs["provider_address"][0]["address_region"],
                    "postalCode": educational_input_kwargs["provider_address"][0]["postal_code"]
                }
            ],
            "url": educational_input_kwargs["provider_url"],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": educational_input_kwargs["provider_telephone"]
            }
        },
        "timeToComplete": educational_input_kwargs["time_to_complete"],
        "applicationStartDate": educational_input_kwargs["application_start_date"],
        "endDate": educational_input_kwargs["end_date"],
        "startDate": educational_input_kwargs["start_date"],
        "occupationalCredentialAwarded": educational_input_kwargs["occupational_credential_awarded"],
        "maximumEnrollment": educational_input_kwargs["maximum_enrollment"],
        "programPrerequisites": [
            {
                "@type": "EducationalOccupationalCredential", 
                "credentialCategory": educational_input_kwargs["program_prerequisites"]["credential_category"]
            },
            {
                "@type": "Text",
                "eligibleGroups": educational_input_kwargs["program_prerequisites"]["eligible_groups"]
            },
            {
                "@type": "Text",
                "maxIncomeEligibility": educational_input_kwargs["program_prerequisites"]["max_income_eligibility"]
            },
            {
                "@type": "Text",
                "otherProgramPrerequisites": educational_input_kwargs["program_prerequisites"]["other_program_prerequisites"]
            }
        ],
        "timeOfDay": educational_input_kwargs["time_of_day"]
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_educational_occupational_converter_required(educational_input_kwargs, offers):
    required_kwargs = {
        "application_deadline": educational_input_kwargs["application_deadline"],
        "program_description": educational_input_kwargs["program_description"],
        "program_name": educational_input_kwargs["program_name"],
        "offers_price": educational_input_kwargs["offers_price"],
        "program_url": educational_input_kwargs["program_url"],
        "provider_name": educational_input_kwargs["provider_name"],
        "provider_url": educational_input_kwargs["provider_url"],
        "provider_telephone": educational_input_kwargs["provider_telephone"],
        "provider_address": educational_input_kwargs["provider_address"],
        "time_to_complete": educational_input_kwargs["time_to_complete"],
    }
    
    expected_output = {
        "@context": "http://schema.org/",
        "@type": "EducationalOccupationalProgram",
        "applicationDeadline": educational_input_kwargs["application_deadline"],
        "name": educational_input_kwargs["program_name"],
        "description": educational_input_kwargs["program_description"],
        "identifier": [], # Can we ask Goodwill to provide one or the other value? They cannot provide both. How do we validate for one or more fields? 
        "offers": offers,
        "url": educational_input_kwargs["program_url"],
        "provider": {
            "@type": "EducationalOrganization",
            "name": educational_input_kwargs["provider_name"],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": educational_input_kwargs["provider_address"][0]["street_address"],
                    "addressLocality": educational_input_kwargs["provider_address"][0]["address_locality"],
                    "addressRegion": educational_input_kwargs["provider_address"][0]["address_region"],
                    "postalCode": educational_input_kwargs["provider_address"][0]["postal_code"]
                }
            ],
            "url": educational_input_kwargs["provider_url"],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": educational_input_kwargs["provider_telephone"]
            }
        },
        "timeToComplete": educational_input_kwargs["time_to_complete"]
    }

    output = educational_occupational_programs_converter(**required_kwargs)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))
