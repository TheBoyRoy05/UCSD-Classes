# lab.py


import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm
from itertools import combinations
from pathlib import Path
from sklearn.preprocessing import Binarizer, QuantileTransformer, FunctionTransformer

import warnings
warnings.filterwarnings('ignore')


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def best_transformation():
    return 1


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------



def create_ordinal(df):
    cut_map = {'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4}
    color_map = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
    clarity_map = {'I1': 0, 'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}

    return pd.DataFrame({
        'ordinal_cut': df['cut'].map(cut_map),
        'ordinal_color': df['color'].map(color_map),
        'ordinal_clarity': df['clarity'].map(clarity_map)
    })


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------



def create_one_hot(df):
    return pd.DataFrame({f'one_hot_{col}_{val}': (df[col] == val).astype(int) for col in ['cut', 'color', 'clarity'] for val in df[col].unique()})

def create_proportions(df):
    return pd.DataFrame({f'proportion_{col}': df[col].map(df[col].value_counts(normalize=True)) for col in ['cut', 'color', 'clarity']})


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def create_quadratics(df):
    return pd.DataFrame({f'{col1} * {col2}': (df[col1] * df[col2]) for col1, col2 in combinations(df.columns.drop(['price', 'cut', 'color', 'clarity']), 2)})


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------



def comparing_performance():
    return [0.8493305264354858, 1548.5331930613174, 'x', 'carat * x', 'ordinal_color', 1434.8400089047327]


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


class TransformDiamonds(object):
    
    def __init__(self, diamonds):
        self.data = diamonds
        
    # Question 6.1
    def transform_carat(self, data):
        return Binarizer(threshold=1).fit_transform(data[['carat']])
    
    # Question 6.2
    def transform_to_quantile(self, data):
        tranformer = QuantileTransformer(n_quantiles=100).fit(self.data[['carat']])
        return tranformer.transform(data[['carat']])
    
    # Question 6.3
    def transform_to_depth_pct(self, data):
        transformer = FunctionTransformer(lambda row: 200 * row['z'] / (row['x'] + row['y']))
        return transformer.fit_transform(data[['x', 'y', 'z']])