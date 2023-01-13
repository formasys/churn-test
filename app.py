import streamlit
import requests as re
import json
import pandas as pd

df = pd.read_csv("Churn_Modelling.csv")


def run():
    streamlit.title("Churn Prediction")
    CreditScore = streamlit.number_input("CreditScore")
    Geography = streamlit.selectbox("Geography", df.Geography.unique())
    Gender = streamlit.selectbox("Sexe", df.Gender.unique())
    Age = streamlit.number_input("Age")
    Tenure = streamlit.selectbox("Produits", df.Tenure.unique())
    Balance = streamlit.number_input("Balance")
    NumOfProducts = streamlit.selectbox("nombre de produits", df.NumOfProducts.unique())
    HasCrCard = streamlit.selectbox("Carte", df.HasCrCard.unique())
    IsActiveMember = streamlit.selectbox("Active?", df.IsActiveMember.unique())
    EstimatedSalary = streamlit.number_input("Salaire")

    data_pred = {
        "CreditScore":CreditScore,
        "Geography":Geography,
        "Gender":Gender,
        "Age":Age,
        "Tenure":Tenure,
        "Balance":Balance,
        "NumOfProducts":NumOfProducts,
        "HasCrCard":HasCrCard,
        "IsActiveMember":IsActiveMember,
        "EstimatedSalary":EstimatedSalary,
    }


    if streamlit.button("Predict"):
        streamlit.info(data_pred)
        #response = requests.post("http://0.0.0.0:8000/predict", data=json.dumps(data_pred, default=str))
        #response = requests.post("http://127.0.0.1:8000/predict", json=data_pred )
        #prediction = response.text
        #streamlit.success(f"The prediction from model: {prediction}")
        response = re.post("http://127.0.0.1:8000/predict", data=json.dumps(data_pred, default=str))
        prediction = response.text
        streamlit.success(f"The prediction from model: {prediction}")



if __name__ == '__main__':
    # by default it will run at 8501 port
    run()

# lancer l'app streamlit run app.py