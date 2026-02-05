# lab.py


import os
import io
from pathlib import Path
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def trick_me():
    return 3


def trick_bool():
    return [4, 10, 13]


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def population_stats(df):
    return pd.DataFrame({
        'num_nonnull': df.notnull().sum(),
        'prop_nonnull': df.notnull().sum() / df.shape[0],
        'num_distinct': df.nunique(dropna=True),
        'prop_distinct': df.nunique(dropna=True) / df.shape[0]
    })


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def most_common(df, N=10):
    result = pd.DataFrame(index=range(N))
    for col in df.columns:
        top = df[col].value_counts().iloc[:N]
        
        if len(top) < N:
            nans = [np.nan] * (N - len(top))
            top = pd.concat([top, pd.Series(nans, index=nans)])
            
        result = result.assign(**{f'{col}_values': top.index, f'{col}_counts': top.values})
        
    return result


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def super_hero_powers(powers):
    powers = powers.set_index("hero_names")
    return [
        powers.sum(axis=1).sort_values().index[-1],
        powers[powers["Flight"]].sum().sort_values().index[-2],
        powers[powers.sum(axis=1) == 1].sum().sort_values().index[-1]
    ]


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def clean_heroes(heroes):
    return heroes.replace("-", np.nan).replace(-99, np.nan)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def super_hero_stats():
    return [
        "Onslaught",
        "George Lucas",
        "bad",
        "Marvel Comics",
        "NBC - Heroes",
        "Groot"
    ]


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def clean_universities(df):
    get_nation = lambda rank: (rank.split(", ")[0]
                                 .replace("USA", "United States")
                                 .replace("UK", "United Kingdom")
                                 .replace("Czechia", "Czech Republic"))
    
    df = df.assign(institution=df["institution"].replace('\n',', ', regex=True), 
                   broad_impact=df["broad_impact"].apply(lambda x: int(x)),
                   nation=df["national_rank"].apply(get_nation),
                   national_rank_cleaned=df["national_rank"].apply(lambda x: int(x.split(", ")[1])),
                   is_r1_public=(df["control"] == "Public"))
    
    return df.drop("national_rank", axis=1)

def university_info(cleaned):
    return [
        (cleaned.groupby("state")
         .agg(size=("state", "size"), mean_score=("score", "mean"))
         .query('size >= 3')
         .sort_values(by="mean_score")
         .index[0]),
        (cleaned.iloc[:100].query('quality_of_faculty <= 100').shape[0] / 100),
        (cleaned.groupby('state').agg(prop_public=("is_r1_public", "mean"))
         .query('prop_public < 0.5')
         .shape[0]),
        (cleaned.query('national_rank_cleaned == 1').iloc[-1]["institution"])
    ]

