import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("Flight Fare Prediction")

def create_input_df():
    return pd.DataFrame(0, index=[0], columns=columns)

# User Inputs
source = st.selectbox("Source", ["BLR","CCU","DEL","MAA","BOM"])
destination = st.selectbox("Destination", ["DEL","BLR","COK","CCU","HYD"])
duration = st.number_input("Duration (minutes)", min_value=30)
dep_hour = st.slider("Departure Hour", 0, 23)
arr_hour = st.slider("Arrival Hour", 0, 23)

# Prediction
if st.button("Predict Price"):

    df = create_input_df()

    # Set source & destination
    if f"Source_code_{source}" in df.columns:
        df[f"Source_code_{source}"] = 1

    if f"Destination_code_{destination}" in df.columns:
        df[f"Destination_code_{destination}"] = 1

    # Time features
    df['Dep_hour_sin'] = np.sin(2 * np.pi * dep_hour / 24)
    df['Dep_hour_cos'] = np.cos(2 * np.pi * dep_hour / 24)
    df['Arrival_hour_sin'] = np.sin(2 * np.pi * arr_hour / 24)
    df['Arrival_hour_cos'] = np.cos(2 * np.pi * arr_hour / 24)

    # Duration
    df['Duration_log'] = np.log1p(duration)

    # Prediction
    pred = np.expm1(model.predict(df))

    st.success(f"Estimated Flight Price: Rs {int(pred[0])}")
