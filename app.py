# app.py

import streamlit as st
import pandas as pd
from src.data_preprocessing import load_data, clean_data
from src.chi_square_analysis import chi_square_test

st.title("Consumer Behavior Analysis with Chi-square Tests")
st.sidebar.header("Select Dataset")

# Choose the dataset to analyze
option = st.sidebar.selectbox("Choose a dataset:",
                              ("Product Uniqueness vs Purchase Likelihood",
                               "Newsletter Engagement vs Download Behavior"))

# Load and display data
if option == "Product Uniqueness vs Purchase Likelihood":
    data = load_data('Case 2 cross')
    st.subheader("Product Uniqueness vs Purchase Likelihood")
elif option == "Newsletter Engagement vs Download Behavior":
    data = load_data('Case 1v')
    st.subheader("Newsletter Engagement vs Download Behavior")

# Show the raw data
st.write("Data Preview:")
st.write(data)

# Clean data
data = clean_data(data)

# Run the Chi-square test
if st.button("Run Chi-square Test"):
    results = chi_square_test(data)
    st.write(f"Chi-square Statistic: {results['chi2']}")
    st.write(f"p-value: {results['p-value']}")
    st.write(f"Degrees of Freedom: {results['degrees_of_freedom']}")
    st.write("Expected Frequencies:")
    st.write(results['expected'])

    if results['p-value'] < 0.05:
        st.success("Significant association found (p < 0.05)")
    else:
        st.warning("No significant association found (p >= 0.05)")
