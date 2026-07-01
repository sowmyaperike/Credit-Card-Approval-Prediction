from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("models/credit_card_model.pkl")
columns = joblib.load("models/feature_columns.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {}

    for col in columns:
        value = request.form.get(col)

        if value is None or value == "":
            value = 0

        data[col] = float(value)

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    if prediction == 0:
        result = "✅ Credit Card Approved"
    else:
        result = "❌ Credit Card Rejected"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)