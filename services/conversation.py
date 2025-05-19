"""
Conversation handling logic for the Manaaki Navigator Streamlit MVP.
This module provides functions for processing user input and generating responses.
"""

from services.mock_data import get_services_by_location, get_maori_location_name

# Define language constants
ENGLISH = "english"
MAORI = "maori"

# Define cultural mode constants
GENERAL = "general"
MAORI_RESPONSIVE = "maori-responsive"

def detect_intent(input_text, language=ENGLISH):
    """
    Detect the user's intent based on their input text.
    
    Args:
        input_text (str): User's input text
        language (str): Current language setting
    
    Returns:
        str: Detected intent
    """
    # Normalize input
    normalized_input = input_text.lower().strip()
    
    # Health-related queries
    if any(keyword in normalized_input for keyword in [
        "health", "doctor", "medical", "hospital", "gp", "hauora", "tākuta"
    ]):
        return "health_services"
    
    # Housing-related queries
    elif any(keyword in normalized_input for keyword in [
        "housing", "home", "rent", "homeless", "whare", "kāinga"
    ]):
        return "housing_assistance"
    
    # Financial assistance queries
    elif any(keyword in normalized_input for keyword in [
        "money", "financial", "benefit", "payment", "pūtea", "tautoko pūtea"
    ]):
        return "financial_support"
    
    # Social support queries
    elif any(keyword in normalized_input for keyword in [
        "family", "social", "support", "community", "whānau", "tautoko pāpori"
    ]):
        return "social_support"
    
    # Mental health queries
    elif any(keyword in normalized_input for keyword in [
        "mental", "anxiety", "depression", "stress", "counseling", "hinengaro"
    ]):
        return "mental_health"
    
    # Greeting queries
    elif any(keyword in normalized_input for keyword in [
        "hello", "hi", "kia ora", "tēnā koe", "greetings"
    ]):
        return "greeting"
    
    # Thank you queries
    elif any(keyword in normalized_input for keyword in [
        "thank", "thanks", "helpful", "good", "great", "kia ora"
    ]):
        return "thanks"
    
    # Goodbye queries
    elif any(keyword in normalized_input for keyword in [
        "bye", "goodbye", "exit", "quit", "end", "ka kite"
    ]):
        return "goodbye"
    
    # Default to unknown intent
    return "unknown"

def extract_entities(input_text):
    """
    Extract entities like location, service type, etc. from user input.
    
    Args:
        input_text (str): User's input text
    
    Returns:
        dict: Extracted entities
    """
    entities = {}
    
    # Extract location
    locations = [
        "auckland", "wellington", "christchurch", "hamilton", "tauranga", 
        "dunedin", "palmerston north", "nelson", "rotorua", "whangarei",
        "invercargill", "new plymouth", "whanganui", "gisborne", "timaru",
        "tāmaki makaurau", "te whanganui-a-tara", "ōtautahi", "kirikiriroa"
    ]
    
    for location in locations:
        if location.lower() in input_text.lower():
            entities["location"] = location
            break
    
    # Extract service types
    service_types = {
        "gp": "general_practitioner",
        "doctor": "general_practitioner",
        "mental": "mental_health",
        "counseling": "mental_health",
        "therapy": "mental_health",
        "emergency housing": "emergency_housing",
        "homeless": "emergency_housing",
        "rent": "rental_assistance",
        "benefit": "financial_benefit",
        "payment": "financial_benefit",
        "food": "food_assistance",
        "dental": "dental_care",
        "teeth": "dental_care",
        "child": "child_services",
        "family": "family_services"
    }
    
    for keyword, service_type in service_types.items():
        if keyword.lower() in input_text.lower():
            entities["service_type"] = service_type
            break
    
    # Extract urgency
    if any(keyword in input_text.lower() for keyword in [
        "urgent", "emergency", "now", "today", "immediately"
    ]):
        entities["urgency"] = "high"
    
    return entities

