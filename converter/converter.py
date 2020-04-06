from converter.helper import add_basic_keywords, add_data_keywords

class Converter():
    def __init__(self, data_keywords_mapper, kwarg_to_schema_key_mapper, additional_required_keywords=[]):
        self.required_keywords = ["provider_address", "program_name", "program_description", "program_url"] + additional_required_keywords
        self.data_keywords_mapper = data_keywords_mapper
        self.kwarg_to_schema_key_mapper = kwarg_to_schema_key_mapper

        self.output = {}

    def trigger_conversion(self, kwargs):
        self._check_for_required(kwargs)
        self._add_basic_keywords(kwargs)
        self._add_data_keywords(kwargs)

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
            self.kwarg_to_schema_key_mapper)

    def _add_data_keywords(self, kwargs):
        self.output = add_data_keywords(self.output, kwargs, self.data_keywords_mapper)
