"""
Main Streamlit application for the Manaaki Navigator MVP.
This file contains the main chat interface and application logic.
"""

import streamlit as st
from services.conversation import process_user_input
from services.mock_data import get_services_by_location
from utils.language import (
    get_ui_text, get_css_for_cultural_mode, get_common_css,
    ENGLISH, MAORI, GENERAL, MAORI_RESPONSIVE
)

# Set page configuration
st.set_page_config(
    page_title="Manaaki Navigator",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = {
        "language": ENGLISH,
        "cultural_mode": GENERAL
    }

if "show_options" not in st.session_state:
    st.session_state.show_options = []

# Apply CSS styling
def apply_custom_css():
    """Apply custom CSS styling based on cultural mode"""
    cultural_mode = st.session_state.context.get("cultural_mode", GENERAL)
    st.markdown(f"""
        <style>
            {get_common_css()}
            {get_css_for_cultural_mode(cultural_mode)}
        </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# Sidebar for settings
with st.sidebar:
    st.title(get_ui_text("app_title", st.session_state.context["language"]))
    
    # Language selector
    language_label = get_ui_text("language_selector", st.session_state.context["language"])
    language_options = {
        ENGLISH: "English",
        MAORI: "Te Reo Māori"
    }
    
    selected_language = st.selectbox(
        language_label,
        options=list(language_options.keys()),
        format_func=lambda x: language_options[x],
        index=0 if st.session_state.context["language"] == ENGLISH else 1
    )
    
    if selected_language != st.session_state.context["language"]:
        st.session_state.context["language"] = selected_language
        st.rerun()
    
    # Cultural mode selector
    cultural_label = get_ui_text("cultural_mode_selector", st.session_state.context["language"])
    cultural_options = {
        GENERAL: get_ui_text("general_mode", st.session_state.context["language"]),
        MAORI_RESPONSIVE: get_ui_text("maori_mode", st.session_state.context["language"])
    }
    
    selected_mode = st.selectbox(
        cultural_label,
        options=list(cultural_options.keys()),
        format_func=lambda x: cultural_options[x],
        index=0 if st.session_state.context["cultural_mode"] == GENERAL else 1
    )
    
    if selected_mode != st.session_state.context["cultural_mode"]:
        st.session_state.context["cultural_mode"] = selected_mode
        st.rerun()
    
    # Clear chat button
    if st.button(get_ui_text("clear_chat", st.session_state.context["language"])):
        st.session_state.messages = []
        st.session_state.show_options = []
        st.session_state.context = {
            "language": st.session_state.context["language"],
            "cultural_mode": st.session_state.context["cultural_mode"]
        }
        st.rerun()

# Main content
st.markdown(f"""
    <div class="main-header">
        <h1>{get_ui_text("chat_title", st.session_state.context["language"])}</h1>
    </div>
""", unsafe_allow_html=True)

# Display initial greeting if no messages
if not st.session_state.messages:
    # Process initial greeting
    greeting_text = "Hello" if st.session_state.context["language"] == ENGLISH else "Tēnā koe"
    result = process_user_input(greeting_text, st.session_state.context)
    
    # Update context
    st.session_state.context = result["context"]
    
    # Add bot message to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": result["response"]["text"]
    })
    
    # Set options for quick replies
    st.session_state.show_options = result["response"].get("options", [])

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
            <div class="chat-message chat-message-user">
                <div>{message["content"]}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-message chat-message-bot">
                <div>{message["content"].replace('\n', '<br>')}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Display services if available in the message
        if "services" in message:
            st.subheader("Services")
            cols = st.columns(len(message["services"]))
            for i, service in enumerate(message["services"]):
                with cols[i]:
                    cultural_class = "service-card-maori" if st.session_state.context["cultural_mode"] == MAORI_RESPONSIVE else "service-card-general"
                    st.markdown(f"""
                        <div class="service-card {cultural_class}">
                            <h4>{service["name"]}</h4>
                            <p>{service["description"]}</p>
                            <p><strong>Address:</strong> {service["address"]}</p>
                            <p><strong>Phone:</strong> {service["phone"]}</p>
                            <p><strong>Hours:</strong> {service["hours"]}</p>
                        </div>
                    """, unsafe_allow_html=True)

# Display option buttons if available
if st.session_state.show_options:
    st.markdown("<div style='margin-top: 1rem;'>", unsafe_allow_html=True)
    cols = st.columns(min(len(st.session_state.show_options), 2))
    for i, option in enumerate(st.session_state.show_options):
        with cols[i % 2]:
            if st.button(option, key=f"option_{i}"):
                # Add user message to chat history
                st.session_state.messages.append({
                    "role": "user",
                    "content": option
                })
                
                # Process user input
                result = process_user_input(option, st.session_state.context)
                
                # Update context
                st.session_state.context = result["context"]
                
                # Add bot message to chat history
                response = result["response"]
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response["text"],
                    "services": response.get("services", [])
                })
                
                # Update options for quick replies
                st.session_state.show_options = response.get("options", [])
                
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# User input
with st.form(key="user_input_form", clear_on_submit=True):
    user_input = st.text_input(
        label="Your message",
        placeholder=get_ui_text("chat_placeholder", st.session_state.context["language"]),
        label_visibility="collapsed"
    )
    
    submit_button = st.form_submit_button(
        label=get_ui_text("send_button", st.session_state.context["language"])
    )
    
    if submit_button and user_input:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Process user input
        result = process_user_input(user_input, st.session_state.context)
        
        # Update context
        st.session_state.context = result["context"]
        
        # Add bot message to chat history
        response = result["response"]
        st.session_state.messages.append({
            "role": "assistant",
            "content": response["text"],
            "services": response.get("services", [])
        })
        
        # Update options for quick replies
        st.session_state.show_options = response.get("options", [])
        
        st.rerun()
