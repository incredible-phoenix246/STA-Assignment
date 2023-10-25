import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the CSV file
data = pd.read_csv("test.csv")

# Remove empty rows under Event_Type
data = data.dropna(subset=["Event_Type"])

# Task 1: Summarize the data for Event_Type per state
event_type_summary = data.groupby(["State", "Event_Type"]).size().reset_index(name="Count")

# Task 2: Basic descriptive statistics with graphs
# Descriptive statistics
descriptive_stats = data.describe()

# Create a bar plot for event counts by state and event type
plt.figure(figsize=(20, 10))
sns.barplot(data=event_type_summary, x="State", y="Count", hue="Event_Type")
plt.title("Event Counts by State and Event Type")
plt.xticks(rotation=90)

# Task 3: Test for differences in the variable of the Storm Event
# Example t-test between two Event Types (you can customize this)
event_type_1 = data[data["Event_Type"] == "Type1"]["SomeNumericColumn"]
event_type_2 = data[data["Event_Type"] == "Type2"]["SomeNumericColumn"]

if event_type_1.empty or event_type_2.empty:
    t_stat, p_value = None, None
else:
    t_stat, p_value = ttest_ind(event_type_1, event_type_2)

# Task 4: Prepare a brief summary report
summary_report = """
--- Summary Report ---
1. Data Summary for Event_Type per State:
{}

2. Basic Descriptive Statistics:
{}

3. T-test for Differences in the Variable of Storm Event:
   - T-statistic: {}
   - P-value: {}

4. Empty Rows Removed Under Event_Type.
""".format(event_type_summary, descriptive_stats, t_stat, p_value)

# Write the report to a text file
with open("summary_report.txt", "w") as report_file:
    report_file.write(summary_report)

# Close the graph display
plt.savefig("bar_plot.png")
plt.close()

print("Summary report has been written to summary_report.txt.")