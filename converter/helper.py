import stringcase

def add_header(json_ld: dict) -> dict:
    output = {
        "@context": "http://schema.org/",
        "@type": "WorkBasedProgram",
    }

    return output


def _add_basic(json_ld: dict, key: str, value: str) -> dict:
    json_ld[key] = value
    return json_ld


def add_description(json_ld: dict, value: str) -> dict:
    return _add_basic(json_ld, "description", value)


def add_name(json_ld: dict, value: str) -> dict:
    return _add_basic(json_ld, "name", value)


def add_url(json_ld: dict, value: str) -> dict:
    return _add_basic(json_ld, "url", value)

def add_end_date(json_ld: dict, value: str) -> dict:
    return _add_basic(json_ld, "endDate", value)

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

    for address in kwargs['provider_address']:
        json_ld = _add_address_data(json_ld, address)

    return json_ld


def _add_address_data(json_ld: dict, address: dict) -> dict:    
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
        json_ld = _add_prerequisite_data(json_ld, prereq_key, prereq_value)

    return json_ld


def _add_prerequisite_data(json_ld: dict, prereq_key: str, prereq_value: str) -> dict:
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
    