# lab.py


import os
import io
from pathlib import Path
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def read_linkedin_survey(dirname):
    responses = Path(dirname)
    surveys = pd.DataFrame()
    
    if not responses.is_dir(): raise FileNotFoundError(f"Directory {dirname} not found!")
    
    for survey_path in responses.iterdir():
        if survey_path.suffix != '.csv': continue
        
        survey = pd.read_csv(survey_path)
        cols = ['first name', 'last name', 'current company', 'job title', 'email', 'university']
        
        for col in cols:
            old_col = [old_col for old_col in survey.columns if col.split()[0] in old_col.lower()][0]
            survey[col] = survey[old_col]
            
        surveys = pd.concat([surveys, survey[cols]], ignore_index=True)
    return surveys

def com_stats(df):
    ohio = df["university"].str.contains("Ohio", na=False)
    programmer = df["job title"].str.contains("Programmer", na=False)
    
    return [
        len(df[ohio & programmer]) / ohio.sum() if ohio.sum() else 0,
        df[df["job title"].str.endswith("Engineer", na=False)]["job title"].nunique(),
        df.iloc[df['job title'].dropna().map(len).idxmax()]["job title"],
        df[df["job title"].str.contains("manager", case=False, na=False)].shape[0]
    ]


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def read_student_surveys(dirname):
    responses = Path(dirname)
    survey = pd.DataFrame({"id": np.arange(1000) + 1})
    if not responses.is_dir(): raise FileNotFoundError(f"Directory {dirname} not found!")
    
    for survey_path in responses.iterdir():
        if survey_path.suffix != '.csv': continue
        survey = survey.merge(pd.read_csv(survey_path), on='id')
        
    return survey.set_index('id')

def check_credit(df):
    responses = df.drop(columns='name').replace('(no genres listed)', np.nan)
    self_ec = (responses.notna().sum(axis=1) >= len(responses.columns) / 2) * 5
    class_ec = min((responses.notna().sum() >= 0.9 * df.shape[0]).sum(), 2)
    return df.assign(ec=self_ec + class_ec)[['name', 'ec']]


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def most_popular_procedure(pets, procedure_history):
    return pets.merge(procedure_history, on="PetID")["ProcedureType"].value_counts().index[0]

def pet_name_by_owner(owners, pets):
    merged = owners.rename(columns={"Name": "First Name"}).merge(pets, on='OwnerID', how='left')
    names = merged.groupby("OwnerID")[["First Name", "Name"]].agg(list)
    format_petname = lambda x: x if len(x) > 1 else x[0]
    return names.set_index(names["First Name"].apply(lambda x: x[0]))["Name"].apply(format_petname)

def total_cost_per_city(owners, pets, procedure_history, procedure_detail):
    return (owners.merge(pets, on="OwnerID")
            .merge(procedure_history, on="PetID", how="left")
            .merge(procedure_detail, on=["ProcedureSubCode", "ProcedureType"], how="left")
            .replace({"Price": np.nan}, {"Price": 0})
            .groupby("City")["Price"]
            .sum())


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def average_seller(sales):
    df = pd.DataFrame(sales.groupby("Name")["Total"].mean())
    return df.rename(columns={"Total": "Average Sales"})

def product_name(sales):
    return sales.pivot_table(index="Name", columns="Product", values="Total", aggfunc="sum")

def count_product(sales):
    pivot = sales.pivot_table(index=["Product", "Name"], 
                              columns="Date", 
                              values="Total", 
                              aggfunc="count")
    return pivot.replace(np.nan, 0)

def total_by_month(sales):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    sales["Month"] = sales["Date"].apply(lambda x: months[int(x[:2]) - 1])
    
    pivot = sales.pivot_table(index=["Name", "Product"], 
                              columns="Month", 
                              values="Total", 
                              aggfunc="sum")
    return pivot.replace(np.nan, 0)