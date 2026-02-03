# lab.py


import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def simple_pipeline(data):
    pipeline = Pipeline([
        ('log_scaler', FunctionTransformer(func=np.log, validate=True)),
        ('regressor', LinearRegression())
    ])
    
    X = data[['c2']]
    y = data['y']
    pipeline.fit(X, y)
    
    return pipeline, pipeline.predict(X)

# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def multi_type_pipeline(data):
    preprocessor = ColumnTransformer([
        ('c1_pass', 'passthrough', ['c1']),
        ('c2_log', FunctionTransformer(func=np.log1p, validate=True), ['c2']),
        ('group_ohe', OneHotEncoder(sparse_output=False), ['group'])
    ])
    
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    
    X = data[['c1', 'c2', 'group']]
    y = data['y']
    pipeline.fit(X, y)
    
    return pipeline, pipeline.predict(X)


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


# Imports
from sklearn.base import BaseEstimator, TransformerMixin

class StdScalerByGroup(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        df = pd.DataFrame(X)
        self.grps_ = df.groupby(df.columns[0])[df.columns[1:]].agg(['mean', 'std'])
        return self

    def transform(self, X, y=None):
        try:
            getattr(self, "grps_")
        except AttributeError:
            raise RuntimeError("You must fit the transformer before tranforming the data!")

        def standarize_subframe(df):
            return df[df.columns[1:]].transform(lambda col: standarize_col(df.name, col))

        def standarize_col(group, col):
            mean = self.grps_.loc[group, (col.name, 'mean')]
            std = self.grps_.loc[group, (col.name, 'std')]
            return (col - mean) / std

        df = pd.DataFrame(X)
        return df.groupby(df.columns[0]).apply(standarize_subframe)


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def eval_toy_model():
    return [
        (2.755108697451811, 0.39558507345910754),
        (2.3192028254180315, 0.5717127276647056),
        (2.3552456238924657, 0.558297236308609),
    ]


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def reg_perf(galton, Model, param):
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split
    
    X = galton.drop(columns=['childHeight'])
    y = galton['childHeight']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    rmse = lambda y, y_pred: np.sqrt(mean_squared_error(y, y_pred))
    
    results = []
    for i in range(1, 21):
        model = Model(**{param: i})
        model.fit(X_train, y_train)
        train_err = rmse(y_train, model.predict(X_train))
        test_err = rmse(y_test, model.predict(X_test))
        results.append((train_err, test_err))
        
    return pd.DataFrame(results, columns=['train_err', 'test_err'], index=range(1, 21))

def tree_reg_perf(galton):
    from sklearn.tree import DecisionTreeRegressor
    return reg_perf(galton, DecisionTreeRegressor, 'max_depth')

def knn_reg_perf(galton):
    from sklearn.neighbors import KNeighborsRegressor
    return reg_perf(galton, KNeighborsRegressor, 'n_neighbors')


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def titanic_model(titanic):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, StandardScaler
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import make_scorer, accuracy_score

    title = lambda name: name.str.extract(r" ([A-Za-z]+)\.")[0]
    extract_title = lambda df: df[["Name"]].apply(title)
    title_transformer = FunctionTransformer(extract_title, validate=False)

    preprocessor = ColumnTransformer(
        [
            ("title", title_transformer, ["Name"]),
            ("categorical", OneHotEncoder(), ["Sex"]),
            ("std_age", StdScalerByGroup(), ["Pclass", "Age"]),
            ("fare", StandardScaler(), ["Fare"]),
            ("passthrough", "passthrough", ["Pclass"]),
        ],
        remainder="drop",
    )

    classifier = RandomForestClassifier(max_depth=6, n_estimators=38, random_state=42)
    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("classifier", classifier),
        ]
    )

    # param_grid = {
    #     "classifier__max_depth": range(1, 11),
    #     "classifier__n_estimators": range(30, 50),
    # }

    # X = titanic.drop(columns=["Survived"])
    # y = titanic["Survived"]

    # grid_search = GridSearchCV(
    #     estimator=pipeline,
    #     param_grid=param_grid,
    #     cv=5,
    #     scoring=make_scorer(accuracy_score),
    #     n_jobs=-1,
    #     verbose=1,
    # )

    # grid_search.fit(X, y)
    # return (
    #     grid_search.best_estimator_,
    #     grid_search.best_params_,
    #     grid_search.best_score_,
    # )
    
    X = titanic.drop(columns=['Survived'])
    y = titanic['Survived']
    pipeline.fit(X, y)
    return pipeline