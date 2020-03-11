import pytest   

@pytest.fixture  
def program_provider_address(): 
    program_provider_address_data = [
        {
            "street_address": "1940 East Silverlake Rd",
            "address_locality": "Tucson",
            "address_region": "AZ",
            "postal_code": "85713"
        }
    ]

    return program_provider_address_data