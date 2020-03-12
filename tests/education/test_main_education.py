import json

from converter import educational_occupational_programs_converter
from expects import equal, expect
from tests.conftest import pprint_diff


def test_educational_occupational_converter_all():
    kwargs = {
    #     "applicationDeadline"
    }

    expected_output = {

    }

    output = educational_occupational_programs_converter(kwargs)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))


def test_educational_occupational_converter_recommended():
    kwargs = {
    #     "applicationDeadline"
    }

    expected_output = {

    }

    output = educational_occupational_programs_converter(kwargs)

    pprint_diff(expected_output, output)

    json_expected_output = json.dumps(expected_output, sort_keys=True)
    json_output = json.dumps(output, sort_keys=True)

    expect(json_output).to(equal(json_expected_output))
