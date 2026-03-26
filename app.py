import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("University Admission Predictor")

gre = st.number_input("GRE Score", 260, 340)
toefl = st.number_input("TOEFL Score", 0, 120)
rating = st.slider("University Rating", 1, 5)
sop = st.slider("SOP Strength", 1.0, 5.0)
lor = st.slider("LOR Strength", 1.0, 5.0)
cgpa = st.number_input("CGPA (out of 10)", 0.0, 10.0)
research = st.selectbox("Research Experience", [0, 1])

if st.button("Predict"):
    input_data = np.array([[gre, toefl, rating, sop, lor, cgpa, research]])
    prediction = model.predict(input_data)[0]
    st.success(f"Chance of Admission: {prediction*100:.2f}%")
