"""
Mock service data for the Manaaki Navigator Streamlit MVP.
This simulates a service directory with health, housing, financial, and social services.
"""

# Mock service data
mock_service_data = [
    # Auckland Health Services
    {
        "id": "auckland-city-mission",
        "name": "Auckland City Mission Health Centre",
        "name_maori": "Te Tari Hauora o Te Mīhana o Tāmaki Makaurau",
        "location": "Auckland",
        "address": "23 Union Street, Auckland Central",
        "phone": "09 303 9200",
        "website": "https://www.aucklandcitymission.org.nz/health-services/",
        "type": "general_practitioner",
        "tags": ["low_cost", "homeless", "addiction", "mental_health"],
        "description": "Provides healthcare services to homeless and vulnerable populations in Auckland.",
        "description_maori": "He ratonga hauora mō ngā tāngata kāinga-kore me ngā tāngata whakaraerae i Tāmaki Makaurau.",
        "eligibility": "Open to all, focus on homeless and low-income individuals",
        "hours": "Monday to Friday, 9am - 5pm",
        "cost": "Free for Community Services Card holders"
    },
    {
        "id": "tamaki-health",
        "name": "Tamaki Health",
        "name_maori": "Hauora Tāmaki",
        "location": "Auckland",
        "address": "Multiple locations across Auckland",
        "phone": "09 274 7823",
        "website": "https://www.tamakihealth.co.nz",
        "type": "general_practitioner",
        "tags": ["family_doctor", "children", "vaccination", "chronic_disease"],
        "description": "Network of affordable medical clinics across Auckland.",
        "description_maori": "He whatunga o ngā ratonga hauora utu-ngāwari puta noa i Tāmaki Makaurau.",
        "eligibility": "Open to all",
        "hours": "Varies by location, most open 7 days",
        "cost": "Low cost for Community Services Card holders"
    },
    {
        "id": "waitemata-phc",
        "name": "Waitematā DHB Primary Health Services",
        "name_maori": "Ngā Ratonga Hauora Tuatahi o Waitematā",
        "location": "Auckland",
        "address": "North Shore and Waitakere",
        "phone": "09 486 8900",
        "website": "https://www.waitematadhb.govt.nz",
        "type": "health_services",
        "tags": ["hospital", "emergency", "specialist", "maternity"],
        "description": "Comprehensive health services for North Shore and West Auckland.",
        "description_maori": "He ratonga hauora mō Te Raki me Te Uru o Tāmaki Makaurau.",
        "eligibility": "Residents of North Shore and West Auckland",
        "hours": "Emergency services 24/7, other services vary",
        "cost": "Free emergency care, other services may have costs"
    },
    
    # Wellington Health Services
    {
        "id": "tu-ora-compass",
        "name": "Tū Ora Compass Health",
        "name_maori": "Tū Ora Compass Health",
        "location": "Wellington",
        "address": "Level 4, 22-28 Willeston Street, Wellington",
        "phone": "04 801 7808",
        "website": "https://www.tuora.org.nz",
        "type": "general_practitioner",
        "tags": ["primary_care", "family_doctor", "maori_health", "pacific_health"],
        "description": "Network of primary healthcare providers across the Wellington region.",
        "description_maori": "He whatunga o ngā kaiwhakarato hauora tuatahi puta noa i te rohe o Te Whanganui-a-Tara.",
        "eligibility": "Open to all",
        "hours": "Varies by practice",
        "cost": "Varies by practice, subsidies available"
    },
    {
        "id": "wellington-hospital",
        "name": "Wellington Regional Hospital",
        "name_maori": "Te Hōhipera o Te Whanganui-a-Tara",
        "location": "Wellington",
        "address": "Riddiford Street, Newtown, Wellington",
        "phone": "04 385 5999",
        "website": "https://www.ccdhb.org.nz",
        "type": "hospital",
        "tags": ["emergency", "specialist", "surgery", "maternity"],
        "description": "Main hospital for the Wellington region providing comprehensive services.",
        "description_maori": "Te hōhipera matua o te rohe o Te Whanganui-a-Tara.",
        "eligibility": "Open to all",
        "hours": "Emergency department open 24/7",
        "cost": "Free for NZ citizens and residents"
    },
    {
        "id": "newtown-union",
        "name": "Newtown Union Health Service",
        "name_maori": "Te Ratonga Hauora Uniana o Newtown",
        "location": "Wellington",
        "address": "14 Hall Street, Newtown, Wellington",
        "phone": "04 389 2040",
        "website": "https://www.newtownunionhealthservice.org.nz",
        "type": "general_practitioner",
        "tags": ["low_cost", "community", "refugee", "maori_health", "pacific_health"],
        "description": "Community-owned health service providing affordable healthcare.",
        "description_maori": "He ratonga hauora nā te hapori, e whakarato ana i te hauora utu-ngāwari.",
        "eligibility": "Residents of Newtown and surrounding areas",
        "hours": "Monday to Friday, 8:30am - 5:00pm",
        "cost": "Low cost for enrolled patients"
    },
    
    # Christchurch Health Services
    {
        "id": "pegasus-health",
        "name": "Pegasus Health",
        "name_maori": "Hauora Pegasus",
        "location": "Christchurch",
        "address": "160 Bealey Avenue, Christchurch",
        "phone": "03 379 1739",
        "website": "https://www.pegasus.health.nz",
        "type": "general_practitioner",
        "tags": ["primary_care", "family_doctor", "mental_health", "chronic_disease"],
        "description": "Network of primary healthcare providers across Canterbury.",
        "description_maori": "He whatunga o ngā kaiwhakarato hauora tuatahi puta noa i Waitaha.",
        "eligibility": "Open to all",
        "hours": "Varies by practice",
        "cost": "Varies by practice, subsidies available"
    },
    {
        "id": "christchurch-hospital",
        "name": "Christchurch Hospital",
        "name_maori": "Te Hōhipera o Ōtautahi",
        "location": "Christchurch",
        "address": "2 Riccarton Avenue, Christchurch",
        "phone": "03 364 0640",
        "website": "https://www.cdhb.health.nz",
        "type": "hospital",
        "tags": ["emergency", "specialist", "surgery", "maternity"],
        "description": "Main hospital for the Canterbury region.",
        "description_maori": "Te hōhipera matua o te rohe o Waitaha.",
        "eligibility": "Open to all",
        "hours": "Emergency department open 24/7",
        "cost": "Free for NZ citizens and residents"
    },
    
    # Housing Services
    {
        "id": "msd-emergency-housing",
        "name": "Emergency Housing Special Needs Grant",
        "name_maori": "Te Pūtea Āwhina Whare Ohotata",
        "location": "Nationwide",
        "address": "Available at all Work and Income offices",
        "phone": "0800 559 009",
        "website": "https://www.workandincome.govt.nz/housing/nowhere-to-stay/emergency-housing.html",
        "type": "emergency_housing",
        "tags": ["housing", "emergency", "financial_assistance"],
        "description": "Financial assistance for emergency housing costs when you have nowhere to stay.",
        "description_maori": "He āwhina pūtea mō ngā utu whare ohotata ina kāore ō wāhi noho.",
        "eligibility": "NZ citizens or residents with emergency housing need",
        "hours": "Monday to Friday, 8:30am - 5:00pm",
        "cost": "Free to apply"
    },
    {
        "id": "kainga-ora",
        "name": "Kāinga Ora - Homes and Communities",
        "name_maori": "Kāinga Ora - Ngā Kāinga me ngā Hapori",
        "location": "Nationwide",
        "address": "Multiple offices nationwide",
        "phone": "0800 801 601",
        "website": "https://kaingaora.govt.nz",
        "type": "social_housing",
        "tags": ["housing", "public_housing", "rental"],
        "description": "Public housing provider for New Zealand.",
        "description_maori": "Te kaiwhakarato whare tūmatanui o Aotearoa.",
        "eligibility": "NZ citizens or residents with housing need",
        "hours": "Monday to Friday, 8:30am - 5:00pm",
        "cost": "Income-related rent"
    },
    
    # Financial Support Services
    {
        "id": "work-and-income",
        "name": "Work and Income",
        "name_maori": "Te Hiranga Tangata",
        "location": "Nationwide",
        "address": "Multiple offices nationwide",
        "phone": "0800 559 009",
        "website": "https://www.workandincome.govt.nz",
        "type": "financial_benefit",
        "tags": ["benefits", "financial_assistance", "employment"],
        "description": "Financial assistance and employment support.",
        "description_maori": "He āwhina pūtea me te tautoko mahi.",
        "eligibility": "Varies by benefit type",
        "hours": "Monday to Friday, 8:30am - 5:00pm",
        "cost": "Free to apply"
    },
    
    # Mental Health Services
    {
        "id": "mental-health-line",
        "name": "Mental Health Line - 1737",
        "name_maori": "Te Raina Hauora Hinengaro - 1737",
        "location": "Nationwide",
        "address": "Phone service",
        "phone": "1737",
        "website": "https://1737.org.nz",
        "type": "mental_health",
        "tags": ["counseling", "crisis", "support"],
        "description": "Free call or text to talk with a trained counsellor.",
        "description_maori": "Waea koreutu, tuku karere koreutu rānei ki te kōrero ki tētahi kaiāwhina ngaio.",
        "eligibility": "Open to all",
        "hours": "24/7",
        "cost": "Free"
    }
]

