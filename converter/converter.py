from converter.helper import (
    add_header,
    add_description,
    add_name,
    add_url,
    add_provider_data
)


def work_based_program_converter(**kwargs):
    _check_for_required(kwargs)

    output = {}

    output = add_header(output)
    output = add_description(output, kwargs['program_description'])
    output = add_name(output, kwargs['program_name'])
    output = add_url(output, kwargs['program_url'])

    output = add_provider_data(output, kwargs)

    return output


def _check_for_required(kwargs: dict) -> None:
    def assert_item(item):
        nonlocal kwargs
        assert(item in kwargs)

    assert_item("program_description")
    assert_item("program_name")
    assert_item("program_url")
    assert_item("provider_address")
