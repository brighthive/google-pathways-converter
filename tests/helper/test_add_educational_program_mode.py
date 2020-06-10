import pytest
from expects import equal, expect

from converter.helper import add_educational_program_mode


@pytest.mark.parametrize("program_mode", [
    ("IN_PERSON"),
    ("ONLINE"),
    ("HYBRID")
])
def test_add_educational_program_mode(program_mode):
    output = add_educational_program_mode({}, program_mode)
    expected_output = {
        "educationalProgramMode": program_mode,
    }

    expect(output).to(equal(expected_output))


def test_add_education_program_mode_add_nothing():
    output = add_educational_program_mode({})
    expected_output = { }

    expect(output).to(equal(expected_output))


@pytest.mark.parametrize("program_mode", [
    ("in person"),
    ("in-person"),
    ("On-line"),
    ("both")
])
def test_add_educational_program_mode_raise_error(program_mode):
    with pytest.raises(ValueError) as execinfo: 
        output = add_educational_program_mode({}, program_mode)

    expected_error = 'Invalid data! "educational_program_mode" must be one of the following: "IN_PERSON", "ONLINE", "HYBRID".'
    expect(str(execinfo.value)).to(equal(expected_error))