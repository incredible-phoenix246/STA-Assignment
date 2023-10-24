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
# Drop rows with missing values
data.dropna(subset=['Event_Type', 'Property_Cost'], inplace=True)

# Function to convert "k" to "1000" and "m" to "1000000"
def transform_property_cost(value):
    value = str(value)  # Ensure it's a string
    if 'k' in value:
        return float(value.replace('k', '')) * 1000
    elif 'm' in value:
        return float(value.replace('m', '')) * 1000000
    else:
        return float(value)

# Apply the transformation to the 'Property_Cost' column
data['Property_Cost'] = data['Property_Cost'].apply(transform_property_cost)

# 3. Basic Descriptive Statistics
property_cost_stats = data['Property_Cost'].describe()
mean = data['Property_Cost'].mean()
median = data['Property_Cost'].median()
mode = data['Property_Cost'].mode().iloc[0]
std_deviation = data['Property_Cost'].std()

# 4. Construct Graphical Summary
# Create a line plot for Event_Type vs. Property_Cost
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Event_Type', y='Property_Cost', ci=None)
plt.xticks(rotation=45)
plt.xlabel('Event Type')
plt.ylabel('Property Cost')
plt.title('Event Type vs. Property Cost (Line Plot)')
plt.show()

# Create a pie chart for the distribution of Event_Type vs. Property_Cost
event_type_vs_property = data.groupby('Event_Type')['Property_Cost'].sum()
plt.figure(figsize=(8, 8))
plt.pie(event_type_vs_property, labels=event_type_vs_property.index, autopct='%1.1f%%')
plt.title('Event Type vs. Property Cost (Pie Chart)')
plt.show()

# Detailed plot
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Event_Type')
plt.xticks(rotation=45)
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.title('Event Type Distribution Detailed')
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
    report_file.write(str(property_cost_summary) + "\n\n")
    report_file.write("--- Mean ---\n")
    report_file.write(f"Mean: {mean}\n")
    report_file.write("--- Median ---\n")
    report_file.write(f"Median: {median}\n")
    report_file.write("--- Mode ---\n")
    report_file.write(f"Mode: {mode}\n")
    report_file.write("--- Standard Deviation ---\n")
    report_file.write(f"Standard Deviation: {std_deviation}\n")

# 7. Save the cleaned data to a new CSV with only 'Event_Type' and 'Property_Cost' columns
data[['Event_Type', 'Property_Cost']].to_csv('new.csv', index=False)

print("Summary report saved as 'summary_report.txt', your cleaned CSV file is saved as 'cleaned_data.csv', and the cleaned data with only 'Event_Type' and 'Property_Cost' columns is exported to 'new.csv'.")
