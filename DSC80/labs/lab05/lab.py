# lab.py


from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def after_purchase():
    return ['NMAR', 'MD', 'MAR', 'NMAR', 'MAR']

# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def multiple_choice():
    return ['MAR', 'MAR', 'MD', 'NMAR', 'MCAR']


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------



def first_round():
    # def test_stat(df):
    #     return np.abs(df[df['credit_card_number'].notna()]['age'].mean() - 
    #                   df[df['credit_card_number'].isna()]['age'].mean())
    
    # payments['age'] = 2024 - pd.to_datetime(payments['date_of_birth']).dt.year
    # observed = test_stat(payments)
    
    # diffs = np.array([])
    # for _ in range(1000):
    #     shuffled = payments.copy()
    #     shuffled['credit_card_number'] = np.random.permutation(shuffled['credit_card_number'])
    #     diffs = np.append(diffs, test_stat(shuffled))
    
    # pval = (diffs >= observed).mean()
    return [0.172, 'NR']

def second_round():
    # payments['age'] = 2024 - pd.to_datetime(payments['date_of_birth']).dt.year
    # notNaAges = payments[payments['credit_card_number'].notna()]['age'].dropna()
    # naAges = payments[payments['credit_card_number'].isna()]['age'].dropna()
    # p_val = stats.ks_2samp(notNaAges, naAges).pvalue
    
    return [0.023496, 'R', 'D']

# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def verify_child(heights):
    p_values = {}
    for col in heights.columns:
        if not col.startswith('child_'): continue
        
        father_with_data = heights['father'][heights[col].notna()]
        father_without_data = heights['father'][heights[col].isna()]
        p_values[col] = stats.ks_2samp(father_with_data, father_without_data).pvalue
            
    return pd.Series(p_values)


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def cond_single_imputation(new_heights):
    new_heights['father_quartile'] = pd.qcut(new_heights['father'], 4)
    return new_heights.groupby('father_quartile')['child'].transform(lambda x: x.fillna(x.mean()))


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def quantitative_distribution(child, N):
    hist = np.histogram(child, bins=np.linspace(child.min(), child.max(), 11))
    props = hist[0] / len(child.dropna())
    choices = np.random.choice(np.arange(10), p=props, size=N)
    return np.array([np.random.uniform(hist[1][choice], hist[1][choice+1]) for choice in choices])

def impute_height_quant(child):
    vals = quantitative_distribution(child, child.isna().sum())
    child[child.isna()] = vals
    return child


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def answers():
    return [1, 2, 2, 1], ['whitehouse.gov', 'netflix.com']
