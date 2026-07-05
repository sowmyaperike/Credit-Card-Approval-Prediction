from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and feature columns
model = joblib.load("models/credit_card_model.pkl")
columns = joblib.load("models/feature_columns.pkl")


# -------------------- HOME PAGE --------------------
@app.route("/")
def home():
    return render_template("home.html")


# -------------------- PREDICTION PAGE --------------------
@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


# -------------------- RESULT PAGE --------------------
@app.route("/predict", methods=["POST"])
def predict():

    # Create dictionary with all model features initialized to 0
    data = {col: 0 for col in columns}

    # Numeric Features
    data["ID"] = 0
    data["CNT_CHILDREN"] = float(request.form["children"])
    data["AMT_INCOME_TOTAL"] = float(request.form["income"])
    data["CNT_FAM_MEMBERS"] = float(request.form["family_members"])
    data["AGE"] = float(request.form["age"])
    data["YEARS_EMPLOYED"] = float(request.form["years_employed"])

    # Default Flags
    data["FLAG_MOBIL"] = 1
    data["FLAG_WORK_PHONE"] = 0
    data["FLAG_PHONE"] = 0
    data["FLAG_EMAIL"] = 0

    # Gender
    if request.form["gender"] == "Male":
        data["CODE_GENDER_M"] = 1

    # Own Car
    if request.form["own_car"] == "Yes":
        data["FLAG_OWN_CAR_Y"] = 1

    # Own Realty
    if request.form["own_realty"] == "Yes":
        data["FLAG_OWN_REALTY_Y"] = 1

    # Income Type
    income_feature = "NAME_INCOME_TYPE_" + request.form["income_type"]
    if income_feature in data:
        data[income_feature] = 1

    # Education
    education_feature = "NAME_EDUCATION_TYPE_" + request.form["education"]
    if education_feature in data:
        data[education_feature] = 1

    # Family Status
    family_feature = "NAME_FAMILY_STATUS_" + request.form["family_status"]
    if family_feature in data:
        data[family_feature] = 1

    # Housing Type
    housing_feature = "NAME_HOUSING_TYPE_" + request.form["housing_type"]
    if housing_feature in data:
        data[housing_feature] = 1

    # Occupation
    occupation_feature = "OCCUPATION_TYPE_" + request.form["occupation"]
    if occupation_feature in data:
        data[occupation_feature] = 1

    # Convert to DataFrame in correct column order
    df = pd.DataFrame([data])
    df = df[columns]

    # Prediction
    prediction = model.predict(df)[0]

    if prediction == 0:
        result = "✅ Credit Card Approved"
    else:
        result = "❌ Credit Card Rejected"

    return render_template("result.html", prediction=result)


# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(debug=True)