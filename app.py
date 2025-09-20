
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Term Deposit Prediction",
    page_icon="🏦",
    layout="wide"
)

# Load your trained model and encoders
@st.cache_resource
def load_model():
    model = pickle.load(open('decision_tree_model.pkl', 'rb'))
    label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))
    return model, label_encoders

model, label_encoders = load_model()

# Title and description
st.title("🏦 Term Deposit Subscription Prediction")
st.markdown("Predict whether a customer will subscribe to a term deposit based on their profile")

# Sidebar for input features
st.sidebar.header("Customer Information")

# Input fields
age = st.sidebar.slider("Age", min_value=18, max_value=95, value=40)
job = st.sidebar.selectbox("Job", [
    'admin.', 'technician', 'services', 'management', 'retired',
    'blue-collar', 'unemployed', 'entrepreneur', 'housemaid',
    'unknown', 'self-employed', 'student'
])
marital = st.sidebar.selectbox("Marital Status", ['married', 'single', 'divorced'])
education = st.sidebar.selectbox("Education", ['secondary', 'tertiary', 'primary', 'unknown'])
default = st.sidebar.selectbox("Has Credit in Default?", ['no', 'yes'])
balance = st.sidebar.number_input("Account Balance", value=1000, step=100)
housing = st.sidebar.selectbox("Has Housing Loan?", ['no', 'yes'])
loan = st.sidebar.selectbox("Has Personal Loan?", ['no', 'yes'])
contact = st.sidebar.selectbox("Contact Communication Type", ['cellular', 'telephone', 'unknown'])
day = st.sidebar.slider("Day of Month", min_value=1, max_value=31, value=15)
month = st.sidebar.selectbox("Month", [
    'jan', 'feb', 'mar', 'apr', 'may', 'jun',
    'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
])
duration = st.sidebar.number_input("Last Contact Duration (seconds)", min_value=0, value=300)
campaign = st.sidebar.number_input("Number of Contacts in Current Campaign", min_value=1, value=2)
pdays = st.sidebar.number_input("Days Since Previous Contact (-1 if not contacted)", value=-1)
previous = st.sidebar.number_input("Number of Previous Contacts", min_value=0, value=0)
poutcome = st.sidebar.selectbox("Previous Campaign Outcome", ['unknown', 'failure', 'success'])

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Prediction")

    if st.button("Predict Subscription", type="primary"):
        # Create input dataframe
        input_data = pd.DataFrame({
            'age': [age],
            'job': [job],
            'marital': [marital],
            'education': [education],
            'default': [default],
            'balance': [balance],
            'housing': [housing],
            'loan': [loan],
            'contact': [contact],
            'day': [day],
            'month': [month],
            'duration': [duration],
            'campaign': [campaign],
            'pdays': [pdays],
            'previous': [previous],
            'poutcome': [poutcome]
        })

        # Encode categorical features
        processed_input = input_data.copy()
        for col in input_data.columns:
            if col in label_encoders and col != 'deposit':
                processed_input[col] = label_encoders[col].transform(processed_input[col])

        # Make prediction
        prediction = model.predict(processed_input)[0]
        probability = model.predict_proba(processed_input)[0][1]

        # Display input summary
        st.write("**Customer Profile:**")
        st.write(f"- {age}-year-old {marital} {job}")
        st.write(f"- Education: {education}")
        st.write(f"- Account Balance: ${balance:,}")
        st.write(f"- Last Contact Duration: {duration} seconds")

        if prediction == 1:
            st.success(f"✅ **Likely to Subscribe** (Confidence: {probability:.1%})")
        else:
            st.error(f"❌ **Unlikely to Subscribe** (Confidence: {1-probability:.1%})")

        # Probability gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Subscription Probability (%)"},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "green"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 70
                }
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Key Insights")
    st.info("""
    **Top Predictors:**
    1. Call Duration
    2. Contact Method
    3. Days Since Last Contact

    **Success Tips:**
    - Longer conversations = higher success
    - Cellular contact works better
    - Target management professionals
    - June campaigns perform best
    """)

# Model Performance Section
st.subheader("📊 Model Performance")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Accuracy", "76.2%", "4.4%")
with col2:
    st.metric("Precision", "69.5%", "2.1%")
with col3:
    st.metric("Recall", "86.4%", "3.2%")
with col4:
    st.metric("F1-Score", "77.0%", "2.8%")

# Feature Importance Visualization
st.subheader("🎯 Feature Importance")
features = model.feature_names_in_  # get feature names from trained model
importance = model.feature_importances_

fi = pd.DataFrame({
    "Features": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=True)

fig = px.bar(fi.tail(5), x="Importance", y="Features", orientation='h',
             title="Top 5 Most Important Features")
fig.update_layout(xaxis_title="Importance Score", yaxis_title="Features")
st.plotly_chart(fig, use_container_width=True)
