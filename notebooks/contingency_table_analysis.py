import pandas as pd
from tabulate import tabulate
df = pd.read_excel("E:\\Software\\Python\\Python_313\\Consumer-Behavior-Analysis\\data\\survey_data.xlsx")
print(df)
# Assuming 'df' is already defined
crosstab_df = pd.crosstab(df["Uniqueness"], df["Purchase Likelihood"], margins=True, margins_name='Total')
print(tabulate(crosstab_df, headers='keys', tablefmt='pretty'))

