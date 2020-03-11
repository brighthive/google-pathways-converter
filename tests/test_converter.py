from expects import expect, equal
from converter import work_based_program_converter
import json
from tests.conftest import pprint_diff

# TODO salaryUponCompletion
# trainingSalary


def test_work_based_program_converter_all(program_provider_address):
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
        },
        "end_date": "2020",
        "start_date": "2019",
        "maximumEnrollment": "maximumEnrollment",
        "occupationalCredentialAwarded": "occupationalCredentialAwarded",
        "timeOfDay": "timeOfDay",
        "timeToComplete": "timeToComplete",
        "offers_price": 123,
        "training_salary": "123.0"
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
        "endDate": "2020",
        "startDate": "2019",
        "maximumEnrollment": "maximumEnrollment",
        "occupationalCredentialAwarded": "occupationalCredentialAwarded",
        "timeOfDay": "timeOfDay",
        "timeToComplete": "timeToComplete",
        "offers": {
            "@type": "Offer",
            "category": "Total Cost",
            "priceSpecification": {
                "@type": "PriceSpecification",
                "price": 123,
                "priceCurrency": "USD"
            }
        },
        "trainingSalary": {
            "@type": "MonetaryAmountDistribution",
            "currency": "USD",
            "duration": "P1H",
            "median": "123.00"
        }
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = work_based_program_converter(**kwargs)

    json_output = json.dumps(output, sort_keys=True)

    pprint_diff(expected_output, output)

    expect(json_output).to(equal(json_expected_output))


def test_work_based_program_converter_required(program_provider_address):
    kwargs = {
        "program_description": "desc",
        "program_name": "name",
        "program_url": "url",
        "provider_name": "provider name",
        "provider_url": "provider url",
        "provider_telephone": "telephone",
        "provider_address": program_provider_address
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
            ],
            "url": "provider url",
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": "telephone"
            }
        }
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)

    output = work_based_program_converter(**kwargs)

    json_output = json.dumps(output, sort_keys=True)

    pprint_diff(expected_output, output)

    expect(json_output).to(equal(json_expected_output))