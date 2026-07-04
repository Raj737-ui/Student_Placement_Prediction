
import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Load the pickle file
with open("placement_model.pkl", "rb") as file:
    data = pickle.load(file)

# Extract objects
model = data["model"]
encoder = data["encoder"]
scaler = data["scaler"]



st.sidebar.image("logo.png", width=100)
st.sidebar.title("Placement Prediction")
st.sidebar.title("🎓 Placement Prediction")

st.markdown("""
<style>

/* ===========================
   MAIN APP BACKGROUND
=========================== */
.stApp {
    background: linear-gradient(135deg,#0F2027,#203A43,#2C5364);
    color: white;
}

/* ===========================
   SIDEBAR
=========================== */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0B132B,#1C2541);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* ===========================
   TITLES
=========================== */

h1{
    color:#FFFFFF;
    text-align:center;
    font-size:40px;
    font-weight:bold;
}

h2,h3,h4{
    color:#F8FAFC;
}

/* ===========================
   LABELS
=========================== */

label{
    color:white !important;
    font-weight:600;
    font-size:16px;
}

/* ===========================
   NUMBER INPUT
=========================== */

.stNumberInput input{
    background:white !important;
    color:black !important;
    border-radius:10px;
}

/* ===========================
   SELECT BOX
=========================== */

div[data-baseweb="select"] > div{
    background:white !important;
    color:black !important;
    border-radius:10px;
}

/* Selected Value */
div[data-baseweb="select"] span{
    color:black !important;
}

/* Dropdown Menu */
div[data-baseweb="popover"]{
    background:white !important;
}

div[data-baseweb="menu"]{
    background:white !important;
}

div[data-baseweb="menu"] div{
    color:black !important;
    background:white !important;
}

div[data-baseweb="menu"] div:hover{
    background:#D6EAF8 !important;
}

/* ===========================
   SLIDER
=========================== */

.stSlider label{
    color:white !important;
}

/* ===========================
   BUTTON
=========================== */

.stButton>button{

    width:100%;

    background:linear-gradient(90deg,#00C9FF,#92FE9D);

    color:black;

    border:none;

    border-radius:12px;

    height:50px;

    font-size:18px;

    font-weight:bold;
}

.stButton>button:hover{

    background:linear-gradient(90deg,#36D1DC,#5B86E5);

    color:white;

    transform:scale(1.02);
}

/* ===========================
   METRIC CARD
=========================== */

div[data-testid="metric-container"]{

    background:rgba(255,255,255,0.12);

    border-radius:15px;

    padding:18px;

    border:1px solid rgba(255,255,255,0.2);

    backdrop-filter:blur(8px);
}

/* ===========================
   SUCCESS
=========================== */

.stSuccess{

    background:#22C55E !important;

    color:white !important;

    border-radius:10px;
}

/* ===========================
   ERROR
=========================== */

.stError{

    background:#EF4444 !important;

    color:white !important;

    border-radius:10px;
}

/* ===========================
   PROGRESS BAR
=========================== */

.stProgress > div > div > div > div{
    background:#22C55E;
}

/* ===========================
   HORIZONTAL LINE
=========================== */

hr{
    border:1px solid rgba(255,255,255,0.2);
}

/* ===========================
   REMOVE STREAMLIT MENU
=========================== */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dataset",
        "🤖 Prediction",
        "📈 Model Performance"
    ]
)

if page == "🏠 Home":
    st.title("Student Placement Prediction")
    st.subheader("Predict campus placement using Machine Learning.")


elif page == "📊 Dataset":
    st.title("Dataset")
    st.markdown("""
        This dataset is used to predict whether a student will be placed based on
        academic performance, skills, and extracurricular achievements.
    """)
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", "45,000")
    col2.metric("Features", "15")
    col3.metric("Target Classes", "1")

    st.divider()

    st.subheader("Dataset Summary")

    summary = {
        "Attribute": [
            "Dataset Name",
            "Total Records",
            "Total Features",
            "Target Variable",
            "Missing Values",
            "Duplicate Records",
            "Numerical Features",
            "Categorical Features"
        ],
        "Value": [
            "Student Placement Prediction",
            "45,000",
            "15",
            "Placement Status",
            "0",
            "0",
            "5",
            "5"
        ]
    }

    st.dataframe(pd.DataFrame(summary), use_container_width=True)

elif page == "🤖 Prediction":
    st.title("🤖 Prediction")
    st.write("Prediction form goes here.")

    st.markdown("Fill in the student details below to predict placement status.")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 0,60,23, key = "Age")
        gender = st.selectbox("Gender", ["Male", "female"], key = "Gender")
        degree = st.selectbox("Degree",
                     ["B.Tech", "B.E", "B.Sc", "BCA", "M.Tech", "MBA", "MCA"],
                     key = "Degree")
        branch = st.selectbox("Branch", ["NA" ,"CSE", "IT", "ECE", "EEE",  "Mechanical",
                                 "Civil", "Electrical"], key = "Branch")
        cgpa = st.slider("CGPA", 0,10,7 , key = "CGPA")
        internships = st.slider("Internships", 0,10,2, key = "Internships")
        projects = st.slider("Projects", 0,10,2, key = "Projects")

    with col2:
        coding = st.slider("Coding Skills", 0,100,70,key = "coding" )
        communication = st.slider("Communication Skills", 0,100,70,key = "communication" )
        aptitude = st.slider("Aptitude Test Score ", 0,100,70,key = "aptitude")
        soft_skills = st.slider("Soft Skills", 0,10,6, key = "soft_skills")
        certifications = st.slider("Certifications", 0,10,3, key = "certifications")
        backlogs = st.slider("Backlogs", 0,10,1, key = "backlogs")

    gender_map = {
        "Female": 0,
        "Male": 1
    }

    degree_map = {
        "B.Tech": 0,
        "B.E": 1,
        "B.Sc": 2,
        "BCA": 3,
        "M.Tech": 4,
        "MBA": 5,
        "MCA": 6
    }

    branch_map = {
        "NA": 0,
        "CSE": 1,
        "IT": 2,
        "ECE": 3,
        "EEE": 4,
        "Mechanical": 5,
        "Civil": 6,
        "Electrical": 7
    }

    gender = gender_map[gender]
    degree = degree_map[degree]
    branch = branch_map[branch]

    if st.button("🚀 Predict Placement", use_container_width=True):
        input_data = np.array([[
            age,
            gender,
            degree,
            branch,
            cgpa,
            internships,
            projects,
            coding,
            communication,
            aptitude,
            soft_skills,
            certifications,
            backlogs
        ]])

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)



        st.divider()

        if prediction[0] == 1:

            st.success("🎉 Student is likely to be PLACED")
            st.success("Congratulations")



        else:

            st.error("❌ Student is likely to be NOT PLACED")
            st.error("Better Luck next time")

           






elif page == "📈 Model Performance":
    st.title("Model Performance")
    st.markdown("""
            Ths page shows the information on performance of model 
        """)
    col1, col2, col3 = st.columns(3)

    col1.metric("Model", "KNN")
    col2.metric("Accuracy", "93.60%")


    st.divider()

    st.subheader("Performance")

    summary = {
        "Attribute": [
            "Models",
            "Accuracy",
            "Precison",
            "Recall",
            "F1-Score",
        ],
        "Value": [
            "KNN",
            "93.60 %%",
            "88.08 %",
            "95.21 %",
            "91.51 %"
        ]
    }

    st.dataframe(pd.DataFrame(summary), use_container_width=True)




