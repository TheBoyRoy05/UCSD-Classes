# project.py


import pandas as pd
import numpy as np
from pathlib import Path

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pd.options.plotting.backend = 'plotly'

from IPython.display import display

# DSC 80 preferred styles
pio.templates["dsc80"] = go.layout.Template(
    layout=dict(
        margin=dict(l=30, r=30, t=30, b=30),
        autosize=True,
        width=600,
        height=400,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        title=dict(x=0.5, xanchor="center"),
    )
)
pio.templates.default = "simple_white+dsc80"
import warnings
warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def clean_loans(loans):
    result = loans.assign(issue_d=pd.to_datetime(loans['issue_d']))
    result['term'] = loans['term'].str.extract('(\d+)').astype(int)
    result['emp_title'] = loans['emp_title'].str.lower().str.strip()
    result['emp_title'] = result['emp_title'].apply(lambda x: 'registered nurse' if x == 'rn' else x)
    result['term_end'] = result['issue_d'] + result['term'].apply(lambda x: pd.DateOffset(months=x))
    return result


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------



def correlations(df, pairs):
    return pd.Series({f'r_{x}_{y}': df[x].corr(df[y]) for x, y in pairs})



# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def create_boxplot(loans):
    bins = [580, 670, 740, 800, 850]
    labels = ['[580, 670)', '[670, 740)', '[740, 800)', '[800, 850)']
    loans['fico_bin'] = pd.cut(loans['fico_range_low'], bins=bins, labels=labels, right=False)
    
    fig = px.box(loans.sort_values('fico_bin'), x='fico_bin', y='int_rate', color='term',
                 labels={'fico_bin': 'Credit Score Range', 'int_rate': 'Interest Rate (%)'},
                 title='Interest Rate vs. Credit Score',
                 color_discrete_map={36: 'purple', 60: 'gold'})
    
    fig.update_layout(legend_title_text='Loan Length (Months)')
    return fig


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def ps_test(loans, N):
    diff = loans[loans['desc'].notna()]["int_rate"].mean() - loans[loans['desc'].isna()]["int_rate"].mean()
    all_rates = loans['int_rate'].values
    labels = loans['desc'].notna().values
    emp_diffs = np.array([])
    
    for _ in range(N):
        shuffled = np.random.permutation(labels)
        with_ps = all_rates[shuffled == True]
        without_ps = all_rates[shuffled == False]
        emp_diffs = np.append(emp_diffs, with_ps.mean() - without_ps.mean())
        
    return (emp_diffs >= diff).mean()
    
def missingness_mechanism():
    return 2
    
def argument_for_nmar():
    return '''It could be that personal statements are not missing at random (NMAR) because people might not include them if they are confident of their credit scores, incomes, and other measures to get the loan. That is, it could be that people who tend to include personal statements are less likely to have good credit scores, incomes, etc. and are thus less likely to get the loan.'''


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def tax_owed(income, brackets):
    total = 0
    for i, (rate, low) in enumerate(brackets):
        high = float('inf') if i == len(brackets) - 1 else brackets[i + 1][1]
        tax = rate * (min(income, high) - low)
        if tax >= 0: total += tax
        else: break
    return total


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def clean_state_taxes(state_taxes_raw):
    clean_state = lambda x: np.nan if isinstance(x, str) and '(' in x else x
    
    df = state_taxes_raw.dropna(how='all')
    df['State'] = df['State'].apply(clean_state).fillna(method='ffill')
    df['Rate'] = (df['Rate'].replace('none', '0').str.rstrip('%').astype(float) / 100).round(2)
    df['Lower Limit'] = df['Lower Limit'].str.replace('$', '').str.replace(',', '').fillna(0).astype(int)
    return df


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def state_brackets(state_taxes):
    create_brackets = lambda df: list(zip(df['Rate'], df['Lower Limit']))
    return (pd.DataFrame(state_taxes.groupby('State').apply(create_brackets))
            .rename(columns={0: 'bracket_list'}))
    
def combine_loans_and_state_taxes(loans, state_taxes):
    # Start by loading in the JSON file.
    # state_mapping is a dictionary; use it!
    import json
    state_mapping_path = Path('data') / 'state_mapping.json'
    with open(state_mapping_path, 'r') as f:
        state_mapping = json.load(f)
        
    # Now it's your turn:
    brackets = state_brackets(state_taxes.assign(State=state_taxes['State'].map(state_mapping)))
    return (loans.merge(brackets.reset_index(), left_on='addr_state', right_on='State')
            .drop('addr_state', axis=1))


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def find_disposable_income(loans_with_state_taxes):
    FEDERAL_BRACKETS = [
     (0.1, 0), 
     (0.12, 11000), 
     (0.22, 44725), 
     (0.24, 95375), 
     (0.32, 182100),
     (0.35, 231251),
     (0.37, 578125)
    ]
    
    calc_fed_tax = lambda row: tax_owed(row['annual_inc'], FEDERAL_BRACKETS)
    calc_state_tax = lambda row: tax_owed(row['annual_inc'], row['bracket_list'])
    calc_disp_inc = lambda row: row['annual_inc'] - row['federal_tax_owed'] - row['state_tax_owed']
    
    with_taxes = loans_with_state_taxes.assign(
        federal_tax_owed=loans_with_state_taxes.apply(calc_fed_tax, axis=1),
        state_tax_owed=loans_with_state_taxes.apply(calc_state_tax, axis=1)
    )
    
    return with_taxes.assign(disposable_income=with_taxes.apply(calc_disp_inc, axis=1))


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def aggregate_and_combine(loans, keywords, quantitative_column, categorical_column):
    result = {}
    for keyword in keywords:
        contains_keyword = loans[loans['emp_title'].str.contains(keyword)]
        category_means = contains_keyword.groupby(categorical_column)[quantitative_column].mean()
        overall_mean = contains_keyword[quantitative_column].mean()
        means = pd.concat([category_means, pd.Series({'Overall': overall_mean})])
        result = {**result, f'{keyword}_mean_{quantitative_column}': means}
    return pd.DataFrame(result)


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def exists_paradox(loans, keywords, quantitative_column, categorical_column):
    aggregated = aggregate_and_combine(loans, keywords, quantitative_column, categorical_column)
    comps = aggregated.iloc[:, 0] > aggregated.iloc[:, 1]
    first = all(comps.iloc[:-1]) and not comps.iloc[-1]
    second = not any(comps.iloc[:-1]) and comps.iloc[-1]
    return bool(first or second)
    
def paradox_example(loans):
    return {
        'loans': loans,
        'keywords': ['stylist', 'operator'],
        'quantitative_column': 'loan_amnt',
        'categorical_column': 'home_ownership'
    }
