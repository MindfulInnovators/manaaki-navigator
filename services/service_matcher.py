"""
Service matching logic for the Manaaki Navigator Streamlit MVP.
This module provides functions for matching user needs to appropriate services.
"""

from services.mock_data import get_services_by_location, get_service_by_id, get_all_locations, get_all_service_types

def match_services(user_context):
    """
    Match services based on user context (location, needs, etc.)
    
    Args:
        user_context (dict): User context including location, service type, etc.
    
    Returns:
        list: Matched services
    """
    location = user_context.get("location", "")
    service_type = user_context.get("service_type", "")
    
    if not location:
        return []
    
    # Get services by location and optionally by service type
    services = get_services_by_location(location, service_type)
    
    # Sort services by relevance (simplified implementation)
    # In a real implementation, this would use more sophisticated ranking
    if service_type:
        # Put exact type matches first
        services.sort(key=lambda s: 0 if s["type"] == service_type else 
                     (1 if service_type in s["tags"] else 2))
    
    return services

def get_service_details(service_id, language="english"):
    """
    Get detailed information about a specific service.
    
    Args:
        service_id (str): ID of the service
        language (str): Language for service details
    
    Returns:
        dict: Service details formatted for display
    """
    service = get_service_by_id(service_id)
    if not service:
        return None
    
    # Format service details based on language
    if language == "maori":
        return {
            "name": service.get("name_maori", service["name"]),
            "description": service.get("description_maori", service["description"]),
            "address": service["address"],
            "phone": service["phone"],
            "website": service["website"],
            "hours": service["hours"],
            "cost": service["cost"],
            "eligibility": service["eligibility"]
        }
    else:  # english
        return {
            "name": service["name"],
            "description": service["description"],
            "address": service["address"],
            "phone": service["phone"],
            "website": service["website"],
            "hours": service["hours"],
            "cost": service["cost"],
            "eligibility": service["eligibility"]
        }

def get_service_recommendations(location, service_type=None, language="english", limit=3):
    """
    Get service recommendations based on location and service type.
    
    Args:
        location (str): User's location
        service_type (str, optional): Type of service needed
        language (str): Language for service details
        limit (int): Maximum number of recommendations to return
    
    Returns:
        list: Recommended services formatted for display
    """
    services = get_services_by_location(location, service_type)
    
    # Format service recommendations based on language
    recommendations = []
    for service in services[:limit]:
        if language == "maori":
            recommendations.append({
                "id": service["id"],
                "name": service.get("name_maori", service["name"]),
                "description": service.get("description_maori", service["description"]),
                "address": service["address"],
                "phone": service["phone"],
                "hours": service["hours"],
                "cost": service["cost"]
            })
        else:  # english
            recommendations.append({
                "id": service["id"],
                "name": service["name"],
                "description": service["description"],
                "address": service["address"],
                "phone": service["phone"],
                "hours": service["hours"],
                "cost": service["cost"]
            })
    
    return recommendations
