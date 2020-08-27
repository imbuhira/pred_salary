import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cleaned_salary_data.csv')

# get relevant columns

df.columns

df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'hourly',
               'employer_provided', 'job_state', 'same_state', 'age', 'python', 'java', 'r', 'spark', 'aws', 'excel',
               'job_title_simple', 'seniority', 'desc_len']]

# get dummy data
df_dum = pd.get_dummies(df_model)