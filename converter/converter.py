from converter.helper import add_basic_keywords, add_data_keywords

class Converter():
    def __init__(self, data_keywords_mapper, kwarg_to_schema_key_mapper, required_keywords):

        self.required_keywords = required_keywords
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
        missing_kwargs = [kwarg for kwarg in self.required_keywords if kwarg not in kwargs.keys()]

        if missing_kwargs:
            missing_kwargs_as_str = ", ".join(missing_kwargs)
            raise RuntimeError(f"One or more required properties needs to be included in the kwargs: {missing_kwargs_as_str}")

    def _add_basic_keywords(self, kwargs):
        self.output = add_basic_keywords(
            self.output,
            kwargs,
            self.kwarg_to_schema_key_mapper)

    def _add_data_keywords(self, kwargs):
        self.output = add_data_keywords(self.output, kwargs, self.data_keywords_mapper)
