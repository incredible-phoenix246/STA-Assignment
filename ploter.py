# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:58:38 2023

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv("classification_report.csv")  # Replace with your CSV file path

# Assuming you have columns 'Event_type' and 'precision' in your data

# Create a bar plot
plt.figure(figsize=(20, 12))
plt.bar(df['Event_Type'], df['precision'])
plt.xlabel('Event Type')
plt.ylabel('Precision')
plt.title('Precision by Event Type')
plt.xticks(rotation=90)  # Rotate the x-axis labels for readability

# Create a line graph
plt.figure(figsize=(20, 20))
plt.subplot(2, 1, 2)  # Subplot for the line graph
plt.plot(df['Event_Type'], df['precision'], marker='o', linestyle='-')
plt.xlabel('Event Type')
plt.ylabel('Precision')
plt.title('Precision by Event Type (Line Graph)')
plt.xticks(rotation=90)  # Rotate the x-axis labels for readability

# Show the plot
plt.tight_layout()
plt.show()
