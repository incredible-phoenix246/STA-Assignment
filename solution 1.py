# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 04:23:10 2023

@author: Ayomikun
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data from the CSV file
data = pd.read_csv('test.csv')

# 2. Data Cleaning
# Handling Missing Values
data.dropna(subset=['Event_Type', 'Property_Cost'], inplace=True)  # Remove rows with missing values

# Remove Outliers (adjust the threshold as needed)
outlier_threshold = 3  # Define your outlier threshold
data = data[(data['Property_Cost'] - data['Property_Cost'].mean()).abs() <= outlier_threshold * data['Property_Cost'].std()]

# 3. Basic Descriptive Statistics
dataset_summary = data.describe()

# 4. Construct Graphical Summary
# Histogram of Property_Cost
plt.figure(figsize=(10, 6))
sns.histplot(data['Property_Cost'], kde=True)
plt.xlabel('Property Cost')
plt.title('Property Cost Distribution')
plt.show()

# Count plot of Event_Type
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Event_Type')
plt.xticks(rotation=45)
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.title('Event Type Distribution')
plt.show()

# 5. Prepare a Brief Summary Report
with open('summary_report.txt', 'w') as report:
    report.write("Event_Type Summary:\n")
    report.write(str(data['Event_Type'].describe()) + "\n\n")
    
    report.write("Property_Cost Summary:\n")
    report.write(str(data['Property_Cost'].describe()) + "\n\n")
    
    report.write("Dataset Summary:\n")
    report.write(str(dataset_summary))

print("Summary report saved as 'summary_report.txt'.")
