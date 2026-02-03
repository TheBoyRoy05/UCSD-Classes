from collections import defaultdict
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import numpy as np


### Question 1
def getMaxLen(dataset):
    return max(len(d["review_text"]) for d in dataset)


def featureQ1(datum, maxLen):
    return [1, len(datum["review_text"]) / maxLen]


def Q1(dataset):
    X = [featureQ1(d, getMaxLen(dataset)) for d in dataset]
    Y = [d["rating"] for d in dataset]
    model = LinearRegression(fit_intercept=False)
    model.fit(X, Y)

    mse = mean_squared_error(Y, model.predict(X))
    return model.coef_, float(mse)


### Question 2
def featureQ2(datum, maxLen):
    weekday = datum["parsed_date"].weekday()
    weekday_features = [1 if i == weekday else 0 for i in range(7)]
    
    month = datum["parsed_date"].month
    month_features = [1 if i == month else 0 for i in range(1, 13)]
    
    return [
        1,
        len(datum["review_text"]) / maxLen,
    ] + weekday_features[1:] + month_features[1:]


def Q2(dataset):
    X = [featureQ2(d, getMaxLen(dataset)) for d in dataset]
    Y = [d["rating"] for d in dataset]

    model = LinearRegression(fit_intercept=False)
    model.fit(X, Y)
    mse = mean_squared_error(Y, model.predict(X))
    return X, Y, float(mse)


### Question 3
def featureQ3(datum, maxLen):
    return [
        1,
        len(datum["review_text"]) / maxLen,
        datum["parsed_date"].weekday(),
        datum["parsed_date"].month,
    ]


def Q3(dataset):
    X = [featureQ3(d, getMaxLen(dataset)) for d in dataset]
    Y = [d["rating"] for d in dataset]

    model = LinearRegression(fit_intercept=False)
    model.fit(X, Y)
    mse = mean_squared_error(Y, model.predict(X))
    return X, Y, float(mse)


### Question 4
def Q4(dataset):
    X2 = [featureQ2(d, getMaxLen(dataset)) for d in dataset]
    Y2 = [d["rating"] for d in dataset]

    model2 = LinearRegression(fit_intercept=False)
    model2.fit(X2[:len(X2)//2], Y2[:len(Y2)//2])
    test_mse2 = mean_squared_error(Y2[len(Y2)//2:], model2.predict(X2[len(X2)//2:]))

    X3 = [featureQ3(d, getMaxLen(dataset)) for d in dataset]
    Y3 = [d["rating"] for d in dataset]

    model3 = LinearRegression(fit_intercept=False)
    model3.fit(X3[:len(X3)//2], Y3[:len(Y3)//2])
    test_mse3 = mean_squared_error(Y3[len(Y3)//2:], model3.predict(X3[len(X3)//2:]))
    return test_mse2, test_mse3


### Question 5
def featureQ5(datum):
    return [1, len(datum["review/text"])]


def Q5(dataset, feat_func):
    X = [feat_func(d) for d in dataset]
    Y = [int(d["review/overall"] >= 4) for d in dataset]

    model = LogisticRegression(class_weight="balanced")
    model.fit(X, Y)
    y_pred = model.predict(X)
    TP = sum(y_pred[i] == 1 and Y[i] == 1 for i in range(len(Y)))
    TN = sum(y_pred[i] == 0 and Y[i] == 0 for i in range(len(Y)))
    FP = sum(y_pred[i] == 1 and Y[i] == 0 for i in range(len(Y)))
    FN = sum(y_pred[i] == 0 and Y[i] == 1 for i in range(len(Y)))
    BER = 0.5 * (FP / (FP + TN) + FN / (FN + TP))

    return TP, TN, FP, FN, BER


### Question 6
def Q6(dataset):
    X = [featureQ5(d) for d in dataset]
    Y = [int(d["review/overall"] >= 4) for d in dataset]

    model = LogisticRegression(class_weight="balanced").fit(X, Y)
    pred_idx = np.argsort(model.predict_proba(X)[:, 1])[::-1]

    Ks = [1, 100, 1000, 10000]
    precs = [np.sum([Y[i] for i in pred_idx[:k]]) / k for k in Ks]

    return precs


### Question 7
def featureQ7(datum):
    return [
        1,
        datum["review/appearance"],
        len(datum["review/text"]),
    ]
