import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv(r'gender_classification_v7.csv')
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})

df_train, df_test = train_test_split(df, test_size=0.3, shuffle=False)
X_train = df_train.iloc[:, 0:7].values
y_train = df_train.iloc[:, 7].values
X_test = df_test.iloc[:, 0:7].values
y_test = df_test.iloc[:, 7].values

model = Perceptron(max_iter=1000, tol=0.01, penalty='l2')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Ti le du doan dung theo Perceptron:")
print('accuracy_score:', accuracy_score(y_test,y_pred))
print('precision_score:', precision_score(y_test,y_pred, average="micro"))
print('recall_score:', recall_score(y_test,y_pred, average="micro"))
print('f1_score:', f1_score(y_test,y_pred, average="micro"))
