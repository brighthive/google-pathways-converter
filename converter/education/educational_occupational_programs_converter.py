from converter.converter import Converter
from converter.helper import (add_educational_program_mode, add_header,
                              add_identifier_data, add_offers_data,
                              add_prerequisites_data, add_provider_data,
                              add_salary_upon_completion_data,
                              add_training_salary_data,
                              validate_occupational_category)

# A list of keywords required for EducationalOccupationPrograms.
required_keywords = [
    "provider_address",
    "program_name",
    "program_description",
    "program_url",
    "application_deadline",
    "offers_price", 
    "provider_name", 
    "provider_url", 
    "provider_telephone", 
    "time_to_complete", 
    "occupational_category"
]

kwarg_to_schema_key_mapper = {
    "program_description": "description",
    "program_name": "name",
    "program_url": "url"
}

data_keywords_mapper = {
    "program_prerequisites": lambda output, kwargs: add_prerequisites_data(output, kwargs.get('program_prerequisites')),
    "offers_price": lambda output, kwargs: add_offers_data(output, kwargs['offers_price']),
    "educational_program_mode": lambda output, kwargs: add_educational_program_mode(output, kwargs["educational_program_mode"]),
    "occupational_category": lambda output, kwargs: validate_occupational_category(output, kwargs["occupational_category"]),
    "all": [
        lambda output, kwargs: add_header(output, "EducationalOccupationalProgram"),
        lambda output, kwargs: add_provider_data(output, kwargs),
        lambda output, kwargs: add_identifier_data(output, kwargs.get('identifier_cip'), kwargs.get('identifier_program_id'))
    ]
}

def educational_occupational_programs_converter(**kwargs):
    educational_occupational_programs_converter = Converter(
        data_keywords_mapper,
        kwarg_to_schema_key_mapper,
        required_keywords)

    return educational_occupational_programs_converter.trigger_conversion(kwargs)
