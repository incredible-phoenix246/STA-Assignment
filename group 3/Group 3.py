import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data from dataset.csv
data = pd.read_csv('dataset.csv')

# 2. Clean the data by removing empty rows
data.dropna(subset=['Event_Type', 'State'], inplace=True)

# 3. Save the cleaned data to group3.csv
data.to_csv('group3.csv', index=False)

# 4. Summarize the data for Event_Type per State
event_type_summary = data.groupby(['Event_Type', 'State']).size().reset_index(name='Count')

# 5. Write the summary to group3.txt
with open('summary.txt', 'w') as summary_file:
    summary_file.write("--- Summary Report ---\n\n")
    summary_file.write("Data Summary for Event_Type per State:\n")
    summary_file.write(event_type_summary.to_string(index=False))
    summary_file.write("\n")

# 6. Plot a graph of Event_Type against State
plt.figure(figsize=(12, 6))
plt.xticks(rotation=90)
plt.title("Event_Type vs. State")
plt.xlabel("State")
plt.ylabel("Count")
plt.bar(event_type_summary['State'], event_type_summary['Count'])
plt.tight_layout()

# Save the plot as a file if needed
plt.savefig('event_type_vs_state.png')

# Display the plot
plt.show()
