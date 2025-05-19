# Manaaki Navigator: Streamlit MVP Documentation

## Overview

Manaaki Navigator is an AI-powered service that helps people in New Zealand find and access health and social services. This Streamlit MVP demonstrates the core functionality with a focus on cultural responsiveness and accessibility for deprived populations.

## Features

### 1. Conversational Interface
- Natural language chat interface for asking about services
- Quick-reply buttons for common options
- Context-aware responses based on previous conversation
- Service recommendations based on user needs

### 2. Bilingual Support
- Full support for both English and te reo Māori
- Language toggle in the sidebar
- All UI elements and responses available in both languages
- Culturally appropriate greetings and terminology

### 3. Cultural Adaptation
- Māori-responsive mode with appropriate styling and language
- Cultural context awareness in responses
- Visual indicators of cultural mode (colors, styling)
- Culturally appropriate service information

### 4. Service Matching
- Location-based service recommendations
- Service type filtering (health, housing, financial, social)
- Display of relevant service details
- Mock data covering major NZ cities

### 5. Multi-Page Structure
- Main chat interface for service navigation
- About page with information about the application
- Testing page for scenario validation

## Limitations

### 1. Data Limitations
- Uses mock data rather than a live service directory
- Limited geographic coverage (major cities only)
- Simplified service information
- No real-time availability information

### 2. Functionality Limitations
- No user authentication or personalization
- No integration with external systems
- Limited conversation paths
- No ability to book appointments or make referrals

### 3. Technical Limitations
- Simple rule-based conversation logic (not true NLP)
- No persistent data storage between sessions
- Limited error handling for edge cases
- Streamlit-specific UI constraints

## Usage Instructions

### Accessing the Application
- The application is available at: https://8501-idtlmhxkg31m55ttxuump-4365083d.manus.computer
- No login required - simply open the link in any modern web browser
- Works on both desktop and mobile devices

### Using the Chat Interface
1. **Start a conversation**: The chat will begin with a greeting
2. **Tell Manaaki what you need**: Type your request or click a suggested option
3. **Provide additional information**: Answer follow-up questions about location or specific needs
4. **View service recommendations**: Review the suggested services based on your needs
5. **Ask for more details**: Continue the conversation to get more information

### Language and Cultural Settings
- Use the sidebar to switch between English and te reo Māori
- Select your preferred cultural mode (General or Māori-Responsive)
- Settings can be changed at any time during the conversation

### Testing Scenarios
1. Navigate to the Testing page via the sidebar
2. Select a test scenario from the available options
3. Follow the step-by-step instructions to validate functionality
4. Mark each step as Pass or Fail based on the results
5. Review the overall test results at the end

## Technical Implementation

The Manaaki Navigator Streamlit MVP is built using:
- **Streamlit**: For the web application framework
- **Python**: For backend logic and conversation handling
- **CSS**: For styling and cultural adaptation
- **Session State**: For maintaining conversation context

The application structure follows a modular design:
- `app.py`: Main application and chat interface
- `pages/`: Additional pages (About, Testing)
- `services/`: Backend logic (conversation, mock data)
- `utils/`: Utility functions (language, styling)

## Future Development Opportunities

1. **Data Integration**: Connect to real service directories and databases
2. **Advanced NLP**: Implement true natural language understanding
3. **User Accounts**: Add personalization and saved preferences
4. **Additional Languages**: Expand to support Pacific languages
5. **Mobile App**: Develop a dedicated mobile application
6. **Offline Support**: Enable functionality without internet connection
7. **Integration APIs**: Connect with healthcare and social service systems

## Support and Feedback

This is an MVP demonstration. For questions, issues, or feedback, please contact the development team.

---

*Developed with aroha for the communities of Aotearoa New Zealand.*
