# project.py


import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px

normalize = lambda grades, name: grades[name].fillna(0).copy() / grades[f"{name} - Max Points"].copy()

# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_assignment_names(grades):
    cols = grades.columns.to_numpy()
    
    return {
        "lab": [col for col in cols if col.startswith("lab") and " " not in col],
        "project": [col for col in cols if col.startswith("project") and " " not in col and "_" not in col],
        "midterm": [col for col in cols if col == "Midterm"],
        "final": [col for col in cols if col == "Final"],
        "disc": [col for col in cols if col.startswith("discussion") and " " not in col],
        "checkpoint": [col for col in cols if "checkpoint" in col and " " not in col],
    }


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def projects_total(grades):
    projects = get_assignment_names(grades)["project"]
    total_scores = pd.Series(0, index=grades.index)

    for project in projects:
        project_scores = grades[project].fillna(0).copy()
        max_points = grades[f"{project} - Max Points"].copy()
        
        if f'{project}_free_response' in grades.columns:
            project_scores += grades[f'{project}_free_response'].fillna(0).copy()
            max_points += grades[f"{project}_free_response - Max Points"].copy()
        
        total_scores += project_scores / max_points
    return total_scores / len(projects)


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def lateness_penalty(col):
    def calc(time):
        hrs, mins, secs = map(int, time.split(":"))
        deadline = lambda x: hrs < x or (hrs == x and (mins == secs == 0))
        
        if deadline(2): return 1
        elif deadline(24 * 7): return 0.9
        elif deadline(24 * 7 * 2): return 0.7
        else: return 0.4
        
    return col.copy().apply(calc)


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def process_labs(grades):
    labs = get_assignment_names(grades)["lab"]
    lab_grades = {}
    
    for lab in labs:
        late_penalty = lateness_penalty(grades[f'{lab} - Lateness (H:M:S)'].copy())
        lab_grades[lab] = normalize(grades, lab) * late_penalty
        
    return pd.DataFrame(lab_grades, index=grades.index)


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def lab_total(processed):
    return processed.apply(lambda student: student.nlargest(len(student) - 1).mean(), axis=1)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def total_points(grades):
    def get_grade(category):
        cols = get_assignment_names(grades)[category]
        normalized_grades = [normalize(grades, col) for col in cols]
        return pd.Series(sum(normalized_grades) / len(cols))
    
    labs = lab_total(process_labs(grades)) * 0.20
    projects = projects_total(grades) * 0.30
    checkpoints = get_grade("checkpoint") * 0.025
    discussions = get_grade("disc") * 0.025
    midterm = get_grade("midterm") * 0.15
    final = get_grade("final") * 0.30
    
    return labs + projects + checkpoints + discussions + midterm + final


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def final_grades(total):
    return total.apply(lambda grade: ['A', 'B', 'C', 'D', 'F'][int(min(9 - (grade * 10 // 1), 4))])

def letter_proportions(total):
    return final_grades(total).value_counts(normalize=True)


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def raw_redemption(final_breakdown, question_numbers):
    columns = final_breakdown.iloc[:, question_numbers]

    points_recieved = columns.fillna(0).to_numpy().sum(axis=1)
    points_available = sum([float(col.split()[-2][1:]) for col in columns])

    rr_scores = {"Raw Redemption Score": points_recieved / points_available}
    return final_breakdown.assign(**rr_scores)[["PID", "Raw Redemption Score"]]
    
def combine_grades(grades, raw_redemption_scores):
    return grades.merge(raw_redemption_scores, on="PID")


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def z_score(ser):
    return (ser - ser.mean()) / ser.std(ddof=0) if ser.std(ddof=0) else pd.Series([0] * len(ser))
    
def add_post_redemption(grades_combined):
    normal_midterms = normalize(grades_combined, 'Midterm')
    pre_red_df = grades_combined.assign(**{'Midterm Score Pre-Redemption': normal_midterms})
    inv_z_score = lambda z: z * normal_midterms.std(ddof=0) + normal_midterms.mean()
    
    return pre_red_df.assign(**{'Midterm Score Post-Redemption': 
        (pre_red_df[['Midterm Score Pre-Redemption', 'Raw Redemption Score']]
         .apply(z_score)
         .fillna(0)
         .max(axis=1)
         .apply(inv_z_score))
         .clip(upper=1)})


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def total_points_post_redemption(grades_combined):
    post_redemption = add_post_redemption(grades_combined)
    post = post_redemption['Midterm Score Post-Redemption']
    pre = post_redemption['Midterm Score Pre-Redemption']
    score_change = (post - pre) * 0.15
    return (total_points(grades_combined) + score_change).clip(upper=1)
        
def proportion_improved(grades_combined):
    post = total_points_post_redemption(grades_combined)
    pre = total_points(grades_combined)
    return (post // 0.1 - pre // 0.1).mean()


# ---------------------------------------------------------------------
# QUESTION 11
# ---------------------------------------------------------------------


def section_most_improved(grades_analysis):
    pre = grades_analysis["Letter Grade Pre-Redemption"]
    post = grades_analysis["Letter Grade Post-Redemption"]
    modified_analysis = grades_analysis.assign(improved_grade=(pre != post))
    
    return (modified_analysis
            .groupby("Section")
            .agg(prop_improved=("improved_grade", "mean"))
            .sort_values(by="prop_improved", ascending=False)
            .index[0])
    
def top_sections(grades_analysis, t, n):
    return np.array(sorted(grades_analysis
                           .query(f'`Final` / `Final - Max Points` > {t}')
                           .groupby("Section")
                           .filter(lambda df: df.shape[0] >= n)["Section"]
                           .unique()))

# ---------------------------------------------------------------------
# QUESTION 12
# ---------------------------------------------------------------------


def rank_by_section(grades_analysis):
    rank = (grades_analysis
            .sort_values(by=["Section", "Total Points Post-Redemption"], ascending=[True, False])
            .groupby("Section").cumcount() + 1)
    return (grades_analysis
            .assign(**{"Section Rank": rank})
            .pivot(index='Section Rank', columns='Section', values='PID')
            .fillna(''))


# ---------------------------------------------------------------------
# QUESTION 13
# ---------------------------------------------------------------------


def letter_grade_heat_map(grades_analysis):
    data = (grades_analysis
            .pivot(columns="Section", values="Letter Grade Post-Redemption")
            .apply(lambda ser: ser.value_counts(normalize=True))
            .fillna(0))
    
    fig = px.imshow(data,
                    labels=dict(x="Section", y="Letter Grade Post-Redemption", color="Proportion"),
                    title='Distribution of Letter Grades by Section',
                    color_continuous_scale=px.colors.sequential.deep,
                    x=data.columns,
                    y=data.index)
    return fig