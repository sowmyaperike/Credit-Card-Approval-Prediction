# 💳 Credit Card Approval Prediction using Machine Learning

A Machine Learning-based web application that predicts whether a credit card application is likely to be **Approved** or **Rejected** based on an applicant's financial and demographic information.

Built using **Python, Flask, Scikit-learn, XGBoost, HTML, and CSS**.

---

## 📖 Project Overview

Banks receive thousands of credit card applications every day. Reviewing each application manually is time-consuming and prone to human error.

This project automates the credit card approval process using Machine Learning. The model analyzes applicant information such as income, employment details, family status, education, housing, and credit history to predict whether a credit card application should be approved.

The trained model is integrated with a Flask web application that provides an easy-to-use interface for real-time predictions.

---

## ✨ Features

- 📊 Data preprocessing and cleaning
- 📈 Exploratory Data Analysis (EDA)
- 🔧 Feature Engineering
- 🤖 Multiple Machine Learning models
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - XGBoost
- 🏆 Best model selection based on performance
- 🌐 Flask Web Application
- 🎨 Responsive HTML & CSS interface
- ⚡ Instant credit card approval prediction

---

## 🖼️ Application Screenshots

### 🏠 Home Page

![Home Page](images/home.png)

---

### 📋 Prediction Page

![Prediction Page](images/prediction.png)

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- XGBoost

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Web Framework
- Flask

### Frontend
- HTML
- CSS

### Model Serialization
- Pickle
- Joblib

### Development Tools
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

```text
Credit-Card-Approval-Prediction
│
├── dataset/
│   └── credit_record.csv
│
├── images/
│   ├── home.png
│   └── prediction.png
│
├── models/
│   └── feature_columns.pkl
│
├── notebooks/
│   └── Credit_Card_Approval.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── prediction.html
│   └── result.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🤖 Machine Learning Models

The following supervised learning algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

After comparing model performance, the best-performing model was selected and integrated into the Flask application.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sowmyaperike/Credit-Card-Approval-Prediction.git
```

### 2️⃣ Navigate to the Project

```bash
cd Credit-Card-Approval-Prediction
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 Dataset

The project is based on the Credit Card Approval dataset containing applicant information and historical credit records.

**Dataset Files**

- application_record.csv
- credit_record.csv

> **Note:** The original `application_record.csv` dataset and the trained model file are not included in this repository because they exceed GitHub's file size limit. They were used during model training and testing.

---

## 📈 Future Improvements

- ☁️ Deploy the application to the cloud
- 🤖 Improve model accuracy
- 📱 Make the interface fully responsive
- 🔐 Add user authentication
- 📊 Add model performance dashboard
- 🌍 Deploy using Render or Railway
- 🔗 Create REST API endpoints

---

## 👥 Team Members

| Name | Role |
|------|------|
| **Sowmya Perike** | Team Lead |
| **Pravallika Sri Modugumudi** | Team Member |
| **R N V Sai Ramya Tadepalli** | Team Member |
| **Manga Doddi Chaitanya** | Team Member |
| **Kraanthi Kunasani** | Team Member |

---

## 🙏 Acknowledgements

This project was developed as part of the **SkillWallet Artificial Intelligence and Machine Learning Program**.

Special thanks to the mentors and contributors who supported the successful completion of this project.

---

## 📄 License

This project is intended for **educational and learning purposes**.

---

## ⭐ If you like this project

If you found this project helpful, consider giving it a ⭐ on GitHub.
