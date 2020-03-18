import pytest

from converter.converter import Converter

@pytest.mark.parametrize("input_kwargs,required_keyword,should_error", [
    ({"a_recommended_keyword": "value"}, "a_required_keyword", True),
    ({"a_required_keyword": "value"}, "a_required_keyword", False)
])
def test_check_for_required(input_kwargs,required_keyword, should_error):
    required_keywords = [required_keyword]
    
    converter = Converter(
        data_keywords_mapper={"all": []},
        kwarg_to_schema_key_mapper={},
        required_keywords=required_keywords
    )

    if should_error:
        with pytest.raises(RuntimeError) as exceptionMsg:
            output = converter.trigger_conversion(input_kwargs)
        
        assert "One or more required properties needs to be included in the kwargs" in str(exceptionMsg.value)
        assert required_keyword in str(exceptionMsg.value)
    else:
        output = converter.trigger_conversion(input_kwargs)

        assert output == {}
