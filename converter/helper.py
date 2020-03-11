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


## ....

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