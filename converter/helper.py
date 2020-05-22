import stringcase


def add_header(pathways_program: dict, type_str: str) -> dict:
    pathways_program["@context"] = "http://schema.org/"
    pathways_program["@type"] = type_str

    return pathways_program


def add_basic_keywords(pathways_program: dict, kwargs, kwarg_to_schema_key_mapper):
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

        pathways_program[camel_case_key] = value

    return pathways_program


def add_data_keywords(pathways_program: dict, kwargs, data_keywords_mapper):
    for fn in data_keywords_mapper['all']:
        pathways_program = fn(pathways_program, kwargs)

    for key, fn in data_keywords_mapper.items():
        if key == "all":
            continue

        try:
            pathways_program = fn(pathways_program, kwargs)
        except KeyError:
            pass

    return pathways_program


def add_provider_data(pathways_program: dict, kwargs: dict) -> dict:
    pathways_program['provider'] = {
        "@type": "EducationalOrganization",
    }

    if 'provider_name' in kwargs:
        pathways_program['provider']["name"] = kwargs['provider_name']

    if 'provider_url' in kwargs:
        pathways_program['provider']["url"] = kwargs['provider_url']

    if 'provider_telephone' in kwargs:
        pathways_program['provider']['contactPoint'] = {
            "@type": "ContactPoint",
            "contactType": "Admissions",
            "telephone": kwargs['provider_telephone']
        }

    # `provider_address` is a list that can contain one or more addresses.
    # `provider_address` is a required field, so we do not need to handle a KeyError.
    for address in kwargs['provider_address']:
        pathways_program = add_address_data(pathways_program, address)

    return pathways_program


def add_address_data(pathways_program: dict, address: dict) -> dict:    
    if 'address' not in pathways_program['provider']:
        pathways_program['provider']['address'] = []

    address_node = {
        "@type": "PostalAddress",
        "streetAddress": address.get("street_address", ""),
        "addressLocality": address.get("address_locality", ""),
        "addressRegion": address.get("address_region", ""),
        "postalCode": address.get("postal_code", ""),
        "addressCountry": address.get("address_country", "")
    }

    pathways_program['provider']['address'].append(address_node)

    return pathways_program


def add_prerequisites_data(pathways_program: dict, prerequisites: dict) -> dict:
    '''
    `programPrerequisites` accepts an EducationalOccupationalCredential object as its value.
    Currently, the BrightHive converter can handle two properties for the EducationalOccupationalCredential object:
        - credentialCategory: the level of education required, e.g., HighSchool
        - competencyRequired: knowledge, skill, ability, or personal attribute that must be demonstrated by a person or other entity.
    '''
    prereq_dict = {
        "@type": "EducationalOccupationalCredential"
    }
    try:
        credential_category = prerequisites["credential_category"]
        prereq_dict["credentialCategory"] = credential_category 
    except (KeyError, TypeError):
        pass

    try: 
        competency_required = prerequisites["competency_required"]
        prereq_dict["competencyRequired"] = competency_required
    except (KeyError, TypeError):
        pass
    
    if len(prereq_dict) > 1:
        pathways_program['programPrerequisites'] = prereq_dict

    return pathways_program


def add_offers_data(pathways_program: dict, price: int):
    offers_node = {
        "@type": "Offer",
        "category": "Total Cost",
        "priceSpecification": {
            "@type": "PriceSpecification",
            "price": price,
            "priceCurrency": "USD"
        }
    }

    pathways_program['offers'] = offers_node
    
    return pathways_program


def add_training_salary_data(pathways_program: dict, price: str):
    training_salary_node = {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1H", # Denotes hourly wage
        "median": price
    }

    pathways_program['trainingSalary'] = training_salary_node

    return pathways_program


def add_salary_upon_completion_data(pathways_program: dict, price: str):
    training_salary_node = {
        "@type": "MonetaryAmountDistribution",
        "currency": "USD",
        "duration": "P1Y", # Denotes annual salary
        "median": price
    }

    pathways_program['salaryUponCompletion'] = training_salary_node

    return pathways_program

def add_identifier_data(pathways_program: dict, cip=None, program_id=None):
    identifier_data = []

    if not cip and not program_id:
        raise ValueError('Missing kwargs! "identifier_cip" AND/OR "identifier_program_id" must have values.')

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
    
    pathways_program['identifier'] = identifier_data

    return pathways_program

def add_educational_program_mode():
