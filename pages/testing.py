"""
Testing page for the Manaaki Navigator Streamlit MVP.
This page provides a scenario testing framework to validate the application functionality.
"""

import streamlit as st
from services.conversation import process_user_input
from utils.language import (
    get_ui_text, get_css_for_cultural_mode, get_common_css,
    ENGLISH, MAORI, GENERAL, MAORI_RESPONSIVE
)

# Define test scenarios
test_scenarios = [
    {
        "id": 1,
        "name": "Health Services Scenario - English",
        "description": "User seeking GP services in Auckland",
        "language": ENGLISH,
        "cultural_mode": GENERAL,
        "steps": [
            {"input": "Hello", "expected_contains": "help connect you with support services"},
            {"input": "I need to find a doctor", "expected_contains": "health services"},
            {"input": "Auckland", "expected_contains": "Auckland"},
            {"input": "GP/Family doctor", "expected_contains": "Community Services Card"}
        ]
    },
    {
        "id": 2,
        "name": "Housing Assistance Scenario - English",
        "description": "User seeking emergency housing",
        "language": ENGLISH,
        "cultural_mode": GENERAL,
        "steps": [
            {"input": "I need housing help", "expected_contains": "housing assistance"},
            {"input": "Emergency housing", "expected_contains": "Emergency Housing Special Needs Grant"},
            {"input": "How do I apply?", "expected_contains": "apply"}
        ]
    },
    {
        "id": 3,
        "name": "Māori Cultural Adaptation Scenario",
        "description": "User interacting in te reo Māori",
        "language": MAORI,
        "cultural_mode": MAORI_RESPONSIVE,
        "steps": [
            {"input": "Tēnā koe", "expected_contains": "Tēnā koe"},
            {"input": "He āwhina hauora", "expected_contains": "ratonga hauora"},
            {"input": "Tāmaki Makaurau", "expected_contains": "Tāmaki Makaurau"}
        ]
    },
    {
        "id": 4,
        "name": "Financial Support Scenario - English with Māori Responsive",
        "description": "User seeking financial assistance with cultural adaptation",
        "language": ENGLISH,
        "cultural_mode": MAORI_RESPONSIVE,
        "steps": [
            {"input": "Kia ora", "expected_contains": "Kia ora"},
            {"input": "I need financial help", "expected_contains": "financial assistance"},
            {"input": "Benefits & payments", "expected_contains": "Work and Income"}
        ]
    },
    {
        "id": 5,
        "name": "Mental Health Support Scenario",
        "description": "User seeking mental health support",
        "language": ENGLISH,
        "cultural_mode": GENERAL,
        "steps": [
            {"input": "I'm feeling anxious", "expected_contains": "mental health"},
            {"input": "Talk to someone now", "expected_contains": "1737"}
        ]
    }
]

# Apply CSS styling
def apply_custom_css():
    """Apply custom CSS styling based on cultural mode"""
    cultural_mode = st.session_state.context.get("cultural_mode", GENERAL)
    st.markdown(f"""
        <style>
            {get_common_css()}
            {get_css_for_cultural_mode(cultural_mode)}
            .test-card {{
                border: 1px solid #ddd;
                border-radius: 0.5rem;
                padding: 1rem;
                margin-bottom: 1rem;
            }}
            .test-step {{
                padding: 0.5rem;
                margin-bottom: 0.5rem;
                border-radius: 0.25rem;
            }}
            .test-step-current {{
                background-color: #e3f2fd;
                border-left: 3px solid #1976d2;
            }}
            .test-step-passed {{
                background-color: #e8f5e9;
                border-left: 3px solid #4caf50;
            }}
            .test-step-failed {{
                background-color: #ffebee;
                border-left: 3px solid #f44336;
            }}
            .test-results {{
                margin-top: 1rem;
                padding: 1rem;
                border-radius: 0.5rem;
            }}
            .test-results-passed {{
                background-color: #e8f5e9;
            }}
            .test-results-failed {{
                background-color: #ffebee;
            }}
        </style>
    """, unsafe_allow_html=True)

# Initialize session state for testing
if "test_scenario" not in st.session_state:
    st.session_state.test_scenario = None

if "test_step" not in st.session_state:
    st.session_state.test_step = 0

if "test_results" not in st.session_state:
    st.session_state.test_results = []

if "test_complete" not in st.session_state:
    st.session_state.test_complete = False

if "test_messages" not in st.session_state:
    st.session_state.test_messages = []

