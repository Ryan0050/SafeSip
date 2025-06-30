import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# Set page configuration
st.set_page_config(
    page_title="SafeSip - Inputs",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

MODEL_PATH = "random_forest_model.joblib"
SCALER_PATH = "random_forest_scaler.joblib" 

@st.cache_resource # Cache the model to load it only once
def load_model_and_scaler(model_path, scaler_path):
    model = None
    scaler = None
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        st.error(f"FileNotFoundError: Model file not found at '{model_path}'.")
        st.error(f"Current directory: '{os.getcwd()}'. Please ensure the file exists or path is correct.")
    except ModuleNotFoundError as e:
        # Generalize the error message for missing libraries
        st.error(f"ModuleNotFoundError loading model: {e}. A library required by the model (e.g., 'scikit-learn', 'xgboost', etc.) might be missing.")
        st.error("Ensure your virtual environment is active and required libraries are installed (e.g., pip install scikit-learn).")
    except Exception as e:
        st.error(f"An unexpected error occurred while loading the model: {e}")

    try:
        scaler = joblib.load(scaler_path)
    except FileNotFoundError:
        st.error(f"FileNotFoundError: Scaler file not found at '{scaler_path}'.")
        st.error(f"Current directory: '{os.getcwd()}'. Please ensure the file exists or path is correct.")
        st.warning("If your model was trained on scaled data, predictions will be incorrect without the scaler.")
    except Exception as e:
        st.error(f"An unexpected error occurred while loading the scaler: {e}")
    
    return model, scaler

# Load the model and scaler when the script runs
model, scaler = load_model_and_scaler(MODEL_PATH, SCALER_PATH)

# Custom CSS for styling (Your CSS remains the same)
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #1E88E5 !important;
        margin-bottom: 1rem !important;
    }
    .sub-header {
        font-size: 1.8rem !important;
        font-weight: 500 !important;
        color: #0D47A1 !important;
    }
    .parameter-desc {
        color: #333333 !important;
        font-size: 1rem !important;
        margin-bottom: 1rem !important;
    }
    .stApp {
        background-color: #f0f8ff;
    }
    .step-container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .navigation-button {
        margin-top: 1rem;
    }
    .progress-container {
        margin-bottom: 2rem;
    }
            
    hr {
        height: 2px !important;
        border: none !important;
        color: #1E88E5 !important;
        background-color: #1E88E5 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }
            
    .parameter-label {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: #0277BD !important;
        margin-bottom: 0.5rem !important;
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
            
    body {
        overflow: auto !important;
    }

    .stApp > header{
        background-color: #1E88E5;
    }

    .main .block-container {
        max-width: 100%;
        padding-top: 1rem;
        padding-bottom: 1rem;
        overflow: auto !important;
    }

    div[data-testid="stSlider"] div[data-baseweb="slider"] > div:nth-of-type(2) {
        color: black !important; /* Targets the min value text */
    }
    div[data-testid="stSlider"] div[data-baseweb="slider"] > div:nth-of-type(3) {
        color: black !important; /* Targets the max value text */
    }

    .result-not-potable{
        font-size : 1.5rem;
        color : red;
        font-weight: bold;
    }
    
    .result-potable{
        font-size : 1.5rem;
        color : green;
        font-weight: bold;
    }

    .confidence{
        font-size: 1.5rem;
        color: #0277BD;
        margin-bottom: 0.5rem;
    }

    div[data-testid="stNumberInput"] input {
        border: 2px solid #1E88E5 !important;
        background-color: white !important;
        color: black !important;
        text-align: center !important;
        font-weight: 500 !important;
        padding: 8px !important;
        border-radius: 8px !important;
        width: 100% !important;
    }
    
    /* Remove arrows from number input */
    div[data-testid="stNumberInput"] input::-webkit-outer-spin-button,
    div[data-testid="stNumberInput"] input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    
    div[data-testid="stNumberInput"] input[type=number] {
        -moz-appearance: textfield;
    }
    
    /* Style for the min/max labels */
    .min-max-label {
        padding-top: 10px;
        color: #666;
        font-size: 0.9rem;
    }
    
    /* Add space before navigation buttons */
    .nav-spacer {
        height: 20px;
    }
    
    .stNumberInput:focus-within > div {
        border-color: #1E88E5 !important;
        box-shadow: none !important;
    }

</style>
""", unsafe_allow_html=True)

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
    st.markdown("<h3 style='color: #1976D2;'> App Information </h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1976D2;'> Our water quality analysis tool helps you determine if your water is safe to drink based on various chemical and physical parameters.</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #1976D2;'> Contact </h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1976D2;'>For more information, contact us at: safesip@gmail.com </p>", unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 1

# Make sure the order of features is exactly as your model input
EXPECTED_FEATURE_ORDER = [
    'ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
    'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'
]


if 'water_params' not in st.session_state:
    st.session_state.water_params = {param: None for param in EXPECTED_FEATURE_ORDER}


# Parameter ranges and descriptions
param_info = {
    'ph': {'min': 1.0, 'max': 14.0, 'desc': 'Measures how acidic/basic the water is. Ideal range is 6.5-8.5.', 'step': 0.1, 'default': 7.0},
    'Hardness': {'min': 30.0, 'max': 300.0, 'desc': 'Amount of dissolved calcium and magnesium in mg/L. Ideal range is 60-180 mg/L (moderately hard to hard).', 'step': 1.0, 'default': 150.0},
    'Solids': {'min': 100.0, 'max': 60000.0, 'desc': 'Total dissolved solids (TDS) in ppm. Ideal range is 50-150 ppm (for good taste and mineral balance).', 'step': 100.0, 'default': 20000.0},
    'Chloramines': {'min': 0.1, 'max': 13.0, 'desc': 'Disinfectants used in water treatment in mg/L. Ideal range is 0.5-4 mg/L.', 'step': 0.1, 'default': 7.0},
    'Sulfate': {'min': 100.0, 'max': 500.0, 'desc': 'Naturally occurring mineral in mg/L. Ideal range is less than 250 mg/L (with a maximum of 500 mg/L for aesthetic reasons).', 'step': 1.0, 'default': 300.0},
    'Conductivity': {'min': 100.0, 'max': 800.0, 'desc': 'Ability of water to conduct electricity in μS/cm. Ideal range is 50-500 μS/cm.', 'step': 1.0, 'default': 400.0},
    'Organic_carbon': {'min': 2.0, 'max': 30.0, 'desc': 'Amount of carbon bound in organic compounds in mg/L. Ideal range is less than 2 mg/L for treated water and less than 4 mg/L for source water.', 'step': 0.1, 'default': 15.0},
    'Trihalomethanes': {'min': 0.5, 'max': 150.0, 'desc': 'Byproducts of water disinfection in μg/L. Ideal range is less than 80 μg/L (US EPA MCL) or less than 100 μg/L (EU directive).', 'step': 0.5, 'default': 60.0},
    'Turbidity': {'min': 1.0, 'max': 7.0, 'desc': 'Cloudiness of water caused by suspended particles in NTU. Ideal range is 1.0-5.0 NTU.', 'step': 0.1, 'default': 4.0}
}

for param_key in EXPECTED_FEATURE_ORDER:
    if st.session_state.water_params.get(param_key) is None:
        st.session_state.water_params[param_key] = param_info[param_key]['default']

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

def go_to_results():
    st.session_state.step = len(EXPECTED_FEATURE_ORDER) + 1 

# Main header
st.markdown('<p class="main-header">Water Quality Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Input Your Water Quality Parameters</p>', unsafe_allow_html=True)

# Progress bar
total_steps = len(EXPECTED_FEATURE_ORDER) 
current_step_display = min(st.session_state.step, total_steps) 
st.markdown('<div class="progress-container">', unsafe_allow_html=True)
st.progress(current_step_display / total_steps if total_steps > 0 else 0)
if total_steps > 0 :
    st.markdown(f'<div class="parameter-label">Step {current_step_display} of {total_steps}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# Multi-step form for input
if st.session_state.step <= total_steps:
    current_param_key = EXPECTED_FEATURE_ORDER[st.session_state.step - 1]
    param_data = param_info[current_param_key]
    
    st.markdown(f'<p class="parameter-label">{current_param_key.replace("_", " ").title()}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="parameter-desc">{param_data["desc"]}</p>', unsafe_allow_html=True)
    
    current_value = float(st.session_state.water_params.get(current_param_key, param_data['default']))

    slider_key = f"slider_{current_param_key}"
    number_input_key = f"number_{current_param_key}"

    def slider_change_callback():
        st.session_state.water_params[current_param_key] = st.session_state[slider_key]

    def number_input_change_callback():
        st.session_state.water_params[current_param_key] = st.session_state[number_input_key]

    new_value_slider = st.slider(
        f"{current_param_key.replace('_', ' ').title()}",
        min_value=float(param_data['min']),
        max_value=float(param_data['max']),
        value=current_value, 
        step=float(param_data['step']),
        key=slider_key,
        on_change=slider_change_callback
    )

    col_num_1, col_num_2, col_num_3 = st.columns([2.2, 1, 2]) 
    with col_num_2:
        new_value_num_input = st.number_input(
            f"Enter {current_param_key.replace('_', ' ').title()} value",
            min_value=float(param_data['min']),
            max_value=float(param_data['max']),
            value=st.session_state.water_params[current_param_key], 
            step=float(param_data['step']),
            label_visibility="collapsed",
            key=number_input_key,
            on_change=number_input_change_callback
        )
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        if st.session_state.step > 1:
            st.button("Previous", on_click=prev_step, key="prev_button", type="secondary")
    with col2:
        if st.session_state.step < total_steps:
            st.button("Next", on_click=next_step, key="next_button", type="primary")
        else:
            st.button("Submit", on_click=go_to_results, key="submit_button", type="primary")

#Results page
elif st.session_state.step == total_steps + 1:
    st.markdown('<p class="sub-header">Water Quality Parameters Summary</p>', unsafe_allow_html=True)
    
    data_for_model_dict = {} 
    display_data_list = []
    
    all_params_filled = True
    for key in EXPECTED_FEATURE_ORDER: 
        value = st.session_state.water_params.get(key)
        if value is None: 
            all_params_filled = False
            st.warning(f"Parameter '{key}' was not set. Please go back and fill all values.")
            value = np.nan 
        
        data_for_model_dict[key] = value
        display_data_list.append({"Parameter": key.replace("_", " ").title(), "Value": "N/A" if pd.isna(value) else value})

    params_df_display = pd.DataFrame(display_data_list)
    st.dataframe(params_df_display, use_container_width=True, hide_index=True)

    st.markdown("<hr style='height: 2px; border: none; color: #1E88E5; background-color: #1E88E5;'>", unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI Analysis Result</p>', unsafe_allow_html=True)
    
    if not all_params_filled:
        st.error("Cannot perform analysis because some parameters are missing. Please use the 'Start Over' button.")
    elif model is None:
        st.error("Model could not be loaded. Cannot perform analysis.")
    elif scaler is None: 
        st.error("Scaler could not be loaded. Cannot perform analysis if model was trained on scaled data.")
        st.warning("If your model does NOT require scaled data, you can remove the scaler loading and usage.")
    else:
        try:
            input_df = pd.DataFrame([data_for_model_dict], columns=EXPECTED_FEATURE_ORDER)
            input_scaled = scaler.transform(input_df)
            prediction = model.predict(input_scaled) 
            
            try:
                probability = model.predict_proba(input_scaled)
            except AttributeError:
                probability = None

            result_value = prediction[0] 
            
            if result_value == 1:
                st.markdown('<div class="result-potable">💧 The water is predicted to be POTABLE.</div>', unsafe_allow_html=True)
                if probability is not None:
                    st.markdown(f'<div class="confidence">Model Confidence: {probability[0][1]*100:.2f}% Potable</div>', unsafe_allow_html=True)
            elif result_value == 0:
                st.markdown('<div class="result-not-potable">⚠️ The water is predicted to be NON-POTABLE.</div>', unsafe_allow_html=True)
                if probability is not None:
                    st.markdown(f'<div class="confidence">Model Confidence: {probability[0][0]*100:.2f}% Non-Potable</div>', unsafe_allow_html=True)
            else:
                st.info(f"Model returned an unexpected prediction value: {result_value}")

        except ValueError as ve:
            st.error(f"ValueError during prediction: {ve}")
            st.warning("This might be due to incorrect data types or shapes. Ensure all inputs are numeric and the scaler/model are compatible.")
            st.code(f"Data sent to scaler: \n{input_df.to_string()}")
        except Exception as e:
            st.error(f"An unexpected error occurred during prediction: {e}")
            st.warning("Please ensure all parameters were entered correctly and the model/scaler are compatible with the input.")
            st.code(f"Data sent to scaler: \n{input_df.to_string()}")
            
    if st.button("⬅️ Start Over", key="restart_button", type="secondary", use_container_width=True):
        st.session_state.step = 1
        for param_key_reset in EXPECTED_FEATURE_ORDER:
            st.session_state.water_params[param_key_reset] = param_info[param_key_reset]['default']
        st.rerun()