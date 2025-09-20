st.set_page_config(
    page_title="Term Deposit Prediction",
    page_icon="🏦",
    layout="wide"
)

# Title and description
st.title("🏦 Term Deposit Subscription Prediction")
st.markdown("Predict customer likelihood to subscribe to term deposits using machine learning")

# Sidebar for user inputs
st.sidebar.header("Customer Information")

# Input fields based on your model features
age = st.sidebar.slider("Age", 18, 95, 40)
job = st.sidebar.selectbox("Job", ["admin", "technician", "services", "management", "retired", 
                                  "blue-collar", "unemployed", "entrepreneur", "housemaid", 
                                  "unknown", "self-employed", "student"])
marital = st.sidebar.selectbox("Marital Status", ["married", "single", "divorced"])
education = st.sidebar.selectbox("Education", ["secondary", "tertiary", "primary", "unknown"])
default = st.sidebar.selectbox("Has Credit Default?", ["no", "yes"])
balance = st.sidebar.number_input("Account Balance", -8000, 100000, 1500)
housing = st.sidebar.selectbox("Has Housing Loan?", ["no", "yes"])
loan = st.sidebar.selectbox("Has Personal Loan?", ["no", "yes"])
contact = st.sidebar.selectbox("Contact Method", ["cellular", "telephone", "unknown"])
duration = st.sidebar.slider("Last Contact Duration (seconds)", 0, 5000, 250)
campaign = st.sidebar.slider
