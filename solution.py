# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 04:23:10 2023

@author: Ayomikun
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the CSV data
data = pd.read_csv('test.csv')

# 2. Extensive Data Cleaning
# Handling missing values, duplicates, and outliers
data.dropna(subset=['Event_Type', 'Property_Cost'], inplace=True)  # Drop rows with missing values
data.drop_duplicates(inplace=True)  # Remove duplicate rows
data = data[(data['Property_Cost'] > 0) & (data['Property_Cost'] < 1e7)]  # Filter out outliers

# 3. Basic Descriptive Statistics
property_cost_stats = data['Property_Cost'].describe()

# 4. Construct Graphical Summary
# Create a histogram for Property_Cost
plt.hist(data['Property_Cost'], bins=20)
plt.title('Property Cost Distribution')
plt.xlabel('Property Cost')
plt.ylabel('Frequency')
plt.show()

# Create a bar plot for Event_Type
plt.subplot(122)
event_type_counts = data['Event_Type'].value_counts()
event_type_counts.plot(kind='bar')
plt.title('Event Type Distribution')
plt.xlabel('Event Type')
plt.ylabel('Count')


# Detailed plot
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Event_Type')
plt.xticks(rotation=45)
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.title('Event Type Distribution Detailed')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Property_Cost'], kde=True)
plt.xlabel('Property Cost')
plt.title('Property Cost Distribution Detaiiled')
plt.show()


# 5. Prepare a Brief Summary Report
event_type_summary = data['Event_Type'].value_counts()
property_cost_summary = property_cost_stats

# 6. Save the Summary Report to a Text File
with open('summary_report.txt', 'w') as report_file:
    report_file.write("Summary Report:\n")
    report_file.write("--- Event_Type Summary ---\n")
    report_file.write(str(event_type_summary) + "\n\n")
    report_file.write("--- Property_Cost Summary ---\n")
    report_file.write(str(property_cost_summary) + "\n")

# 7. Save the cleaned data to a new CSV
data.to_csv('cleaned_data.csv', index=False)

print("Summary report saved as 'summary_report.txt' and your cleaned csv file is saved as 'cleaned_data.csv'.")
