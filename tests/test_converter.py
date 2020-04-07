import pytest

from converter.converter import Converter

@pytest.mark.parametrize("input_kwargs,additional_required_keywords,should_error", [
    ({"a_recommended_keyword": "value"}, ["a_required_keyword"], True),
    ({"a_recommended_keyword": "value"}, ["a_required_keyword, another_required_keyword"], True),
    ({"a_required_keyword_with_no_value": ""}, ["a_required_keyword_with_no_value"], True),
    ({"a_required_keyword": "value"}, ["a_required_keyword"], False)
])
def test_check_for_required(work_based_input_kwargs, input_kwargs, additional_required_keywords, should_error):
    required_input_kwargs = {
        "provider_address": work_based_input_kwargs["provider_address"],
        "program_name": work_based_input_kwargs["program_name"],
        "program_description": work_based_input_kwargs["program_description"],
        "program_url": work_based_input_kwargs["program_url"]
    }

    input_kwargs.update(required_input_kwargs)

    converter = Converter(
        data_keywords_mapper={"all": []},
        kwarg_to_schema_key_mapper={
            "program_description": "description",
            "program_name": "name",
            "program_url": "url"
        },
        additional_required_keywords=additional_required_keywords
    )

    if should_error:
        with pytest.raises(ValueError) as exceptionMsg:
            output = converter.trigger_conversion(input_kwargs)

        assert "Missing kwargs! Please include values for the following fields" in str(exceptionMsg.value)
        assert ",".join(additional_required_keywords) in str(exceptionMsg.value)
    else:
        output = converter.trigger_conversion(input_kwargs)
        assert output == {'name': 'Goodwill Program', 'description': 'A description of a Goodwill program', 'url': 'goodwill.org'}
