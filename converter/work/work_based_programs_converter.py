from converter.converter import Converter
from converter.work.helper import (add_header, add_offers_data,
                              add_prerequisites_data, add_provider_data,
                              add_salary_upon_completion_data,
                              add_training_salary_data)

kwarg_to_schema_key_mapper = {
    "program_description": "description",
    "program_name": "name",
    "program_url": "url"
}

basic_keywords = [
    "description",
    "name",
    "url",
    "endDate",  # Dates should use ISO-8601 format – do we need to validate?
    "startDate",
    "maximumEnrollment",
    "occupationalCredentialAwarded",
    "timeOfDay",
    "timeToComplete",  # Again, should be ISO-8601 format (for durations) – should this library validate for this?
]

data_keywords_mapper = {
    "program_prerequisites": lambda output, kwargs: add_prerequisites_data(output, kwargs['program_prerequisites']),
    "offers_price": lambda output, kwargs: add_offers_data(output, kwargs['offers_price']),
    "training_salary": lambda output, kwargs: add_training_salary_data(output, kwargs['training_salary']),
    "salary_upon_completion": lambda output, kwargs: add_salary_upon_completion_data(output, kwargs['salary_upon_completion']),
    "all": [
        lambda output, kwargs: add_header(output, "WorkBasedProgram"),
        lambda output, kwargs: add_provider_data(output, kwargs)
    ]
}

required_keywords = [
    "program_description",
    "program_name",
    "program_url",
    "provider_address",
]

def work_based_programs_converter(**kwargs):
    work_based_programs_converter = Converter(
        basic_keywords,
        data_keywords_mapper,
        kwarg_to_schema_key_mapper,
        required_keywords)

    return work_based_programs_converter.trigger_conversion(kwargs)
