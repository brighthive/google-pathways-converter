import stringcase


def add_header(json_ld: dict, type_str: str) -> dict:
    json_ld["@context"] = "http://schema.org/"
    json_ld["@type"] = type_str

    return json_ld


def add_basic_keywords(output, kwargs, kwarg_to_schema_key_mapper):
    # A list of non-nested schema.org properties
    basic_keywords = [
        "applicationDeadline",
        "description",
        "name",
        "url",
        "endDate",  # Dates should use ISO-8601 format – do we need to validate?
        "startDate",
        "maximumEnrollment",
        "occupationalCredentialAwarded",
        "timeOfDay",
        "timeToComplete", # Again, should be ISO-8601 format (for durations) – should this library validate for this?
        "applicationStartDate" # ISO-8601 format
    ]

    for key, value in kwargs.items():
        try:
            key = kwarg_to_schema_key_mapper[key]
        except KeyError:
            pass

        camel_case_key = stringcase.camelcase(key)
        if camel_case_key not in basic_keywords:
            continue

        output[camel_case_key] = value

    return output


def add_data_keywords(output, kwargs, data_keywords_mapper):
    for fn in data_keywords_mapper['all']:
        output = fn(output, kwargs)

    for key, fn in data_keywords_mapper.items():
        if key == "all":
            continue

        try:
            output = fn(output, kwargs)
        except KeyError:
            pass

    return output


def add_provider_data(json_ld: dict, kwargs: dict) -> dict:
    json_ld['provider'] = {
        "@type": "EducationalOrganization",
    }

    if 'provider_name' in kwargs:
        json_ld['provider']["name"] = kwargs['provider_name']

    if 'provider_url' in kwargs:
        json_ld['provider']["url"] = kwargs['provider_url']

    if 'provider_telephone' in kwargs:
        json_ld['provider']['contactPoint'] = {
            "@type": "ContactPoint",
            "telephone": kwargs['provider_telephone']
        }

    # `provider_address` is a list that can contain one or more addresses.
    # `provider_address` is a required field, so we do not need to handle a KeyError.
    for address in kwargs['provider_address']:
        json_ld = add_address_data(json_ld, address)

    return json_ld


def add_address_data(json_ld: dict, address: dict) -> dict:    
    if 'address' not in json_ld['provider']:
        json_ld['provider']['address'] = []

    address_node = {
        "@type": "PostalAddress",
        "streetAddress": address.get("street_address", ""),
        "addressLocality": address.get("address_locality", ""),
        "addressRegion": address.get("address_region", ""),
        "postalCode": address.get("postal_code", "")
    }

    json_ld['provider']['address'].append(address_node)

    return json_ld


def add_prerequisites_data(json_ld: dict, prerequisites: list) -> dict:
    json_ld['programPrerequisites'] = []

    for prereq_key, prereq_value in prerequisites.items():
        json_ld = add_prerequisite(json_ld, prereq_key, prereq_value)

    return json_ld


def add_prerequisite(json_ld: dict, prereq_key: str, prereq_value: str) -> dict:
    prereq_type = "Text"
    if "credential_category" == prereq_key:
        prereq_type = "EducationalOccupationalCredential"

    camelcase_prereq = stringcase.camelcase(prereq_key)

    prereq_node = {
        "@type": prereq_type,
        camelcase_prereq: prereq_value
    }

    json_ld['programPrerequisites'].append(prereq_node)

    return json_ld


def add_offers_data(output, price: int):
    offers_node = {
        "@type": "Offer",
        "category": "Total Cost",
        "priceSpecification": {
            "@type": "PriceSpecification",
            "price": price,
            "priceCurrency": "USD"
        }
    }

    output['offers'] = offers_node
    
    return output


def add_training_salary_data(output, price: str):
    training_salary_node = {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1H", # Denotes hourly wage
        "median": price
    }

    output['trainingSalary'] = training_salary_node

    return output


def add_salary_upon_completion_data(output, price: str):
    training_salary_node = {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1Y", # Denotes annual salary
        "median": price
    }

    output['salaryUponCompletion'] = training_salary_node

    return output

def add_identifier_data(output, cip=None, program_id=None):
    identifier_data = []

    if cip:
        identifier_data.append({
            "@type": "PropertyValue",
            "propertyID": "CIP2010",
            "value": cip
        })
    
    if program_id:
        identifier_data.append({
            "@type": "PropertyValue",
            "propertyID": "ProgramID",
            "value": program_id
        })
    
    output['identifier'] = identifier_data

    return output