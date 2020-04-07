import pytest

from converter.converter import Converter

@pytest.mark.parametrize("input_kwargs,required_keywords,should_error", [
    ({"a_recommended_keyword": "value"}, ["a_required_keyword"], True),
    ({"a_recommended_keyword": "value"}, ["a_required_keyword, another_required_keyword"], True),
    ({"a_required_keyword_with_no_value": ""}, ["a_required_keyword_with_no_value"], True),
    ({"a_required_keyword_with_no_value": None}, ["a_required_keyword_with_no_value"], True),
    ({"a_required_keyword": "value"}, ["a_required_keyword"], False)
])
def test_check_for_required(input_kwargs, required_keywords, should_error):
    converter = Converter(
        data_keywords_mapper={"all": []},
        kwarg_to_schema_key_mapper={
            "program_description": "description",
            "program_name": "name",
            "program_url": "url"
        },
        required_keywords=required_keywords
    )

    if should_error:
        with pytest.raises(ValueError) as exceptionMsg:
            output = converter.trigger_conversion(input_kwargs)

        assert "Missing kwargs! Please include values for the following fields" in str(exceptionMsg.value)
        assert ", ".join(required_keywords) in str(exceptionMsg.value)
    else:
        output = converter.trigger_conversion(input_kwargs)
        assert output == {}


@pytest.mark.parametrize("required_keywords,initialized_required_keywords", [
    ("provider_address", ["provider_address"]),
    ("provider_address,program_name,program_url", ["provider_address", "program_name", "program_url"]),
    ("provider_address, program_name", ["provider_address", "program_name"])
])
def test_required_keywords_init(required_keywords, initialized_required_keywords):
    converter = Converter(
        data_keywords_mapper={"all": []},
        kwarg_to_schema_key_mapper={},
        required_keywords=required_keywords
    )

    assert converter.required_keywords == initialized_required_keywords