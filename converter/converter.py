from converter.helper import add_basic_keywords, add_data_keywords

class Converter():
    def __init__(self, data_keywords_mapper, kwarg_to_schema_key_mapper, required_keywords=[]):
        if type(required_keywords) is str:
            required_keywords = required_keywords.replace(' ', '').split(',')

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
        '''
        This function checks two things:
        (1) the kwargs contain all required fields
        (2) all required fields have a value – Google pathways does not consider an empty string to be valid input.
        '''
        missing_kwargs = []
        for kwarg in self.required_keywords:
            if kwarg not in kwargs.keys():
                missing_kwargs.append(kwarg)
            elif kwargs[kwarg] == '' or kwargs[kwarg] == None or kwargs[kwarg] == []:
                missing_kwargs.append(kwarg)

        if missing_kwargs:
            missing_kwargs_as_str = ", ".join(missing_kwargs)
            raise ValueError(f"Missing kwargs! Please include values for the following fields: {missing_kwargs_as_str}")

    def _add_basic_keywords(self, kwargs):
        self.output = add_basic_keywords(
            self.output,
            kwargs,
            self.kwarg_to_schema_key_mapper)

    def _add_data_keywords(self, kwargs):
        self.output = add_data_keywords(self.output, kwargs, self.data_keywords_mapper)
