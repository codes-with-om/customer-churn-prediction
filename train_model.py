import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# load dataset
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# basic cleaning
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# target
df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})

# select only needed features
df = df[['tenure', 'MonthlyCharges', 'Contract', 'InternetService', 'Churn']]

# encoding
df = pd.get_dummies(df, drop_first=True)

# split
X = df.drop('Churn', axis=1)
y = df['Churn']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# model
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# save
joblib.dump(model, 'churn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model retrained & saved successfully!")