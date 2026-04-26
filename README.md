# 📊 Customer Churn Prediction App

## 🚀 Project Overview
This project predicts whether a customer is likely to churn using Machine Learning.

## 🧠 Model Used
- Logistic Regression (with class balancing)
- Threshold tuning for better recall

## 📊 Features Used
- Tenure
- Monthly Charges
- Contract Type
- Internet Service

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

## 📊 Model Performance

- Accuracy: ~75%
- Recall (Churn): ~0.90 (after threshold tuning)
- Business Focus: Minimize customer loss (False Negatives)

## ⚖️ Key Insight

Reducing false negatives is more important than overall accuracy because missing a churn customer leads to direct business loss.

## 🔍 Threshold Tuning

Custom threshold (0.4) was used instead of default 0.5 to improve recall.

## 📸 App Preview

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/45ec4c04-8227-412c-9242-ac1090915fc7" />


## 🖥️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