def generate_response(intent, context):
    """
    Generate a response based on the detected intent and conversation context.
    
    Args:
        intent (str): Detected intent
        context (dict): Conversation context including language, cultural mode, etc.
    
    Returns:
        dict: Response containing text, options, and any other relevant data
    """
    language = context.get("language", ENGLISH)
    cultural_mode = context.get("cultural_mode", GENERAL)
    location = context.get("location", "")
    service_type = context.get("service_type", "")
    
    # Default responses
    default_response = {
        ENGLISH: {
            "text": "I'm here to help you find services. What kind of help are you looking for today?",
            "options": ["Health services", "Housing help", "Financial support", "Social services"]
        },
        MAORI: {
            "text": "Kei konei ahau hei āwhina i a koe. He aha te momo āwhina e hiahiatia ana e koe i tēnei rā?",
            "options": ["Ratonga hauora", "Āwhina whare", "Tautoko pūtea", "Ratonga pāpori"]
        }
    }
    
    # Intent-based responses
    if intent == "greeting":
        if language == MAORI:
            return {
                "text": "Tēnā koe! Ko Manaaki tōku ingoa. He aha tāu e hiahia ana i tēnei rā?",
                "options": ["Ratonga hauora", "Āwhina whare", "Tautoko pūtea", "Ratonga pāpori"]
            }
        else:  # ENGLISH
            if cultural_mode == MAORI_RESPONSIVE:
                return {
                    "text": "Kia ora! I'm Manaaki, here to help connect you with support services. What kind of help are you looking for today?",
                    "options": ["Health services", "Housing help", "Financial support", "Social services"]
                }
            else:  # GENERAL
                return {
                    "text": "Hello! I'm Manaaki, here to help connect you with support services. What kind of help are you looking for today?",
                    "options": ["Health services", "Housing help", "Financial support", "Social services"]
                }
    
    elif intent == "health_services":
        # If we have location, provide location-specific services
        if location:
            services = get_services_by_location(location, service_type)
            if services:
                if language == MAORI:
                    maori_location = get_maori_location_name(location)
                    services_text = "\n\n".join([f"{i+1}. {s.get('name_maori', s['name'])}" for i, s in enumerate(services[:3])])
                    return {
                        "text": f"Anei ētahi ratonga hauora i {maori_location}:\n\n{services_text}\n\nHe aha te momo ratonga hauora e hiahiatia ana e koe?",
                        "options": ["Tākuta whānau", "Hauora hinengaro", "Hauora niho", "Hauora wāhine"],
                        "services": services[:3]
                    }
                else:  # ENGLISH
                    services_text = "\n\n".join([f"{i+1}. {s['name']}" for i, s in enumerate(services[:3])])
                    return {
                        "text": f"Here are some health services in {location}:\n\n{services_text}\n\nWhat type of health service are you looking for?",
                        "options": ["GP/Family doctor", "Mental health", "Dental care", "Women's health"],
                        "services": services[:3]
                    }
        
        # If no location or no services found, ask for location
        if language == MAORI:
            return {
                "text": "E hiahia ana koe ki te rapu ratonga hauora? Tēnā, kōrero mai he aha tō wāhi noho kia āhei ai au ki te kimi i ngā ratonga tata ki a koe.",
                "options": ["Tāmaki Makaurau", "Te Whanganui-a-Tara", "Ōtautahi", "Kirikiriroa"]
            }
        else:  # ENGLISH
            return {
                "text": "I understand you're looking for health services. Could you tell me what area you live in so I can find services near you?",
                "options": ["Auckland", "Wellington", "Christchurch", "Hamilton"]
            }
    
    elif intent == "housing_assistance":
        # If we have service type, provide specific information
        if service_type == "emergency_housing":
            if language == MAORI:
                return {
                    "text": "Mēnā kei te rapu whare ohotata koe, anei ētahi ratonga ka taea te āwhina:\n\n1. Te Pūtea Āwhina Whare Ohotata (MSD)\n2. Te Tari Whare o Aotearoa\n3. Te Tūāpapa Kura Kāinga\n\nKei te hiahia koe kia tukuna atu he taipitopito anō mō tētahi o ēnei ratonga?",
                    "options": ["Āe", "Kāo", "Me pēhea au e tono ai?", "He ratonga anō?"]
                }
            else:  # ENGLISH
                return {
                    "text": "If you need emergency housing, these services can help:\n\n1. Emergency Housing Special Needs Grant (MSD)\n2. Housing New Zealand\n3. Ministry of Housing and Urban Development\n\nWould you like more details about any of these services?",
                    "options": ["Yes", "No", "How do I apply?", "Are there other options?"]
                }
        
        # General housing assistance
        if language == MAORI:
            return {
                "text": "E hiahia ana koe ki te rapu āwhina whare? He maha ngā momo āwhina e wātea ana. He aha te mea e hiahiatia ana e koe?",
                "options": ["Whare ohotata", "Āwhina rēti", "Whare pāpori", "Whakatikatika whare"]
            }
        else:  # ENGLISH
            return {
                "text": "I see you're looking for housing assistance. There are several types of housing support available. What specific help do you need?",
                "options": ["Emergency housing", "Rent assistance", "Social housing", "Home repairs"]
            }
    
    elif intent == "financial_support":
        if language == MAORI:
            return {
                "text": "E hiahia ana koe ki te rapu āwhina pūtea. He aha te momo āwhina e hiahiatia ana e koe?",
                "options": ["Penihana", "Tautoko whānau", "Utunga ohotata", "Āwhina nama"]
            }
        else:  # ENGLISH
            return {
                "text": "I understand you're looking for financial assistance. What type of financial support are you interested in?",
                "options": ["Benefits & payments", "Family support", "Emergency payment", "Debt assistance"]
            }
    
    elif intent == "social_support":
        if language == MAORI:
            return {
                "text": "E hiahia ana koe ki te rapu tautoko pāpori mō koe, mō tō whānau rānei?",
                "options": ["Mōku ake", "Mō tōku whānau", "Mō tētahi atu", "Ngā ratonga hapori"]
            }
        else:  # ENGLISH
            return {
                "text": "I see you're looking for social support. Is this support for yourself, your family, or someone else?",
                "options": ["For myself", "For my family", "For someone else", "Community services"]
            }
    
    elif intent == "mental_health":
        if language == MAORI:
            return {
                "text": "E hiahia ana koe ki te rapu ratonga hauora hinengaro. He maha ngā momo tautoko e wātea ana. He aha te mea e hiahiatia ana e koe?",
                "options": ["Kōrero tautoko", "Kaiāwhina ngaio", "Ratonga ohotata", "Rōpū tautoko"]
            }
        else:  # ENGLISH
            return {
                "text": "I understand you're looking for mental health support. There are several types of services available. What specific help do you need?",
                "options": ["Talk to someone now", "Professional help", "Crisis services", "Support groups"]
            }
    
    elif intent == "thanks":
        if language == MAORI:
            return {
                "text": "Kia ora mō tō whakamahi i a Manaaki Kaiārahi. He aha atu tāku e āwhina ai i a koe?",
                "options": ["Āe", "Kāo, kua ea"]
            }
        else:  # ENGLISH
            return {
                "text": "You're welcome! Is there anything else I can help you with today?",
                "options": ["Yes", "No, that's all"]
            }
    
    elif intent == "goodbye":
        if language == MAORI:
            return {
                "text": "Ka pai, e hoa. Mā te wā! Hoki mai anō mēnā ka hiahia āwhina anō koe.",
                "options": []
            }
        else:  # ENGLISH
            return {
                "text": "Thank you for using Manaaki Navigator. Feel free to come back anytime you need help!",
                "options": []
            }
    
    # Default to unknown intent response
    return default_response.get(language, default_response[ENGLISH])

def process_user_input(input_text, context):
    """
    Process user input and generate a response based on the conversation context.
    
    Args:
        input_text (str): User's input text
        context (dict): Current conversation context
    
    Returns:
        dict: Updated context and response
    """
    # Detect intent from user input
    intent = detect_intent(input_text, context.get("language", ENGLISH))
    
    # Extract entities from user input
    entities = extract_entities(input_text)
    
    # Update context with extracted entities
    updated_context = {**context, **entities}
    
    # Generate response based on intent and updated context
    response = generate_response(intent, updated_context)
    
    return {
        "context": updated_context,
        "response": response,
        "intent": intent,
        "entities": entities
    }
