from expects import expect, be_an, raise_error, have_property, equal, be_empty

class TestConverter():
    def test_converter(self):
        kwargs = {"test_arg": "value"}
        
        expected_output = {}

        output = convert(**input_)

        expect(output).to(equal(expected_output))
