# Weather Prediction Using Machine Learning

## Project Overview
This project predicts whether it will rain tomorrow based on weather conditions using Machine Learning.

## Objective
The main objective is to predict tomorrow's rainfall using parameters such as temperature, humidity, wind speed, and pressure.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Pickle
- VS Code

## Dataset
The dataset contains the following features:
- Temperature
- Humidity
- Wind Speed
- Pressure
- Rain Tomorrow

## Machine Learning Model
A Machine Learning classification model is trained using weather data to predict whether it will rain tomorrow.

## Project Features
- Weather data preprocessing
- Machine Learning model training
- Rainfall prediction
- FastAPI integration
- API-based predictions

## How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python -m uvicorn app:app --reload
```

### 3. Open API Documentation

http://127.0.0.1:8000/docs

## Deployment
The application is deployed using Render.

## Author
Gowri Kulkarni