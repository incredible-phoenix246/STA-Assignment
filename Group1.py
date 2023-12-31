# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:23:54 2023

@author: AYOMIKUN
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ask the user for the CSV file name
csv_file_name = input("Enter the CSV file name: ")

# 2. Ask the user for the column names
event_column = input("Enter the name of the event column: ")
property_column = input("Enter the name of the property column: ")

# 3. Load the CSV data
data = pd.read_csv(csv_file_name)

# 4. Data Cleaning
# Drop rows with missing values
data.dropna(subset=[event_column, property_column], inplace=True)

# Function to convert "k" to 1000 and convert "m" to 1000000
def transform_property_cost(value):
    value = str(value)  # Ensure it's a string
    if 'k' in value:
        return float(value.replace('k', '')) * 1000
    elif 'm' in value:
        return float(value.replace('m', '')) * 1000000
    else:
        return float(value)

# Apply the transformation to the 'Property_Cost' column
data[property_column] = data[property_column].apply(transform_property_cost)

# 5. Basic Descriptive Statistics
property_cost_stats = data[property_column].describe()
mean = data[property_column].mean()
median = data[property_column].median()
mode = data[property_column].mode().iloc[0]
std_deviation = data[property_column].std()

# 6. Construct Graphical Summary
# Create a line plot for the specified columns
plt.figure(figsize=(25, 15))
sns.lineplot(data=data, x=event_column, y=property_column, ci=None)
plt.xticks(rotation=90)
plt.xlabel(event_column)
plt.ylabel(property_column)
plt.title(f'{event_column} vs. {property_column} (Line Plot)')
plt.show()


# Create a pie chart for the distribution of the specified columns
event_vs_property = data.groupby(event_column)[property_column].sum()
plt.figure(figsize=(40, 40))
plt.pie(event_vs_property, labels=event_vs_property.index, autopct='%1.1f%%')
plt.title(f'{event_column} vs. {property_column} (Pie Chart)')
plt.show()
"""

event_vs_property = data.groupby(event_column)[property_column].sum()

# Create a pie chart with a table
fig, ax = plt.subplots(figsize=(20, 20))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    event_vs_property,
    labels=event_vs_property.index,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.4),
)

# Create a table with color codes and values
colors = [w.get_facecolor() for w in wedges]
cell_text = [f'{label}: {value:.1f}%' for label, value in zip(event_vs_property.index, event_vs_property)]
table = ax.table(cellText=[cell_text], cellLoc='center', loc='center')

# Customize the appearance of the table
table.scale(1, 1.5)
table.auto_set_font_size(False)
table.set_fontsize(14)
table.auto_set_column_width([0])

# Apply cell colors
for i, color in enumerate(colors):
    for j in range(len(cell_text)):
        table.get_celld()[(j + 1, i)].set_facecolor(color)

plt.title(f'{event_column} vs. {property_column} (Pie Chart with Table)')
plt.show()
"""

# Detailed plot
plt.figure(figsize=(25, 15))
sns.countplot(data=data, x=event_column)
plt.xticks(rotation=90)
plt.xlabel(event_column)
plt.ylabel('Count')
plt.title(f'{event_column} Distribution Detailed')
plt.show()

# 7. Prepare a Brief Summary Report
event_summary = data[event_column].value_counts()
property_summary = property_cost_stats

# 8. Save the Summary Report to a Text File
with open('summary_report.txt', 'w') as report_file:
    report_file.write("Summary Report:\n")
    report_file.write(f"--- {event_column} Summary ---\n")
    report_file.write(str(event_summary) + "\n\n")
    report_file.write(f"--- {property_column} Summary ---\n")
    report_file.write(str(property_summary) + "\n\n")
    report_file.write("--- Mean ---\n")
    report_file.write(f"Mean: {mean}\n")
    report_file.write("--- Median ---\n")
    report_file.write(f"Median: {median}\n")
    report_file.write("--- Mode ---\n")
    report_file.write(f"Mode: {mode}\n")
    report_file.write("--- Standard Deviation ---\n")
    report_file.write(f"Standard Deviation: {std_deviation}\n")

# 9. Save the cleaned data to a new CSV with only specified columns
data[[event_column, property_column]].to_csv('new.csv', index=False)
# 8. Save the cleaned data to a new CSV file with empty rows removed
data.to_csv('cleaned_data.csv', index=False)


print("Summary report saved as 'summary_report.txt', your cleaned CSV file is saved as 'cleaned_data.csv', and the cleaned data with only the specified columns is exported to 'new.csv'.")
