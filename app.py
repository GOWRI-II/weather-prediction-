
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("weather_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="Weather Prediction",
    page_icon="🌦️"
)

st.title("🌦️ Weather Prediction System")
st.write("Enter weather conditions to predict whether it may rain.")

# User inputs
temperature = st.number_input(
    "Temperature (°C)", min_value=-10.0,
    max_value=60.0, value=24.0
)

humidity = st.slider(
    "Humidity (%)", 0, 100, 85
)

wind_speed = st.number_input(
    "Wind Speed (km/h)", min_value=0.0,
    max_value=200.0, value=20.0
)

pressure = st.number_input(
    "Pressure (hPa)", min_value=850.0,
    max_value=1100.0, value=1005.0
)

# Prediction button
if st.button("Predict Weather"):
    input_data = pd.DataFrame(
        [[temperature, humidity, wind_speed, pressure]],
        columns=[
            "Temperature",
            "Humidity",
            "Wind_Speed",
            "Pressure"
        ]
    )

    prediction = model.predict(input_data)[0]

    if prediction == "Yes":
        st.warning("🌧️ Prediction: Rain may occur.")
    else:
        st.success("☀️ Prediction: Rain is less likely.")

    st.caption(
        "Educational demo using sample data, not a reliable "
        "real-world weather forecast."
    )
