"""
Utility functions for language and cultural adaptation in the Manaaki Navigator Streamlit MVP.
"""

# Define language constants
ENGLISH = "english"
MAORI = "maori"

# Define cultural mode constants
GENERAL = "general"
MAORI_RESPONSIVE = "maori-responsive"

# UI text translations
ui_text = {
    "app_title": {
        ENGLISH: "Manaaki Navigator",
        MAORI: "Manaaki Kaiārahi"
    },
    "welcome_title": {
        ENGLISH: "Welcome to Manaaki Navigator",
        MAORI: "Nau Mai ki Manaaki Kaiārahi"
    },
    "language_selector": {
        ENGLISH: "Language",
        MAORI: "Reo"
    },
    "cultural_mode_selector": {
        ENGLISH: "Cultural Mode",
        MAORI: "Ahurea"
    },
    "general_mode": {
        ENGLISH: "General",
        MAORI: "Ahurea Whānui"
    },
    "maori_mode": {
        ENGLISH: "Māori-Responsive",
        MAORI: "Ahurea Māori"
    },
    "chat_placeholder": {
        ENGLISH: "Type your message here...",
        MAORI: "Tāuru tō karere ki konei..."
    },
    "send_button": {
        ENGLISH: "Send",
        MAORI: "Tukuna"
    },
    "about_title": {
        ENGLISH: "About Manaaki Navigator",
        MAORI: "Mō Manaaki Kaiārahi"
    },
    "testing_title": {
        ENGLISH: "Scenario Testing",
        MAORI: "Whakamātautau Kōrero"
    },
    "chat_title": {
        ENGLISH: "Chat with Manaaki",
        MAORI: "Kōrero ki a Manaaki"
    },
    "clear_chat": {
        ENGLISH: "Clear Chat",
        MAORI: "Ūkui Kōrero"
    },
    "start_over": {
        ENGLISH: "Start Over",
        MAORI: "Tīmata Anō"
    }
}

def get_ui_text(key, language=ENGLISH):
    """
    Get UI text in the specified language.
    
    Args:
        key (str): Text key
        language (str): Language code (english or maori)
    
    Returns:
        str: Translated text
    """
    if key in ui_text:
        return ui_text[key].get(language, ui_text[key][ENGLISH])
    return key

def get_css_for_cultural_mode(cultural_mode=GENERAL):
    """
    Get CSS styling based on cultural mode.
    
    Args:
        cultural_mode (str): Cultural mode (general or maori-responsive)
    
    Returns:
        str: CSS styling
    """
    if cultural_mode == MAORI_RESPONSIVE:
        return """
        .stApp {
            background-color: #f0f7f4;
        }
        .main-header {
            background-color: #2c7d59;
            color: white;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
        }
        .chat-message-bot {
            background-color: #e6f2ea;
            border-left: 5px solid #2c7d59;
        }
        .chat-message-user {
            background-color: #e3f2fd;
            border-right: 5px solid #2196f3;
        }
        .stButton>button {
            background-color: #2c7d59;
            color: white;
        }
        .option-button {
            background-color: #e6f2ea;
            border: 1px solid #2c7d59;
            color: #2c7d59;
        }
        """
    else:  # GENERAL
        return """
        .stApp {
            background-color: #f8f9fa;
        }
        .main-header {
            background-color: #1976d2;
            color: white;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
        }
        .chat-message-bot {
            background-color: #f1f1f1;
            border-left: 5px solid #1976d2;
        }
        .chat-message-user {
            background-color: #e3f2fd;
            border-right: 5px solid #2196f3;
        }
        .stButton>button {
            background-color: #1976d2;
            color: white;
        }
        .option-button {
            background-color: #f1f1f1;
            border: 1px solid #1976d2;
            color: #1976d2;
        }
        """

def get_common_css():
    """
    Get common CSS styling for the application.
    
    Returns:
        str: CSS styling
    """
    return """
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        position: relative;
        width: 80%;
    }
    .chat-message-bot {
        margin-right: auto;
    }
    .chat-message-user {
        margin-left: auto;
        text-align: right;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    .option-button {
        margin: 0.25rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        cursor: pointer;
        text-align: center;
        transition: all 0.2s;
    }
    .option-button:hover {
        opacity: 0.8;
    }
    .service-card {
        border: 1px solid #ddd;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .service-card h4 {
        margin-top: 0;
    }
    .service-card-maori {
        border-color: #2c7d59;
    }
    .service-card-general {
        border-color: #1976d2;
    }
    """