def get_services_by_location(location, service_type=None):
    """
    Filter services by location and optionally by service type.
    
    Args:
        location (str): Location to filter by
        service_type (str, optional): Service type to filter by
    
    Returns:
        list: Filtered list of services
    """
    # Normalize location name
    normalized_location = location.lower()
    
    # Filter services by location
    services = [
        service for service in mock_service_data 
        if service["location"].lower() == normalized_location or service["location"].lower() == "nationwide"
    ]
    
    # Further filter by service type if provided
    if service_type:
        services = [
            service for service in services 
            if service["type"] == service_type or service_type in service["tags"]
        ]
    
    return services

def get_service_by_id(service_id):
    """
    Get a service by its ID.
    
    Args:
        service_id (str): ID of the service to retrieve
    
    Returns:
        dict: Service data or None if not found
    """
    for service in mock_service_data:
        if service["id"] == service_id:
            return service
    return None

def get_maori_location_name(location):
    """
    Get the Māori name for a location.
    
    Args:
        location (str): English location name
    
    Returns:
        str: Māori location name or original name if not found
    """
    location_map = {
        "auckland": "Tāmaki Makaurau",
        "wellington": "Te Whanganui-a-Tara",
        "christchurch": "Ōtautahi",
        "hamilton": "Kirikiriroa",
        "dunedin": "Ōtepoti",
        "tauranga": "Tauranga Moana"
    }
    
    return location_map.get(location.lower(), location)

def get_all_locations():
    """
    Get a list of all unique locations in the service directory.
    
    Returns:
        list: List of unique locations
    """
    locations = set()
    for service in mock_service_data:
        if service["location"].lower() != "nationwide":
            locations.add(service["location"])
    
    return sorted(list(locations))

def get_all_service_types():
    """
    Get a list of all unique service types in the service directory.
    
    Returns:
        list: List of unique service types
    """
    service_types = set()
    for service in mock_service_data:
        service_types.add(service["type"])
        for tag in service["tags"]:
            service_types.add(tag)
    
    return sorted(list(service_types))
