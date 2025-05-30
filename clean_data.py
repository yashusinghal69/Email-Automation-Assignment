import pandas as pd
import numpy as np
import os

data = pd.read_csv('Data - Sheet1.csv')

# Remove duplicate rows having exact same rows
data = data.drop_duplicates()

# Normalize 'has_joined_event' values
data['has_joined_event'] = data['has_joined_event'].str.strip().str.lower().map({'yes': True, 'no': False})

# Flag missing or blank job titles
# df['missing_job_title'] = df['Job Title'].apply(lambda x: pd.isna(x) or str(x).strip() == '')


# Flag incomplete or missing LinkedIn profiles
def is_linkedin_incomplete(value):
    if pd.isna(value):
        return True
    value = str(value).strip().lower()
    return not (value.startswith("http://") or value.startswith("https://"))

data['missing_linkedin'] = data['What is your LinkedIn profile?'].apply(is_linkedin_incomplete)


# Clean LinkedIn column values
def clean_linkedin(value):
    if pd.isna(value):
        return ""  # Replace NaN with empty string
    value = str(value).strip()
    if value.lower().startswith("http://") or value.lower().startswith("https://"):
        return value
    return ""  # Replace bad URLs with empty string

data['What is your LinkedIn profile?'] = data['What is your LinkedIn profile?'].apply(clean_linkedin)


# Convert created_at to datetime object
data['created_at'] = pd.to_datetime(data['created_at'], errors='coerce')
# # Format it as 'YYYY-MM-DD HH:MM AM/PM'
data['created_at'] = data['created_at'].dt.strftime('%B %d, %Y — %I:%M %p')


 # Fix inconsistent casing in Job Title: 'student' → 'Student'
data['Job Title'] = data['Job Title'].apply(lambda x: str(x).strip().capitalize() if pd.notna(x) else x)

# Fill missing job titles with most frequent value
most_common_job = data['Job Title'].mode()[0]
data['Job Title'] = data['Job Title'].fillna(most_common_job)

# Fill missing ticket_name with most frequent value
most_common_ticket = data['ticket_name'].mode()[0]
data['ticket_name'] = data['ticket_name'].fillna(most_common_ticket)


# Standardize casing and trim
data['name']        = data['name'].str.strip().str.title()
data['first_name']  = data['first_name'].str.strip().str.title()
data['last_name']   = data['last_name'].str.strip().str.title()

#Parse full name into parts
def parse_name(full):
    parts = str(full).split()
    if len(parts) >= 2:
        return parts[0], parts[-1]
    elif len(parts) == 1:
        return parts[0], ''
    else:
        return '', ''

data[['parsed_first', 'parsed_last']] = data['name'].apply(lambda x: pd.Series(parse_name(x)))

#Back-fill missing first/last names
data['first_name'] = data['first_name'].fillna(data['parsed_first'])
data['last_name']  = data['last_name'].fillna(data['parsed_last'])

data = data.drop(columns=['parsed_first', 'parsed_last'])

# Save cleaned output
data.to_csv("cleaned_output1.csv", index=False)

