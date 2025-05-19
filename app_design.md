# Manaaki Navigator: Streamlit Version Design

## Overview

This document outlines the design for the Streamlit version of the Manaaki Navigator MVP, focusing on creating a functional, accessible application that preserves the core features of the original React-based MVP while leveraging Streamlit's strengths.

## Core Features to Implement

1. **Conversational Interface**
   - Chat-like interaction with the AI assistant
   - Message history display
   - User input handling
   - Response generation based on user queries

2. **Service Matching & Needs Assessment**
   - Rule-based intent detection
   - Entity extraction (location, service type)
   - Service recommendation based on user needs
   - Display of relevant service information

3. **Bilingual Support**
   - Toggle between English and te reo Māori
   - Language-specific responses and UI elements
   - Translation of service information

4. **Cultural Adaptation**
   - Māori-responsive mode with appropriate styling
   - Culturally appropriate greetings and terminology
   - Visual indicators of cultural mode

## Streamlit Application Structure

```
manaaki-navigator-streamlit/
├── app.py                  # Main Streamlit application
├── pages/                  # Additional pages
│   ├── about.py            # About page
│   └── testing.py          # Scenario testing page
├── services/               # Backend services
│   ├── conversation.py     # Conversation handling logic
│   ├── service_matcher.py  # Service matching logic
│   └── mock_data.py        # Mock service directory data
├── utils/                  # Utility functions
│   ├── language.py         # Language handling utilities
│   └── styling.py          # Custom styling functions
├── assets/                 # Static assets
│   └── logo.png            # Application logo
└── requirements.txt        # Dependencies
```

## User Interface Design

### Main Chat Interface

```
+-----------------------------------------------+
| [Language Toggle] [Cultural Mode Toggle]      |
+-----------------------------------------------+
| Manaaki Navigator                             |
+-----------------------------------------------+
|                                               |
| [Bot]: Kia ora! I'm Manaaki, here to help...  |
|                                               |
| [User]: I need help with housing              |
|                                               |
| [Bot]: I understand you're looking for        |
|        housing assistance. What specific      |
|        help do you need?                      |
|                                               |
| [Option Buttons]                              |
| [Emergency housing] [Rent assistance] [...]   |
|                                               |
+-----------------------------------------------+
| Your message:                                 |
| [                                      ] [>]  |
+-----------------------------------------------+
```

### About Page

```
+-----------------------------------------------+
| [Language Toggle] [Cultural Mode Toggle]      |
+-----------------------------------------------+
| About Manaaki Navigator                       |
+-----------------------------------------------+
|                                               |
| What is Manaaki Navigator?                    |
| ...                                           |
|                                               |
| How does it work?                             |
| ...                                           |
|                                               |
| What does the name Manaaki mean?              |
| ...                                           |
|                                               |
+-----------------------------------------------+
```

### Testing Page

```
+-----------------------------------------------+
| Scenario Testing                              |
+-----------------------------------------------+
|                                               |
| Select a Test Scenario:                       |
| [Dropdown Menu]                               |
|                                               |
| Current Step: 1/4                             |
| Input: "I need a doctor"                      |
| Expected: Contains "health services"          |
|                                               |
| [Pass] [Fail] [Reset]                         |
|                                               |
| Test Results:                                 |
| Step 1: Passed                                |
| ...                                           |
|                                               |
+-----------------------------------------------+
```

## Technical Implementation Approach

### Conversation Management

1. **Session State**
   - Use Streamlit's session state to maintain conversation history
   - Store user preferences (language, cultural mode) in session state
   - Preserve context between interactions

2. **Message Display**
   - Custom message containers with different styling for user and bot
   - Typing indicator animation for bot responses
   - Scrollable message history container

3. **Input Handling**
   - Text input for user messages
   - Button options for quick replies
   - Input validation and processing

### Service Matching Logic

1. **Intent Detection**
   - Simple keyword-based intent recognition
   - Pattern matching for common queries
   - Context-aware response generation

2. **Entity Extraction**
   - Location identification from user input
   - Service type classification
   - Urgency detection

3. **Service Recommendation**
   - Filtering mock service directory based on extracted entities
   - Ranking services by relevance
   - Formatting service information for display

### Cultural Adaptation

1. **Language Switching**
   - Dictionary-based translation for UI elements
   - Predefined responses in both languages
   - Language-specific formatting and terminology

2. **Cultural Mode**
   - Custom CSS for different cultural modes
   - Adapted greeting patterns and conversation flows
   - Visual indicators of current cultural mode

## Streamlit-Specific Optimizations

1. **Component Caching**
   - Use `@st.cache_data` for service data and responses
   - Optimize performance for repeated queries

2. **Responsive Layout**
   - Utilize Streamlit columns for adaptive layouts
   - Mobile-friendly design considerations

3. **Custom Styling**
   - CSS customization for chat bubbles and buttons
   - Theme consistency with original MVP

4. **State Management**
   - Efficient use of session state to maintain conversation context
   - Clear separation of UI and logic components

## Deployment Approach

1. **Local Development**
   - Develop and test locally using `streamlit run app.py`
   - Ensure all dependencies are in requirements.txt

2. **Streamlit Cloud Deployment**
   - Direct deployment to Streamlit Cloud without GitHub
   - Package all necessary files for upload

3. **Alternative Deployment Options**
   - Instructions for deploying to Heroku
   - Instructions for deploying to Render or Railway

## Limitations and Considerations

1. **Streamlit Constraints**
   - Limited control over UI compared to React
   - Page refreshes may affect user experience
   - Session management differences

2. **Feature Prioritization**
   - Focus on core conversational experience
   - Simplified SMS simulation if needed
   - Maintain essential cultural adaptation features

3. **Performance Considerations**
   - Optimize for Streamlit's execution model
   - Minimize unnecessary recomputation

## Next Steps

1. Implement basic Streamlit application structure
2. Develop conversation management system
3. Integrate mock service data and matching logic
4. Add language and cultural adaptation features
5. Implement testing framework
6. Deploy and document the application
