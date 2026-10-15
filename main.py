
import random

from fastapi import FastAPI, Query

# Lab-defined student details
SEED = 4
REGISTRATION_NUMBER = "FA23-BDS-004"

# Generate coefficients deterministically
random.seed(SEED)

a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = FastAPI(title="Linear Regression Prediction API")


@app.get("/")
def home():
    return {"message": "Linear Regression Prediction API"}


@app.get("/predict")
def predict(
    x1: float = Query(...),
    x2: float = Query(...),
    x3: float = Query(...),
):
    prediction = a1 * x1 + a2 * x2 + a3 * x3 + b

    return {
        "registration number": REGISTRATION_NUMBER,
        "prediction": round(prediction, 2),
    }
