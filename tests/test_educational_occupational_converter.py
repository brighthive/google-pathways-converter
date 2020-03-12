import json

from converter import educational_occupational_programs_converter
from expects import equal, expect
from tests.conftest import pprint_diff

# def test_educational_occupational_converter():
#     recommended_fields = {
        # "programPrerequisites": [
        #     {
        #         "@type": "EducationalOccupationalCredential", 
        #         "credentialCategory": "HighSchool"
        #     },
        #     {
        #         "@type": "Text",
        #         "eligibleGroups": "Youth"
        #     },
        #     {
        #         "@type": "Text",
        #         "maxIncomeEligibility": "20000"
        #     },
        #     {
        #         "@type": "Text",
        #         "otherProgramPrerequisites": "other"
        #     }
        # ],
        # "endDate": input_kwargs['end_date'],
        # "startDate": input_kwargs['start_date'],
        # "maximumEnrollment": input_kwargs['maximum_enrollment'],
        # "occupationalCredentialAwarded": input_kwargs['occupational_credential_awarded'],
        # "timeOfDay": input_kwargs['time_of_day'],
        # "timeToComplete": input_kwargs['time_to_complete'],
        # "offers": offers,
        # "trainingSalary": training_salary,
        # "salaryUponCompletion": salary_upon_completion
    # }
    # required_fields_as_jsonld.update(recommended_fields)

    # output = work_based_programs_converter(**input_kwargs)

    # pprint_diff(required_fields_as_jsonld, output)

    # json_expected_output = json.dumps(required_fields_as_jsonld, sort_keys=True)
    # json_output = json.dumps(output, sort_keys=True)

    # print(json.dumps(output, indent=4, sort_keys=True))
    # expect(json_output).to(equal(json_expected_output))

def test_educational_occupational_converter_all():
    # required_fields = {
    #     "applicationDeadline"
    # }

    expected_output = {}
    output = educational_occupational_programs_converter({})

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))

