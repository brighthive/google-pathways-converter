from converter.converter import Converter

def test_converter_check_for_required(work_based_input_kwargs):
    required_keywords = [
        "program_description",
        "program_name",
        "program_url",
        "provider_address",
    ]
    
    converter = Converter(
        data_keywords_mapper={},
        kwarg_to_schema_key_mapper={},
        required_keywords=required_keywords
    )

    converter.trigger_conversion(work_based_input_kwargs)
