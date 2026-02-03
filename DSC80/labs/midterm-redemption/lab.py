# lab.py


import pandas as pd
import numpy as np
import sys
import os
from dsc80_utils import *



# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def amina_function():
    # Your solution should use at least one of these dataframes
    parks = pd.read_csv('data/parks.csv')
    visits = pd.read_csv('data/visits.csv', parse_dates=['entry'])
    df1 = parks.merge(visits, on='park_id', how='inner')
    df2 = parks.merge(visits, on='park_id', how='left')

    return visits[visits['name'] == 'Amina Garcia'].shape[0]


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def least_function():
    # Your solution should use at least one of these dataframes
    parks = pd.read_csv('data/parks.csv')
    visits = pd.read_csv('data/visits.csv', parse_dates=['entry'])
    df1 = parks.merge(visits, on='park_id', how='inner')
    df2 = parks.merge(visits, on='park_id', how='left')
    
    temp = visits.copy()
    temp['year'] = visits['entry'].dt.year
    return temp.groupby('year').size().idxmin()


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def never_function():
    # Your solution should use at least one of these dataframes
    parks = pd.read_csv('data/parks.csv')
    visits = pd.read_csv('data/visits.csv', parse_dates=['entry'])
    df1 = parks.merge(visits, on='park_id', how='inner')
    df2 = parks.merge(visits, on='park_id', how='left')
    
    return df2[df2['name'].isna()]['parkname'].unique()


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def prop_missing_function():
    df = pd.read_csv('data/visits_missing_a.csv')
    return df['duration'].isna().mean()


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


np.random.seed(42)
df = pd.read_csv('data/visits_missing_a.csv')
with_2020 = df.assign(is_2020=df['entry_year'] == 2020)
stats, obs = permutation_test(with_2020, 'entry_hour', 'is_2020', tvd)

def p_val_function():
    return (stats >= obs).mean()

def reject_function():
    return bool(p_val_function() <= 0.01)



# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def hour_pval_function():
    df = pd.read_csv('data/visits_missing_a.csv')
    has_duration = df.assign(has_duration=df['duration'].notna())
    stats, obs = permutation_test(has_duration, 'entry_hour', 'has_duration', tvd)
    return (stats >= obs).mean()

def hour_mar_function():
    return bool(hour_pval_function() <= 0.01)


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


np.random.seed(42)
def pvals_function():
    result = {}
    has_duration = df.assign(has_duration=df['duration'].notna())
    for col in ['region', 'entry_month', 'entry_year']:
        stats, obs = permutation_test(has_duration, col, 'has_duration', tvd)
        result[col] = (stats >= obs).mean()

    return result
    
def mar_cols_function():
    return {col: bool(val <= 0.01) for col, val in pvals_function().items()}
    


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def prob_impute(s):
    s = s.copy()
    num_null = s.isna().sum()
    fill_values = np.random.choice(s.dropna(), num_null)
    s[s.isna()] = fill_values
    return s

def df_imputed_function():
    mar_cols = [col for col, val in mar_cols_function().items() if val]
    return df.assign(imputed=df.groupby(mar_cols, as_index=False)['duration'].transform(prob_impute))