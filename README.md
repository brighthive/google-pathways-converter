# Google Pathways Converter

The `google-pathways-converter` is a Python package that converts a dictionary of keyword arguments into Google-pathways-friendly JSON-LD.  

## Motivation (Why did we build this?)

[Google Pathways](https://developers.google.com/search/docs/data-types/job-training) illuminates "pathways" for job seekers trying to acquire skills for a new role, job, or career. Google Pathways is an online utility integrated with the Google search engine: in other words, Google reads structured data from publicly available web pages, and if compatible with Pathways, the data appears in Google search results. *Try it for yourself!* Go to [Google](https://www.google.com/), and enter “job training and Richmond, VA”. You should see a panel with expandable results for jobs, paid training, and educational programs near Richmond. 

Google only ingests programs data that aligns with the schema definitions standardized by [schema.org](https://schema.org/). Schema.org specifies schemas for two program types: `WorkBasedProgram` and `EducationalOccupationalProgram`. A work-based program both provides job training and pays a wage. An educational-occupational program does not pay a wage, but offers a learning experience, which may or may not require the student to pay tuition and/or fees.

A BrightHive Data Trust may include data resources that describe work-based and/or educational-occupational programs. In many cases, Data Trust members want to easily, securely, and effectively disseminate information about their program offerings – something that Google Pathways facilitates. To this end, the `google-pathways-converter` library transforms data resources into Schema.org definitions, which can be consumed and returned by Google Pathways.

## Getting Started

### Installation
`google-pathways-converter` can be installed into your virtual environment in a number of ways. Pipenv users can run the following command:

```python
pipenv install -e git+https://github.com/brighthive/google-pathways-converter.git@master#egg=converter
```

Then, install the library wherever you need to it.

```python
from converter import educational_occupational_programs_converter, work_based_programs_converter
```

### Converter kwargs: Educational Occupational Programs
You need to consider the following fields for the educational-occupational converter: `educational_occupational_programs_converter`.

| Field        | Type   
| --------------------- | -------------
| **REQUIRED FIELDS**  
| program_name          | String              
| program_url           | String      
| provider_address      | A list of dicts. Each dict should have the following keys: street_address, address_locality, address_region, postal_code, and address_country.
| application_deadline  | String that represents a date value in ISO-8601 format
| offers_price          | Integer
| provider_name         | String
| provider_url          | String
| provider_telephone    | String
| time_to_complete                   | String that represents a duration in ISO-8601 format
| identifier_cip  AND/OR identifier_program_id | String
| occupational_category | A list of strings. Each string must reference a [BLS SOC-6 code](https://www.bls.gov/soc/2010/home.htm), e.g., ["47-2111", "49-9021"].
| **RECOMMENDED FIELDS**                
| application_start_date             | String
| start_date                         | String that represents a date in ISO-8601 format
| end_date                           | String that represents a date in ISO-8601 format
| occupational_credential_awarded    | String
| educational_program_mode           | String with one of three values: "IN_PERSON", "ONLINE", or "HYBRID". Only programs that take place 100% online qualify as being in "ONLINE" mode.
| maximum_enrollment                 | String
| offers_price                       | Integer
| time_of_day                        | String 
| program_prerequisites              | A dict with up to two specified keywords: "competency_required" (knowledge, skill, ability or personal attribute that a program participant must be able to demonstrate) and/or "credential_category" (a type of credential that a program participant must have)

### Converter kwargs: Work Based Programs
You need to consider the following fields for the work-based converter: `work_based_programs_converter`.

| Field        | Type   
| --------------------- | -------------
| **REQUIRED FIELDS**  
| program_name          | String              
| program_url           | String      
| provider_address      | A list of dicts. Each dict should have the following keys: street_address, address_locality, address_region, postal_code, and address_country. 
| program_description   | String
| occupational_category | A list of strings. Each string must reference a [BLS SOC-6 code](https://www.bls.gov/soc/2010/home.htm), e.g., ["47-2111", "49-9021"].
| **RECOMMENDED FIELDS**   
| program_description                | String
| provider_name                      | String
| provider_url                       | String
| provider_telephone                 | String
| identifier_program_id              | String
| start_date                         | String that represents a date in ISO-8601 format
| end_date                           | String that represents a date in ISO-8601 format
| occupational_credential_awarded    | String
| maximum_enrollment                 | String
| offers_price                       | Integer
| time_of_day                        | String 
| program_prerequisites              | A dict with up to two specified keywords: "competency_required" (knowledge, skill, ability or personal attribute that a program participant must be able to demonstrate) and/or "credential_category" (a type of credential that a program participant must have)

### Example

Below gives an example of the `educational_occupational_programs_converter`. Note: you can pass in a dict (recommended), or you may pass in the kwargs directly. If you use a dict, then remember to unpack it.

```python
from converter import educational_occupational_programs_converter

programs_input = {
    'application_deadline': '2020-04-01', 
    'program_name': 'Goodwill Program', 
    'offers_price': 2000, 
    'program_url': 'goodwill.org', 
    'provider_name': 'Goodwill of Springfield', 
    'provider_url': 'goodwill.org', 
    'provider_telephone': '333-343-4444', 
    'provider_address': [
        {
            'street_address': '1 Grickle Grass Lane', 
            'address_locality': 'Springfield', 
            'address_region': 'MA', 
            'address_country': 'US',
            'postal_code': '88881'
        }
    ], 
    'time_to_complete': 'P6M', 
    'identifier_cip': '51.3333', 
    'identifier_program_id': '5688', 
    'application_start_date': '2020-01-01', 
    'program_prerequisites': {
        'credential_category': 'HighSchool',
        'competency_required': 'Valid driver’s license'
    },
    'end_date': '2020-12-01', 
    'occupational_credential_awarded': 'Food Handlers Certification', 
    'maximum_enrollment': '50', 
    'start_date': '2020-04-01', 
    'time_of_day': 'Evening',
    'educational_program_mode': 'HYBRID'
}

output = educational_occupational_programs_converter(**programs_input)
json.dumps(output, sort_keys=True)
```

```python
# Results!
{
    "@context": "http://schema.org/", 
    "@type": "EducationalOccupationalProgram", 
    "applicationDeadline": "2020-04-01", 
    "applicationStartDate": "2020-01-01", 
    "endDate": "2020-12-01", 
    "identifier": [
        {
            "@type": "PropertyValue", 
            "propertyID": "CIP2010", 
            "value": "51.3333"
        }, 
        {
            "@type": "PropertyValue", 
            "propertyID": "ProgramID", 
            "value": "5688"
        }
    ], 
    "maximumEnrollment": "50", 
    "name": "Goodwill Program", 
    "occupationalCredentialAwarded": "Food Handlers Certification", 
    "offers": {
        "@type": "Offer", 
        "category": "Total Cost", 
        "priceSpecification": {
            "@type": "PriceSpecification", 
            "price": 2000, 
            "priceCurrency": "USD"
        }
    }, 
    "programPrerequisites": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "HighSchool",
        "competencyRequired": "Valid driver’s license"
    },
    "provider": {
        "@type": "EducationalOrganization", 
        "address": [
            {
                "@type": "PostalAddress", 
                "addressLocality": "Springfield", 
                "addressRegion": "MA",
                "addressCountry": "US", 
                "postalCode": "88881", 
                "streetAddress": "1 Grickle Grass Lane"
            }
        ], 
        "contactPoint": {
            "@type": "ContactPoint", 
            "telephone": "333-343-4444"
        }, 
        "name": "Goodwill of Springfield", 
        "url": "goodwill.org"
    }, 
    "startDate": "2020-04-01", 
    "timeOfDay": "Evening", "timeToComplete": "P6M", "url": "goodwill.org",
    "educationalProgramMode": "HYBRID"
}
```

## Testing
`google-pathways-converter` comes with a comprehensive suite of unit tests. Execute all tests by running:

```
pipenv run pytest
```
## How to contribute
We welcome code contributions, suggestions, and reports! Please report bugs, and make suggestions using [Github issues](https://github.com/brighthive/google-pathways-converter/issues). The BrightHive team will triage and prioritize your issue as soon as possible. 

## Team

* Regina Compton (Software Engineer)
* Logan Ripplinger (Software Engineer)

https://brighthive.io/brighthive-team/