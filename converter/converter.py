from converter.helper import (add_header, add_basic_keywords, add_offers_data,
                              add_prerequisites_data, add_provider_data,
                              add_salary_upon_completion_data,
                              add_training_salary_data,
                              add_data_keywords)
import pdb

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


class Converter():
    def __init__(self, basic_keywords, data_keywords_mapper, kwarg_to_schema_key_mapper, required_keywords):

        self.required_keywords = required_keywords
        self.basic_keywords = basic_keywords
        self.data_keywords_mapper = data_keywords_mapper
        self.kwarg_to_schema_key_mapper = kwarg_to_schema_key_mapper

        self.output = {}

    def trigger_conversion(self, kwargs):
        self._check_for_required(kwargs)
        self._add_basic_keywords(kwargs)
        # pdb.set_trace()
        
        self._add_data_keywords(kwargs)
        # pdb.set_trace()

        return self.output

    def _check_for_required(self, kwargs):
        # TODO flatten kwargs and check all keys // BUT WE DONT NEED TO SUPPORT THIS

        def assert_required_keyword_is_in_kwargs(item):
            try:
                assert(item in kwargs)
            except AssertionError:
                raise RuntimeError("Required property not included")

        for required_keyword in self.required_keywords:
            assert_required_keyword_is_in_kwargs(required_keyword)

    def _add_basic_keywords(self, kwargs):
        self.output = add_basic_keywords(
            self.output,
            kwargs,
            self.basic_keywords,
            self.kwarg_to_schema_key_mapper)

    def _add_data_keywords(self, kwargs):
        # special case 'all'
        self.output = add_data_keywords(self.output, kwargs, self.data_keywords_mapper)


def work_based_program_converter(**kwargs):
    work_based_programs_converter = Converter(
        basic_keywords,
        data_keywords_mapper,
        kwarg_to_schema_key_mapper,
        required_keywords)

    return work_based_programs_converter.trigger_conversion(kwargs)
