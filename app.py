import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Disease Prediction System",
    layout="wide",
    page_icon="🩺",
)

# Custom Styling
st.markdown(
    """
    <style>
        /* Main background and text color */
        body {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #1F2937 !important;
        }
        /* Button styling */
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        /* Input field styling */
        .stTextInput > div > div > input {
            background-color: #1F2937;
            color: #FAFAFA;
            border-radius: 8px;
            border: 1px solid #4CAF50;
        }
        /* Title and header styling */
        h1, h2, h3, h4, h5, h6 {
            color: #4CAF50;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Get working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        'Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0,
        styles={
            "container": {"background-color": "#1F2937"},
            "icon": {"color": "#4CAF50"},
            "nav-link": {"color": "#FAFAFA", "font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#4CAF50"},
        }
    )

# Function to create input fields with three columns per row
def get_input(fields):
    inputs = []
    for i in range(0, len(fields), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(fields):
                with cols[j]:
                    inputs.append(float(st.text_input(fields[i + j], "0")))
    return inputs

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction 🩸')
    st.markdown("Enter the following details to predict diabetes risk.")
    user_input = get_input([
        'Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness',
        'Insulin', 'BMI', 'Diabetes Pedigree Function', 'Age'
    ])
    if st.button('Predict Diabetes'):
        result = 'Diabetic' if diabetes_model.predict([user_input])[0] else 'Not Diabetic'
        if result == 'Diabetic':
            st.error(f'Result: {result} ⚠️')
        else:
            st.success(f'Result: {result} ✅')

# Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction 🫀')
    st.markdown("Enter the following details to predict heart disease risk.")
    user_input = get_input([
        'Age', 'Sex (0: Female, 1: Male)', 'Chest Pain Type (0-3)', 'Resting BP', 'Cholesterol',
        'Fasting Blood Sugar (0: No, 1: Yes)', 'Rest ECG (0-2)', 'Max Heart Rate',
        'Exercise Angina (0: No, 1: Yes)', 'Oldpeak', 'Slope (0-2)', 'Major Vessels (0-3)', 'Thal (0-3)'
    ])
    if st.button('Predict Heart Disease'):
        result = 'Has Heart Disease' if heart_disease_model.predict([user_input])[0] else 'No Heart Disease'
        if result == 'Has Heart Disease':
            st.error(f'Result: {result} ⚠️')
        else:
            st.success(f'Result: {result} ✅')

# Parkinson's Prediction
elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction 🧠")
    st.markdown("Enter the following details to predict Parkinson's disease risk.")
    user_input = get_input([
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'Jitter(%)', 'Jitter(Abs)',
        'RAP', 'PPQ', 'Jitter:DDP', 'Shimmer', 'Shimmer(dB)',
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR',
        'HNR', 'RPDE', 'DFA', 'Spread1', 'Spread2', 'D2', 'PPE'
    ])
    if st.button("Predict Parkinson's"):
        result = "Has Parkinson's" if parkinsons_model.predict([user_input])[0] else "No Parkinson's"
        if result == "Has Parkinson's":
            st.error(f'Result: {result} ⚠️')
        else:
            st.success(f'Result: {result} ✅')