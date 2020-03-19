# google-pathways-converter

The `google-pathways-converter` is a Python package that converts a dictionary of keyword arguments into Google-pathways-friendly JSON-LD.  

## Motivation (Why did we build this?)

An online utility integrated with the Google search engine, [Google Pathways](https://developers.google.com/search/docs/data-types/job-training) illuminates "pathways" for job seekers trying to acquire skills for a new role, job, or career. Google  reads structured data from publicly available web pages, and if compatible with Pathways, the data appears in Google search results. *Try it for yourself!* Go to [Google](https://www.google.com/), and enter “job training and Richmond, VA”. You should see a panel with expandable results for jobs, paid training, and educational programs near Richmond. 

Google only ingests programs data that aligns with the schema definitions standardized by [schema.org](https://schema.org/). Schema.org specifies schemas for two program types: `WorkBasedProgram` and `EducationalOccupationalProgram`. A work-based program both provides job training and pays a wage. An educational-occupational program does not pay a wage, but offers a learning experience, which may or may not require the student to pay tuition and/or fees.

A BrightHive Data Trust may include data resources that describe work-based and/or educational-occupational programs. In many cases, Data Trust members want to easily, securely, and effectively disseminate information about their program offerings – something that Google Pathways facilitates. To this end, the `google-pathways-converter` library transforms data resources into JSON-LD and makes it possible to integrate programs data with Google Pathways.

## Getting Started

### Installation
`google-pathways-converter` can be installed into your virtual environment in a number of ways. Pipenv users can run the following command:

```
pipenv install -e git+https://github.com/brighthive/google-pathways-converter.git@master#egg=converter
```

Then, install the library wherever you need to it.

```
from converter import educational_occupational_programs_converter, work_based_programs_converter
```

### Converter kwargs: Educational Occupational Programs
You need to consider the following fields for the educational-occupational converter: `educational_occupational_programs_converter`.

| Field        | Type   
| --------------------- | -------------
| **REQUIRED FIELDS**  
| program_name          | String              
| program_url           | String      
| provider_address      | A list of dicts. Each dict should have at least one of the following keys: street_address, address_locality, address_region, postal_code.        
| application_deadline  | String that represents a date value in ISO-8601 format
| offers_price          | Integer
| provider_name         | String
| provider_url          | String
| provider_telephone    | String
| time_to_complete      | String that represents a duration in ISO-8601 format
| **RECOMMENDED FIELDS**                
| identifier_cip                     | String
| identifier_program_id              | String
| application_start_date             | String
| program_prerequisites              | A dict with any number of keywords, e.g., credential_category, eligible_groups, max_income_eligibility, other_program_prerequisites, etc.
| start_date                         | String that represents a date in ISO-8601 format
| end_date                           | String that represents a date in ISO-8601 format
| occupational_credential_awarded    | String
| maximum_enrollment                 | String
| offers_price                       | Integer
| time_of_day                        | String 

### Converter kwargs: Work Based Programs
You need to consider the following fields for the work-based converter: `work_based_programs_converter`.

| Field        | Type   
| --------------------- | -------------
| **REQUIRED FIELDS**  
| program_name          | String              
| program_url           | String      
| provider_address      | A list of dicts. Each dict should have at least one of the following keys: street_address, address_locality, address_region, postal_code. 
| program_description   | String
| **RECOMMENDED FIELDS**   
| program_description                | String
| provider_name                      | String
| provider_url                       | String
| provider_telephone                 | String
| identifier_program_id              | String
| program_prerequisites              | A dict with any number of keywords, e.g., credential_category, eligible_groups, max_income_eligibility, other_program_prerequisites, etc.
| start_date                         | String that represents a date in ISO-8601 format
| end_date                           | String that represents a date in ISO-8601 format
| occupational_credential_awarded    | String
| maximum_enrollment                 | String
| offers_price                       | Integer
| time_of_day                        | String 

### Example

Below gives an example of the `educational_occupational_programs_converter`. Note: you can pass in a dict (recommended), or you may pass in the kwargs directly. If you use a dict, then remember to unpack it.

```
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
            'postal_code': '88881'
        }
    ], 
    'time_to_complete': 'P6M', 
    'identifier_cip': '51.3333', 
    'identifier_program_id': '5688', 
    'application_start_date': '2020-01-01', 
    'program_prerequisites': {
        'credential_category': 'HighSchool', 
        'eligible_groups': 'Youth', 
        'max_income_eligibility': '20000', 
        'other_program_prerequisites': 'other'
    }, 
    'end_date': '2020-12-01', 
    'occupational_credential_awarded': 'Food Handlers Certification', 
    'maximum_enrollment': '50', 
    'start_date': '2020-04-01', 
    'time_of_day': 'Evening'
}

output = educational_occupational_programs_converter(**programs_input)
json.dumps(output, sort_keys=True)
```

```
>>> {
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
    "programPrerequisites": [
        {
            "@type": "EducationalOccupationalCredential", 
            "credentialCategory": "HighSchool"
        }, 
        {
            "@type": "Text", 
            "eligibleGroups": "Youth"
        },
        {
            "@type": "Text", 
            "maxIncomeEligibility": "20000"
        }, 
        {
            "@type": "Text", 
            "otherProgramPrerequisites": "other"
        }
    ], 
    "provider": {
        "@type": "EducationalOrganization", 
        "address": [
            {
                "@type": "PostalAddress", 
                "addressLocality": "Springfield", 
                "addressRegion": "MA", 
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
    "timeOfDay": "Evening", "timeToComplete": "P6M", "url": "goodwill.org"
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