from converter.helper import (add_header, add_basic_keywords, add_offers_data,
                              add_prerequisites_data, add_provider_data,
                              add_salary_upon_completion_data,
                              add_training_salary_data)


def work_based_program_converter(**kwargs):
    _check_for_required(kwargs)

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

    try:
        output = add_training_salary_data(output, kwargs['training_salary'])
    except KeyError:
        pass

    try:
        output = add_salary_upon_completion_data(output, kwargs['salary_upon_completion'])
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
