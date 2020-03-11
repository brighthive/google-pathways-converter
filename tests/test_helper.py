from converter.helper import add_provider_data, add_prerequisites_data
import json
from expects import expect, equal


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

    print(json.dumps(expected_output, sort_keys=True, indent=4))
    print(json.dumps(output, sort_keys=True, indent=4))

    expect(json_output).to(equal(json_expected_output))


def test_add_prerequisites_data(program_provider_address):
    kwargs = {}

    expected_output = { "programPrerequisites": [] }

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = add_prerequisites_data({}, kwargs)

    json_output = json.dumps(output, sort_keys=True)

    print(json.dumps(expected_output, sort_keys=True, indent=4))
    print(json.dumps(output, sort_keys=True, indent=4))

    expect(json_output).to(equal(json_expected_output))