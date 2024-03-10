import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from DecisionTree import DecisionTree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from gui import create_main_window
from recode_Stacking import Stacking

df = pd.read_csv(r'gender_classification_v7.csv')
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})

df_train, df_test = train_test_split(df, test_size=0.3, shuffle=False)
X_train = df_train.iloc[:, 0:7].values
y_train = df_train.iloc[:, 7].values
X_test = df_test.iloc[:, 0:7].values
y_test = df_test.iloc[:, 7].values

stacking = Stacking()
model1 = Perceptron(max_iter=1000, tol=0.01, penalty='l2')
model2 = MLPClassifier(hidden_layer_sizes=(75,25,10),activation='relu',max_iter=5000,alpha=0.01,solver='adam',random_state=21,tol=0.00001)
model3 = DecisionTree(max_depth=6)
stacking.fit(model1, model2, model3, X_train, y_train)

y_pred = stacking.predict(model1, model2, model3,X_test)

accuracy_score = accuracy_score(y_test,y_pred)
precision_score = precision_score(y_test,y_pred, average="micro")
recall_score = recall_score(y_test,y_pred, average="micro")
f1_score = f1_score(y_test,y_pred, average="micro")

create_main_window(accuracy_score, precision_score, recall_score, f1_score, model1, model2, model3)
