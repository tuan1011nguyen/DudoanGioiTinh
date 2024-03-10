import pandas as pd
from sklearn.model_selection import train_test_split
from DecisionTree import DecisionTree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from gui import create_id3_window
# Đọc dữ liệu từ file CSV
df = pd.read_csv('gender_classification_v7.csv')
selected_columns = ['long_hair', 'forehead_width_cm', 'forehead_height_cm',
                         'nose_wide', 'nose_long', 'lips_thin',
                         'distance_nose_to_lip_long', 'gender']
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})
data = df[selected_columns]

X = data.drop("gender", axis=1).values
y = data["gender"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
clf = DecisionTree(max_depth=6)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy_score = accuracy_score(y_test,y_pred)
precision_score = precision_score(y_test,y_pred, average="micro")
recall_score = recall_score(y_test,y_pred, average="micro")
f1_score = f1_score(y_test,y_pred, average="micro")

create_id3_window(accuracy_score, precision_score, recall_score, f1_score, clf)