# 💳 Credit Card Approval Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a credit card application will be **approved** or **rejected** using Machine Learning algorithms. The system analyzes applicant information such as income, age, family members, employment years, and other financial details to make predictions.

The best-performing model is integrated into a **Flask web application**, allowing users to enter applicant details and receive an instant prediction.

---

## 📸 Application Screenshots

### 🏠 Home Page

![Home Page](images/home.png)

---

### ✅ Prediction Result

![Prediction Result](images/prediction.png)

---

## 🚀 Features

- Data Collection and Analysis
- Data Preprocessing
- Feature Engineering
- Multiple Machine Learning Models
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Model Comparison
- Flask Web Application
- User-friendly HTML & CSS Interface
- Instant Credit Card Approval Prediction

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- HTML
- CSS
- Joblib
- Jupyter Notebook

---

## 📂 Project Structure

```text
Credit-Card-Approval-Prediction
│
├── images
│   ├── home.png
│   └── prediction.png
│
├── static
│   └── style.css
│
├── templates
│   └── index.html
│
├── .gitignore
├── Credit_Card_Approval.ipynb
├── app.py
├── credit_record.csv
├── feature_columns.pkl
├── README.md
└── requirements.txt
```

> **Note:** The original training dataset `application_record.csv` is not included in this repository because it exceeds GitHub's web upload size limit (25 MB). The model was trained using both `application_record.csv` and `credit_record.csv`.

---

## 🤖 Machine Learning Models

The following Machine Learning algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The best-performing model was saved and integrated into the Flask web application for prediction.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sowmyaperike/Credit-Card-Approval-Prediction.git
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Flask application

```bash
python app.py
```

### 4. Open your browser

Visit:

```text
http://127.0.0.1:5000
```

### 5. Predict

Enter the applicant details and click **Predict** to view the credit card approval result.

---

## 📈 Future Improvements

- Deploy the application to the cloud
- Improve the user interface
- Develop a REST API for predictions
- Add more features for better accuracy
- Optimize the Machine Learning model

---

## 👥 Team

- **Sowmya Perike** *(Team Lead)*
- **Pravallika Sri Modugumudi**
- **R N V Sai Ramya**
- **Manga Doddi Chaitanya**
- **Kraanthi Kunasani**

---

## 📜 License

This project was developed for educational purposes as part of the **SkillWallet Artificial Intelligence and Machine Learning Program**.