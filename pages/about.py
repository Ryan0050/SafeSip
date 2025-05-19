import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Set page configuration
st.set_page_config(
    page_title="About Our AI Model - SafeSip",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
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
            
    .section-header {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #0277BD !important;
    }
            
    .content-text {
        color: #333333 !important;
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
    }
    
    .black-text, 
    h3.black-text, 
    p.black-text {
        color: #000000 !important;
    }

    .highlight-box {
        background-color: #E3F2FD;
        border-left: 4px solid #1E88E5;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1.5rem 0;
    }
            
    .feature-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
            
    .stApp {
        background-color: #f0f8ff;
    }
            
    hr {
        height: 2px !important;
        border: none !important;
        color: #1E88E5 !important;
        background-color: #1E88E5 !important;
        margin-top: 0.5rem !important;
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

with st.sidebar:
    if st.button("🏠 Home", key="sidebar_home_button", use_container_width=True):
        st.session_state.current_page = "app.py"
        st.switch_page("app.py")

    if st.button("📊 Analyze", key="sidebar_analyze_button", use_container_width=True):
        st.session_state.current_page = "analyze.py"
        st.switch_page("pages/analyze.py")

    if st.button("ℹ️ About", key="sidebar_about_button", use_container_width=True):
        st.switch_page("pages/about.py")
    
    st.markdown("---")
    st.markdown("<h3 style='color: #1976D2;'> App Information </h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1976D2;'> Our water quality analysis tool helps you determine if your water is safe to drink based on various chemical and physical parameters.</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #1976D2;'> Contact </h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1976D2;'>For more information, contact us at: safesip@gmail.com </p>", unsafe_allow_html=True)


st.markdown('<p class="main-header">About Our AI Model</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">How We Determine Water Potability</p>', unsafe_allow_html=True)


st.markdown('<p class="content-text" style="padding-bottom: 1rem;">Our water quality analysis tool uses advanced machine learning to determine if your water is safe to drink. We leverage the power of a <strong>Random Forest</strong>, a robust algorithm that analyzes multiple water quality parameters to provide accurate potability predictions.</p>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)


st.markdown('<p class="sub-header">What is Random Forest?</p>', unsafe_allow_html=True)

st.markdown('<p class="content-text"><strong>Random Forest</strong> is a popular and powerful machine learning algorithm that uses an ensemble of decision trees to make predictions. It operates by constructing a multitude of decision trees during training and then combining their outputs (e.g., by voting for classification tasks). It\'s widely recognized in the data science community for its:</p>', unsafe_allow_html=True)

st.markdown("""
<div class="black-text" style="font-size: 1.1rem; padding-left: 2rem; padding-right: 2rem; padding-bottom: 1rem;">
<ul>
    <li><strong>High Accuracy</strong>: Often achieves strong predictive performance across various tasks.</li>
    <li><strong>Speed and Efficiency</strong>: Can be trained relatively quickly, especially with parallel processing.</li>
    <li><strong>Robustness</strong>: Handles non-linear data well and is relatively robust to outliers.</li>
    <li><strong>Interpretability</strong>: Provides insights into which water parameters are most important for the prediction.</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)


st.markdown('<p class="sub-header">How Our Water Quality Model Works</p>', unsafe_allow_html=True)
st.markdown('<p class="content-text">Our <strong>Random Forest</strong> model was trained on thousands of water samples with known potability outcomes. The model learned patterns and relationships between water quality parameters and whether the water was safe to drink.</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h3 class="section-header">When you input your water quality parameters, our system:</h3>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<h3 class="black-text">1. Data Processing </h3>', unsafe_allow_html=True)
    st.markdown('<p class="black-text">Your input parameters are processed and (if necessary) scaled to match the format our model was trained on. </p>', unsafe_allow_html=True)

with col2:
    st.markdown('<h3 class="black-text">2. Prediction </h3>', unsafe_allow_html=True)
    st.markdown('<p class="black-text">The <strong>Random Forest</strong> model analyzes the complex relationships between all parameters to determine potability.</p>', unsafe_allow_html=True)

with col3:
    st.markdown('<h3 class="black-text">3. Explanation </h3>', unsafe_allow_html=True)
    st.markdown('<p class="black-text">The system provides not just a result, but also indicates the model\'s confidence and can highlight influential factors based on feature importance.</p>', unsafe_allow_html=True)


st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Parameter Importance</p>', unsafe_allow_html=True)
st.markdown('<p class="content-text">Not all water quality parameters have equal importance in determining potability. Our model, like many tree-based models, can estimate the relative importance of each parameter:</p>', unsafe_allow_html=True) # Slight rephrase for generality


feature_importance = {
    'Parameter': ['pH', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
                  'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'],
    'Importance': [14.18, 11.48, 11.05, 11.66, 14.53, 9.33, 9.06, 9.58, 9.1]
}

fig, ax = plt.subplots(figsize=(16.5, 7.5))
y_pos = np.arange(len(feature_importance['Parameter']))
ax.barh(y_pos, feature_importance['Importance'], color='#1E88E5')
ax.set_yticks(y_pos)
ax.set_yticklabels(feature_importance['Parameter'])
ax.invert_yaxis()
ax.set_xlabel('Relative Importance (%)')
ax.set_title('Water Quality Parameter Importance in Potability Prediction (Illustrative)')

for i, v in enumerate(feature_importance['Importance']):
    ax.text(v + 0.2, i, f"{v}%", va='center')

plt.tight_layout()
st.pyplot(fig)
st.markdown('<hr>', unsafe_allow_html=True)

st.markdown('<p class="sub-header">Model Accuracy</p>', unsafe_allow_html=True)
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("""
    <div class="black-text" style="font-size: 1.1rem; padding-left: 2rem; padding-right: 2rem; padding-bottom: 1rem;">
    <ul>
        <li><strong>72% Overall Accuracy</strong>:  Correctly predicts water potability in 72% of cases</li>
        <li><strong>Low False Negatives</strong>: Aims to minimize the chance of classifying unsafe water as safe.</li>
        <li><strong>Continuous Improvement</strong>: The model can be regularly updated with new data.</li>
        <li><strong>Validated Against Laboratory Tests</strong>: Ideally, results are compared with standard water testing procedures.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    conf_matrix = np.array([[223, 29], [82, 69]])
    
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Predicted Potable', 'Predicted Non-Potable'],
                yticklabels=['Actually Potable', 'Actually Non-Potable'])
    plt.title('Model Prediction Accuracy (Illustrative)')
    plt.tight_layout()
    st.pyplot(fig)

st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Limitations and Considerations</p>', unsafe_allow_html=True)

st.markdown('<p class="section-header">Even with a highly accurate model, it\'s important to understand its limitations:</p>', unsafe_allow_html=True)
st.markdown("""
<p class="black-text">The model provides a prediction of potability based on learned patterns, not an absolute guarantee.</p>
<p class="black-text">Unusual contaminants not included in the training data or extreme parameter values may affect accuracy.</p>
<p class="black-text">This tool is meant to be informative and should not replace official laboratory water testing, especially in critical situations.</p>
<p class="black-text">Always follow local health guidelines regarding water safety.</p>
""", unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

st.markdown('<p class="sub-header">Ready to Test Your Water?</p>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown('<p class="content-text">Use our water quality analysis tool to check if your water is safe to drink. Simply input your water parameters and let our <strong>Random Forest</strong> model do the analysis.</p>', unsafe_allow_html=True)


if st.button("Test Your Water Now", type="primary"):
    st.switch_page("pages/analyze.py")

st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<p class="black-text">© 2025 SafeSip | All Rights Reserved</p>', unsafe_allow_html=True)