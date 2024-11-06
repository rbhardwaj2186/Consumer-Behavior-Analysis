# src/chi_square_analysis.py

from scipy.stats import chi2_contingency
import pandas as pd

def chi_square_test(data):
    # Assumes the data is a contingency table without row totals
    chi2, p, dof, expected = chi2_contingency(data.iloc[:, 1:])
    return {
        "chi2": chi2,
        "p-value": p,
        "degrees_of_freedom": dof,
        "expected": pd.DataFrame(expected, columns=data.columns[1:], index=data.iloc[:, 0])
    }
