# Import Needed Libraries
import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel

# FastAPI libray
from fastapi import FastAPI

# Initiate app instance
app = FastAPI(title='Churn Prediction', version='1.0',
              description='Best model is used for prediction')

# Initialize model artifacte files. This will be loaded at the start of FastAPI model server.
model = joblib.load("best_model.pkl")


# This struture will be used for Json validation.
# With just that Python type declaration, FastAPI will perform below operations on the request data
## 1) Read the body of the request as JSON.
## 2) Convert the corresponding types (if needed).
## 3) Validate the data.If the data is invalid, it will return a nice and clear error,
##    indicating exactly where and what was the incorrect data.
class Data(BaseModel):
    CreditScore:int
    Geography:str
    Gender:str
    Age:int
    Tenure:int
    Balance:float
    NumOfProducts:int
    HasCrCard:int
    IsActiveMember:int
    EstimatedSalary:float


# Api root or home endpoint
@app.get('/')
@app.get('/home')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'System is healthy'}


# ML API endpoint for making prediction aganist the request received from client
@app.post("/predict")
def predict(data:Data):
    data = data.dict()
    print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',data)
    prediction = model.predict(pd.DataFrame(columns=list(data.keys()), data=[list(data.values())]))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",prediction)
    if(prediction[0]>0.5):
        predictionchurn="churn client"
    else:
        predictionchurn="Not chrun client"
    return predictionchurn


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# lancer l'api: uvicorn main:app --reload