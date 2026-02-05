# lab.py


from pathlib import Path
import io
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
    n = len(nums)
    mean = sum(nums) / n
    sort_nums = sorted(nums)
    
    if n % 2 == 0:
        median = (sort_nums[n // 2 - 1] + sort_nums[n // 2]) / 2
    else:
        median = sort_nums[n // 2]
        
    return median <= mean


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    return "".join([s[:i+1] for i in range(n)][::-1])


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    width = len(str(max(ints) + n))
    return [" ".join([str(i).zfill(width) for i in range(num - n, num + n + 1) ]) for num in ints]


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def last_chars(fh):
    return "".join([line.rstrip()[-1] for line in fh if line.strip()])


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def add_root(A):
    return A + np.sqrt(np.arange(len(A)))

def where_square(A):
    return np.isclose(np.sqrt(A) % 1, 0)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_loop(matrix, cutoff):
    means = [sum(matrix[:, i]) / matrix.shape[0] for i in range(matrix.shape[1])]
    cols = [i for i, v in enumerate(means) if v > cutoff]
    return matrix[:, cols]

# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    return matrix[:, np.mean(matrix, 0) > cutoff]


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    return np.round(np.diff(A) / A[:-1], 2)

def with_leftover(A):
    can_buy_days = np.where(np.cumsum(20 % A) >= A)[0]
    return can_buy_days[0] if len(can_buy_days) > 0 else -1


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    teams = salary.groupby("Team")
    salary_sorted = salary.sort_values(by="Salary", ascending=False)
    fifth_lowest = salary_sorted.iloc[-5]
    highest_salary = salary_sorted.iloc[0]
    get_last_name = lambda name: name.split(" ")[1]
    
    return pd.Series({
        "num_players": salary.shape[0],
        "num_teams": salary["Team"].nunique(),
        "total_salary": salary["Salary"].sum(),
        "highest_salary": salary_sorted.iloc[0]["Player"],
        "avg_los": np.round(salary[salary["Team"] == "Los Angeles Lakers"]["Salary"].mean(), 2),
        "fifth_lowest": f'{fifth_lowest["Player"]}, {fifth_lowest["Team"]}',
        "duplicates": len(np.unique(salary["Player"].apply(get_last_name))) != salary.shape[0],
        "total_highest": teams.sum().loc[highest_salary["Team"]]["Salary"]
    })


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    rows = []
    with open(fp, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            line = line.replace('",', '|').replace(',','|')
            row = line.strip().split('|')
            
            # Fix cases where double quotes might still be misplaced
            row = [x.replace('"', '') for x in row if x]
            
            # Reformat data
            first, last = row[0], row[1]
            weight = float(row[2]) if row[2] else None
            height = float(row[3]) if row[3] else None
            geo = f'{row[4]},{row[5]}'
            
            row = [first, last, weight, height, geo]
            rows.append(row)
            
    return pd.DataFrame(rows, columns=header)