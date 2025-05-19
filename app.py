import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="SafeSip",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 5rem !important;
        font-weight: 700 !important;
        color: #0D47A1 !important;
        margin-bottom: 1rem !important;
    }
            
    .sub-header {
        font-size: 2.5rem !important;
        font-weight: 500 !important;
        color: #1976D2 !important;
        margin-bottom: 1.5rem !important;
    }
            
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
            
    .parameter-name {
        font-weight: 600;
        color: #0277BD;
    }
            
    .parameter-desc {
        color: #333333;
    }
            
    .black-text, 
    h3.black-text, 
    p.black-text {
        color: #000000 !important;
    }
            
    .stApp {
        background-color: #f0f8ff;
    }
    
    .centered-button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    
    hr {
        height: 2px !important;
        border: none !important;
        color: #1E88E5 !important;
        background-color: #1E88E5 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    div[data-testid="stButton"]:not([data-testid="stSidebarContent"] div[data-testid="stButton"]) > button {
        background-color: #1E88E5;
        color: white !important;
        padding: 1rem 2rem;
        font-size: 1.4rem;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        text-align: center;
        display: inline-block;
        margin: 10px 0;
    }
            
    [data-testid="stSidebarContent"] div[data-testid="stButton"] > button:focus {
        outline: none !important;
        border-color: #4A90E2 !important;
        color: #1E88E5;
    }
            
    [data-testid="stSidebar"] {
        background-color: white;
    }

    [data-testid="stSidebarContent"] div[data-testid="stButton"] > button {
        display: block;
        width: 100%;
        text-align: left;
        font-size: 1.1rem;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    }
            
    div[data-testid="stButton"] > button[kind="secondary"] {
        background-color: transparent;
        color: #1E88E5;
        border: 2px solid #1E88E5;
        padding: 0.75rem 1.5rem;
        font-size: 1.2rem;
    }
    
    div[data-testid="stButton"] > button[kind="secondary"]:hover {
        background-color: rgba(30, 136, 229, 0.1);
        color: #0D47A1 !important;
    }
            
    div[data-testid="stSidebarNav"] {
        display: none;
    }
            
    section[data-testid="stSidebar"] > div > div:first-child > div > button {
        background-color: #4A90E2;
        color: white;
        border-radius: 4px;
    }
    
    section[data-testid="stSidebar"] > div > div:first-child > div > button svg {
        color: white; 
    }
    
    section[data-testid="stSidebar"] > div > div:first-child > div > button:hover {
        background-color: #0D47A1;
    }
    .stApp > header{
        background-color: #1E88E5;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    if st.button("🏠 Home", key="sidebar_home_button", use_container_width=True):
        st.session_state.current_page = "app.py"
        st.switch_page("app.py")

    if st.button("📊 Analyze", key="sidebar_analyze_button", use_container_width=True):
        st.session_state.current_page = "analyze.py"
        st.switch_page("pages/analyze.py")

    if st.button("ℹ️ About", key="sidebar_about_button", use_container_width=True):
        st.switch_page("pages/about.py")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1976D2;'> App Information </h3>", unsafe_allow_html=True) # Changed from "About" to avoid confusion with nav item
    st.markdown("<p style='color: #1976D2;'> Our water quality analysis tool helps you determine if your water is safe to drink based on various chemical and physical parameters.</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #1976D2;'> Contact </h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1976D2;'>For more information, contact us at: safesip@gmail.com </p>", unsafe_allow_html=True)

# Main content
st.markdown('<p class="main-header">SafeSip</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Is your water safe to drink? Find out with our advanced AI tools.</p>', unsafe_allow_html=True)

# Hero section with columns
col1_hero, col2_hero = st.columns([3, 2])

with col1_hero:
    st.markdown("""
    <h3 class="black-text">Our Mission</h3>

    <p class="black-text">We provide a reliable and easy-to-use tool that analyzes water quality parameters to determine
    if your water is safe for consumption. By inputting key water quality metrics, you can quickly
    assess the potability of your water source.</p>

    """, unsafe_allow_html=True)

    # Using st.button for functionality with secondary style
    if st.button("Learn More About Water Quality", key="learn_more_button", type="secondary"):
        st.switch_page("pages/about.py")


with col2_hero:
    try:
        image = Image.open("ClearWater.jpg")
        st.image(image, caption="Clean, safe drinking water is essential for health.")
    except FileNotFoundError:
        st.warning("Water.jpg not found. Please ensure it's in the project directory.")
        st.markdown("<div style='height:200px; background-color:#e0e0e0; border-radius:10px; display:flex; align-items:center; justify-content:center;'>Placeholder Image</div>", unsafe_allow_html=True)


# How it works section
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p class="sub-header" style="text-align:center;">How It Works</p>', unsafe_allow_html=True)

col1_how, col2_how, col3_how = st.columns(3)

with col1_how:
    st.markdown('<h3 class="black-text" style="text-align:center;">1. Input Parameters</h3>', unsafe_allow_html=True)
    st.markdown('<p class="black-text">Enter the measured values from your water sample for each listed characteristic.</p>', unsafe_allow_html=True)

with col2_how:
    st.markdown('<h3 class="black-text" style="text-align:center;">2. Analysis</h3>', unsafe_allow_html=True)
    st.markdown('<p class="black-text">Our intelligent system processes your data, comparing it against safety standards and using a predictive model.</p>', unsafe_allow_html=True)

with col3_how:
    st.markdown('<h3 class="black-text" style="text-align:center;">3. Results</h3>', unsafe_allow_html=True)
    st.markdown('<p class="black-text">Get instant results on whether your water is likely safe to drink based on the analysis.</p>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p class="sub-header" style="text-align:center;">Understanding Water Quality Parameters</p>', unsafe_allow_html=True)

col1_params, col2_params = st.columns(2)

parameters = {
    "pH :": "Measures how acidic/basic the water is. Ideal range is 6.5-8.5.",
    "Hardness :": "Amount of dissolved calcium and magnesium. Affects taste and can cause scale buildup.",
    "Solids :": "Total dissolved solids (TDS) in the water. High levels can affect taste and indicate contamination.",
    "Chloramines :": "Disinfectants used in water treatment. Necessary for killing bacteria but can cause issues at high levels.",
    "Sulfate :": "Naturally occurring mineral. High levels can cause a bitter taste and laxative effects.",
    "Conductivity :": "Ability of water to conduct electricity, indicating the presence of ions.",
    "Organic_carbon :": "Amount of carbon bound in organic compounds. Can indicate contamination from decaying vegetation or industrial processes.",
    "Trihalomethanes :": "Byproducts of water disinfection. Can pose health risks at high levels.",
    "Turbidity :": "Cloudiness of water caused by suspended particles. Can indicate contamination.",
    "Potability :": "The final determination of whether water is safe to drink."
}

param_items_list = list(parameters.items())
mid_point = (len(param_items_list) + 1) // 2

for i, (param, desc) in enumerate(param_items_list):
    target_column = col1_params if i < mid_point else col2_params
    with target_column:
        st.markdown(f'<div class="card"><span class="parameter-name">{param}</span> <span class="parameter-desc">{desc}</span></div>', unsafe_allow_html=True)


# Call to action
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p class="sub-header" style="text-align:center;">Ready to check your water quality?</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.3rem; text-align:center;" class="black-text">Use our trained AI model to check your water quality</p>', unsafe_allow_html=True)


_, btn_col_centered, _ = st.columns([2, 1, 1.5])

with btn_col_centered:
    # Use markdown to create a div with text-align:center.
    # Since the button is display:inline-block, this will center it within this column.
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Try It Now", key="try_now_home", type="primary"):
        st.switch_page("pages/analyze.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p class="black-text">© 2025 SafeSip | All Rights Reserved</p>', unsafe_allow_html=True)