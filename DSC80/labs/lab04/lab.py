# lab.py


import pandas as pd
import numpy as np
import io
from pathlib import Path
import os


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def prime_time_logins(login):
    login['Time'] = pd.to_datetime(login['Time'])
    return (login.groupby('Login Id')
            .apply(lambda df: df.query('16 <= Time.dt.hour < 20').shape[0], include_groups=False)
            .to_frame(name='Time'))


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def count_frequency(login):
    get_frequency = lambda df: df.shape[0] / max(1, max((pd.to_datetime("2024-01-31 23:59:00") - pd.to_datetime(df['Time'])).dt.days))
    return (login.groupby('Login Id')
            .apply(get_frequency, include_groups=False))


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def cookies_null_hypothesis():
    return [1, 2]
                         
def cookies_p_value(N):
    return float((np.random.binomial(n=250, p=0.04, size=N) >= 15).mean())


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def car_null_hypothesis():
    return [1, 4]

def car_alt_hypothesis():
    return [2, 6]

def car_test_statistic():
    return [1, 4]

def car_p_value():
    return 4


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def superheroes_test_statistic():
    return [1]
    
def bhbe_col(heroes):
    return (heroes['Hair color'].str.contains('blond', case=False, na=False) & 
            heroes['Eye color'].str.contains('blue', case=False, na=False))

def superheroes_observed_statistic(heroes):
    blue_blond = heroes[bhbe_col(heroes)]
    return blue_blond.query('Alignment == "good"').shape[0] / blue_blond.shape[0]

def simulate_bhbe_null(heroes, N):
    num_bhbe = bhbe_col(heroes).sum()
    prop_good = heroes.query('Alignment == "good"').shape[0] / heroes.shape[0]
    return np.random.binomial(n=num_bhbe, p=prop_good, size=N) / num_bhbe

def superheroes_p_value(heroes):
    p_val = (simulate_bhbe_null(heroes, 100_000) >= superheroes_observed_statistic(heroes)).mean()
    return [float(p_val), "Reject" if p_val <= 0.01 else "Fail to reject"]


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def diff_of_means(data, col='orange'):
    return abs(data.groupby('Factory')[col].mean().diff().iloc[-1])

def simulate_null(data, col='orange'):
    shuffled = data.copy()
    shuffled['Factory'] = np.random.permutation(data['Factory'])
    return diff_of_means(shuffled, col)

def color_p_value(data, col='orange'):
    observed = diff_of_means(data, col)
    tests = np.array([simulate_null(data, col) for _ in range(1000)])
    
    # plt.hist(tests, bins=20, color=col)
    # plt.axvline(x=observed, color='red')
    
    return (tests >= observed).mean()


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def ordered_colors():
    # return [(col, float(color_p_value(skittles, col))) for col in skittles.columns[:-1]] 
    return [('yellow', 0.0), ('orange', 0.056), ('red', 0.237), ('green', 0.479), ('purple', 0.986)]


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


    
def same_color_distribution():
    # def tvd(shuffled):
    #     counts = skittles.assign(Factory=shuffled).groupby('Factory').sum()
    #     dist = counts.apply(lambda x: x / counts.sum(axis=1)).T
    #     return (dist["Waco"] - dist["Yorkville"]).abs().sum() / 2
    
    # tests = [tvd(np.random.permutation(skittles.Factory.values)) for _ in range(1000)]
    # observed = tvd(skittles.Factory.values)
    # return (tests >= observed).mean()
    return (0.009, "Reject")


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def perm_vs_hyp():
    return ['P', 'P', 'H', 'H', 'P']