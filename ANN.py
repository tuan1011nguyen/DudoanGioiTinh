import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv(r'gender_classification_v7.csv')
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})

df_train, df_test = train_test_split(df, test_size=0.3, shuffle=False)
X_train = df_train.iloc[:, 0:7].values
y_train = df_train.iloc[:, 7].values
X_test = df_test.iloc[:, 0:7].values
y_test = df_test.iloc[:, 7].values

# Gọi mô hình với chỉ số phù hợp cho bài toán
model = MLPClassifier(hidden_layer_sizes=(75,25,10),activation='relu',max_iter=5000,alpha=0.01,solver='adam',random_state=21,tol=0.00001)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Kết quả chạy mô hình
print("Ti le du doan dung theo NeuralNetworks:")
print('accuracy_score:', accuracy_score(y_test,y_pred))
print('precision_score:', precision_score(y_test,y_pred, average="micro"))
print('recall_score:', recall_score(y_test,y_pred, average="micro"))
print('f1_score:', f1_score(y_test,y_pred, average="micro"))
