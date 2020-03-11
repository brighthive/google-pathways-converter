import stringcase
from converter.helper import (
    add_header,
    add_provider_data,
    add_prerequisites_data,
    add_offers_data
)

kwarg_to_schema_key_mapper = {
    "program_description": "description",
    "program_name": "name",
    "program_url": "url"
}

basic_keywords = [
    "description",
    "name",
    "url",
    "endDate",
    "startDate",
    "maximumEnrollment",
    "occupationalCredentialAwarded",
    "timeOfDay",
    "timeToComplete",
]


def work_based_program_converter(**kwargs):
    _check_for_required(kwargs)
    # _check_for_unknown_fields(kwargs)

    output = {}

    output = add_header(output)
    output = add_basic_keywords(output, kwargs)

    try:
        output = add_provider_data(output, kwargs)
    except KeyError:
        raise RuntimeError("Required property not included")

    try:
        output = add_prerequisites_data(output, kwargs['program_prerequisites'])
    except KeyError:
        pass

    try:
        output = add_offers_data(output, kwargs['offers_price'])
    except KeyError:
        pass

    return output


def _check_for_required(kwargs: dict) -> None:
    def assert_item(item):
        nonlocal kwargs
        assert(item in kwargs)

    assert_item("program_description")
    assert_item("program_name")
    assert_item("program_url")
    assert_item("provider_address")


def add_basic_keywords(output, kwargs):
    for key, value in kwargs.items():
        ## first convert to ours if possible
        try:
            key = kwarg_to_schema_key_mapper[key]
        except KeyError:
            pass

        camel_case_key = stringcase.camelcase(key)
        if camel_case_key not in basic_keywords:
            continue

        output[camel_case_key] = value

    return output
