# google-pathways-converter

This library translates keyword arguments into schema.org json-ld documents.

It provides a generalized internal conversion scheme that can be extended to support any json-ld schema.

# How it works
```
import work_programs_converter

kwargs = {
    "keyword": "value"
}

work_programs_json_ld = work_programs_converter(kwargs)
```

# Contribution
This can be easily extended to support any number of schema.org schemas.

# How to test
```
pipenv run pytest
```