# Page content
def show_testing_page():
    # Apply styling
    apply_custom_css()
    
    # Page header
    st.markdown(f"""
        <div class="main-header">
            <h1>{get_ui_text("testing_title", st.session_state.context.get("language", ENGLISH))}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Scenario selection or test execution
    if not st.session_state.test_scenario:
        st.subheader("Select a Test Scenario")
        
        for scenario in test_scenarios:
            st.markdown(f"""
                <div class="test-card">
                    <h3>{scenario["name"]}</h3>
                    <p>{scenario["description"]}</p>
                    <p><strong>Language:</strong> {scenario["language"].capitalize()} | 
                    <strong>Cultural Mode:</strong> {scenario["cultural_mode"].capitalize()}</p>
                    <p><strong>Steps:</strong> {len(scenario["steps"])}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Start Scenario #{scenario['id']}", key=f"start_{scenario['id']}"):
                # Set up the test environment
                st.session_state.test_scenario = scenario
                st.session_state.test_step = 0
                st.session_state.test_results = []
                st.session_state.test_complete = False
                st.session_state.test_messages = []
                
                # Update context for language and cultural mode
                st.session_state.context["language"] = scenario["language"]
                st.session_state.context["cultural_mode"] = scenario["cultural_mode"]
                
                st.rerun()
    
    else:
        # Display current test scenario
        scenario = st.session_state.test_scenario
        st.subheader(f"Testing: {scenario['name']}")
        st.write(scenario["description"])
        
        # Display test progress
        progress = st.progress(0)
        if not st.session_state.test_complete:
            progress.progress((st.session_state.test_step) / len(scenario["steps"]))
        else:
            progress.progress(1.0)
        
        # Display current step or results
        if not st.session_state.test_complete:
            current_step = scenario["steps"][st.session_state.test_step]
            
            st.markdown(f"""
                <div class="test-step test-step-current">
                    <p><strong>Step {st.session_state.test_step + 1}/{len(scenario["steps"])}</strong></p>
                    <p><strong>Input:</strong> "{current_step["input"]}"</p>
                    <p><strong>Expected response should contain:</strong> "{current_step["expected_contains"]}"</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Display chat interface for testing
            st.subheader("Test Chat")
            
            # Display previous messages
            for message in st.session_state.test_messages:
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
            
            # Process current step
            if st.button("Process Current Step"):
                # Add user message to chat history
                st.session_state.test_messages.append({
                    "role": "user",
                    "content": current_step["input"]
                })
                
                # Process user input
                result = process_user_input(current_step["input"], st.session_state.context)
                
                # Update context
                st.session_state.context = result["context"]
                
                # Add bot message to chat history
                response = result["response"]
                st.session_state.test_messages.append({
                    "role": "assistant",
                    "content": response["text"]
                })
                
                st.rerun()
            
            # Test result buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Pass"):
                    st.session_state.test_results.append({
                        "step": st.session_state.test_step,
                        "passed": True
                    })
                    
                    if st.session_state.test_step + 1 < len(scenario["steps"]):
                        st.session_state.test_step += 1
                    else:
                        st.session_state.test_complete = True
                    
                    st.rerun()
            
            with col2:
                if st.button("Fail"):
                    st.session_state.test_results.append({
                        "step": st.session_state.test_step,
                        "passed": False
                    })
                    
                    if st.session_state.test_step + 1 < len(scenario["steps"]):
                        st.session_state.test_step += 1
                    else:
                        st.session_state.test_complete = True
                    
                    st.rerun()
            
            with col3:
                if st.button("Cancel Test"):
                    st.session_state.test_scenario = None
                    st.session_state.test_step = 0
                    st.session_state.test_results = []
                    st.session_state.test_complete = False
                    st.session_state.test_messages = []
                    
                    st.rerun()
        
        else:
            # Display test results
            all_passed = all(result["passed"] for result in st.session_state.test_results)
            result_class = "test-results-passed" if all_passed else "test-results-failed"
            
            st.markdown(f"""
                <div class="test-results {result_class}">
                    <h3>Test Complete</h3>
                    <p>{"All steps passed successfully!" if all_passed else "Some steps failed. Review the results below."}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Display detailed results
            st.subheader("Test Results")
            for i, result in enumerate(st.session_state.test_results):
                step = scenario["steps"][result["step"]]
                step_class = "test-step-passed" if result["passed"] else "test-step-failed"
                
                st.markdown(f"""
                    <div class="test-step {step_class}">
                        <p><strong>Step {result["step"] + 1}:</strong> {result["passed"] and "Passed" or "Failed"}</p>
                        <p><strong>Input:</strong> "{step["input"]}"</p>
                        <p><strong>Expected to contain:</strong> "{step["expected_contains"]}"</p>
                    </div>
                """, unsafe_allow_html=True)
            
            if st.button("Test Another Scenario"):
                st.session_state.test_scenario = None
                st.session_state.test_step = 0
                st.session_state.test_results = []
                st.session_state.test_complete = False
                st.session_state.test_messages = []
                
                st.rerun()

# Run the page
show_testing_page()
