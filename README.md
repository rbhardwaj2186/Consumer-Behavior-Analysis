# Consumer Behavior Analysis with Chi-square Tests

## Overview

This project provides an interactive tool built with **Streamlit** for analyzing consumer behavior data through **Chi-square tests of independence**. It helps users determine if there are statistically significant associations between categorical variables related to consumer behavior.

<img src="https://github.com/user-attachments/assets/fedec27f-b672-4de6-a493-623359877f65" alt="Descriptive Alt Text" width="100%">

### Key Features
- **Dataset Selection**: Choose between two datasets to analyze:
  - **Newsletter Engagement vs. Download Behavior**: Examines whether reading a newsletter is associated with an increase in downloads.
  - **Product Uniqueness vs. Purchase Likelihood**: Assesses if perceived product uniqueness influences purchase likelihood.
- **Data Preview**: Displays a contingency table of the selected dataset to understand the distribution of values.
- **Chi-square Test Execution**: Runs the Chi-square test of independence on the selected dataset and displays the results, including:
  - Chi-square Statistic
  - p-value
  - Degrees of Freedom
  - Expected Frequencies
- **Interpretation of Results**: Provides a conclusion based on the p-value to help users understand if the association is statistically significant.

### Technologies Used
- **Python**
- **Streamlit** for the interactive GUI
- **Pandas** for data manipulation
- **SciPy** for Chi-square test calculations

## Installation

### Step 1: Clone the Repository
To get started, clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/Consumer-Behavior-Analysis.git
cd Consumer-Behavior-Analysis
