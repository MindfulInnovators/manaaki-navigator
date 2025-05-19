"""
About page for the Manaaki Navigator Streamlit MVP.
This page provides information about the application and its purpose.
"""

import streamlit as st
from utils.language import (
    get_ui_text, get_css_for_cultural_mode, get_common_css,
    ENGLISH, MAORI, GENERAL, MAORI_RESPONSIVE
)

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

# Page content
def show_about_page():
    # Apply styling
    apply_custom_css()
    
    # Get language and cultural mode from session state
    language = st.session_state.context.get("language", ENGLISH)
    cultural_mode = st.session_state.context.get("cultural_mode", GENERAL)
    
    # Page header
    st.markdown(f"""
        <div class="main-header">
            <h1>{get_ui_text("about_title", language)}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # About content in English
    if language == ENGLISH:
        st.markdown("""
        ## What is Manaaki Navigator?
        
        Manaaki Navigator is an AI-powered service that helps people in New Zealand find and access health and social services. The name "Manaaki" comes from the Māori concept of showing respect, hospitality, and care for others.
        
        Our goal is to make it easier for everyone, especially those facing barriers or challenges, to connect with the support they need. We focus on providing culturally responsive information and guidance that respects the diversity of Aotearoa New Zealand.
        
        ## How does it work?
        
        Simply chat with Manaaki and tell us what kind of help you're looking for. You can ask about:
        
        - Health services (doctors, mental health, dental care)
        - Housing assistance (emergency housing, rental support)
        - Financial support (benefits, emergency payments)
        - Social services (family support, community resources)
        
        Manaaki will ask questions to understand your needs and then suggest relevant services in your area.
        
        ## Cultural Responsiveness
        
        Manaaki Navigator is designed with cultural responsiveness at its core. You can:
        
        - Switch between English and te reo Māori
        - Select the Māori-responsive mode for culturally appropriate interactions
        - Access information about services that specialize in culturally responsive care
        
        ## About this MVP
        
        This is a Minimum Viable Product (MVP) version of Manaaki Navigator. It demonstrates the core functionality but has some limitations:
        
        - It uses simulated data rather than a live service directory
        - It has limited conversation paths and service information
        - It doesn't yet connect directly to service providers
        
        We're continuously improving Manaaki Navigator based on user feedback and community needs.
        """)
    
    # About content in Māori
    else:
        st.markdown("""
        ## He aha te Manaaki Kaiārahi?
        
        Ko Manaaki Kaiārahi he ratonga atamai hangarau e āwhina ana i ngā tāngata o Aotearoa ki te rapu me te uru atu ki ngā ratonga hauora me ngā ratonga pāpori. Ko te ingoa "Manaaki" e hāngai ana ki te tikanga Māori o te whakaatu i te manaaki, te manaakitanga, me te tiaki i ētahi atu.
        
        Ko tā mātou whāinga he whakamāmā ake mā te katoa, otirā mō rātou e aro ana ki ngā āhuatanga uaua, ki te tūhono ki te tautoko e hiahiatia ana. E arotahi ana mātou ki te whakarato mōhiohio me te ārahi e hāngai ana ki te ahurea e whakaute ana i te kanorau o Aotearoa.
        
        ## Me pēhea te mahi?
        
        Kōrero noa ki a Manaaki, ā, kōrero mai he aha te momo āwhina e hiahia ana koe. Ka taea e koe te pātai mō:
        
        - Ngā ratonga hauora (ngā tākuta, te hauora hinengaro, te tiaki niho)
        - Āwhina whare (whare ohotata, tautoko rēti)
        - Tautoko pūtea (penihana, utunga ohotata)
        - Ngā ratonga pāpori (tautoko whānau, rauemi hapori)
        
        Ka pātai a Manaaki i ngā pātai hei mārama ki ō hiahia, kātahi ka taunaki i ngā ratonga e hāngai ana ki tō rohe.
        
        ## Urupare ā-Ahurea
        
        Kua hangaia a Manaaki Kaiārahi me te urupare ā-ahurea i tōna iho. Ka taea e koe:
        
        - Te huri i waenga i te reo Pākehā me te reo Māori
        - Te kōwhiri i te aratau urupare Māori mō ngā taunekeneke e tika ana ki te ahurea
        - Te uru atu ki ngā mōhiohio mō ngā ratonga e whakarato ana i te tiaki e hāngai ana ki te ahurea
        
        ## Mō tēnei MVP
        
        He putanga Hua Ora Iti (MVP) tēnei o Manaaki Kaiārahi. E whakaatu ana i te mahinga matua engari he āhuatanga whāiti:
        
        - Ka whakamahi i ngā raraunga whakatauira, kaua i te whaiaronga ratonga ora
        - He ara kōrero me ngā mōhiohio ratonga whāiti
        - Kāore anō kia tūhono tōtika ki ngā kaiwhakarato ratonga
        
        E whakapai tonu ana mātou i a Manaaki Kaiārahi i runga i ngā urupare kaiwhakamahi me ngā hiahia hapori.
        """)
    
    # Footer with cultural adaptation
    if cultural_mode == MAORI_RESPONSIVE:
        st.markdown("""
        ---
        
        *Manaaki tangata, manaaki whenua, manaaki taiao.*  
        *Care for the people, care for the land, care for the environment.*
        """)
    else:
        st.markdown("""
        ---
        
        *Developed with aroha for the communities of Aotearoa New Zealand.*
        """)

# Run the page
show_about_page()
