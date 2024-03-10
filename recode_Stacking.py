import numpy as np

class Stacking:
    def fit(self, model1,model2,model3, X,y):
        model1.fit(X, y)
        model2.fit(X, y)
        model3.fit(X,y)

    def predict(self, model1,model2, model3, X_test):
        y_pred1 = model1.predict(X_test)
        y_pred2 = model2.predict(X_test)
        y_pred3 = model3.predict(X_test)

        y_pred = (y_pred1 + y_pred2 + y_pred3) >= 2
        y_pred = np.where(y_pred, 1, 0)
        return y_pred