import json

from converter import work_based_programs_converter
from expects import equal, expect
from tests.conftest import pprint_diff


def test_work_based_programs_converter_all(work_based_input_kwargs, offers, training_salary, salary_upon_completion):
    output = work_based_programs_converter(**work_based_input_kwargs)
    expected_output = {
        "@context": "http://schema.org/",
        "@type": "WorkBasedProgram",
        "name": work_based_input_kwargs['program_name'],
        "description": work_based_input_kwargs['program_description'],
        "url": work_based_input_kwargs["program_url"],
        "offers": offers,
        "provider": {
            "@type": "EducationalOrganization",
            "name": work_based_input_kwargs['provider_name'],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": work_based_input_kwargs['provider_address'][0]['street_address'],
                    "addressLocality": work_based_input_kwargs['provider_address'][0]['address_locality'],
                    "addressRegion": work_based_input_kwargs['provider_address'][0]['address_region'],
                    "addressCountry": work_based_input_kwargs['provider_address'][0]['address_country'],
                    "postalCode": work_based_input_kwargs['provider_address'][0]['postal_code']
                }
            ],
            "url": work_based_input_kwargs['provider_url'],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "Admissions",
                "telephone": work_based_input_kwargs['provider_telephone']
            }
        },
        "timeToComplete": work_based_input_kwargs['time_to_complete'],
        "endDate": work_based_input_kwargs['end_date'],
        "startDate": work_based_input_kwargs['start_date'],
        "maximumEnrollment": work_based_input_kwargs["maximum_enrollment"],
        "programPrerequisites": {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": work_based_input_kwargs["program_prerequisites"]["credential_category"],
            "competencyRequired": work_based_input_kwargs["program_prerequisites"]["competency_required"]
        },
        "timeOfDay": work_based_input_kwargs["time_of_day"],
        "trainingSalary": training_salary,
        "salaryUponCompletion": salary_upon_completion,
        "occupationalCredentialAwarded": work_based_input_kwargs["occupational_credential_awarded"],
        "occupationalCategory": ["15-1152", "15-2021", "15-2031"]
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_work_based_programs_converter_required(work_based_input_kwargs):
    required_kwargs = {
        "program_description": work_based_input_kwargs['program_description'],
        "program_name": work_based_input_kwargs['program_name'],
        "program_url": work_based_input_kwargs['program_url'],
        "provider_name": work_based_input_kwargs['provider_name'],
        "provider_url": work_based_input_kwargs['provider_url'],
        "provider_telephone": work_based_input_kwargs['provider_telephone'],
        "provider_address": work_based_input_kwargs['provider_address'],
        "occupational_category": ["15-1152", "15-2021", "15-2031"]
    }
    output = work_based_programs_converter(**required_kwargs)

    expected_output = {
        "@context": "http://schema.org/",
        "@type": "WorkBasedProgram",
        "description": work_based_input_kwargs['program_description'],
        "name": work_based_input_kwargs['program_name'],
        "url": work_based_input_kwargs['program_url'],
        "provider": {
            "@type": "EducationalOrganization",
            "name": work_based_input_kwargs['provider_name'],
            "address": [ 
                {
                    "@type": "PostalAddress", 
                    "streetAddress": work_based_input_kwargs['provider_address'][0]['street_address'],
                    "addressLocality": work_based_input_kwargs['provider_address'][0]['address_locality'],
                    "addressRegion": work_based_input_kwargs['provider_address'][0]['address_region'],
                    "addressCountry": work_based_input_kwargs['provider_address'][0]['address_country'],
                    "postalCode": work_based_input_kwargs['provider_address'][0]['postal_code']
                }
            ],
            "url": work_based_input_kwargs['provider_url'],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "Admissions",
                "telephone": work_based_input_kwargs['provider_telephone']
            }
        },
        "occupationalCategory": ["15-1152", "15-2021", "15-2031"]
    }

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)
    
    expect(json_output).to(equal(json_expected_output))
