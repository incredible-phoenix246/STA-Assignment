# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:01:29 2023

@author: USER
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import io
from sklearn.metrics import accuracy_score, classification_report

# Load your dataset
df = pd.read_csv("dataset.csv")

# Select the specific columns of interest
df = df[['State', 'Month', 'Event_Type']]

df.dropna(inplace=True)

# Convert categorical variables to numerical features using one-hot encoding
df = pd.get_dummies(df, columns=['Month', 'State'], prefix=['Month', 'State'], drop_first=True)

# Split the data into features and target variable
X = df.drop(['Event_Type'], axis=1)
y = df['Event_Type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a classification model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100)

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(report)

# Convert the classification report to a DataFrame
report_df = pd.read_fwf(io.StringIO(report), header=0)

# Save the report to a CSV file
report_df.to_csv("classification_report.csv", index=False)

'''
# Create a new figure
fig, ax = plt.subplots()

# Plot the training and testing accuracy
ax.plot(X_train['Month'], y_train, label='Training Accuracy')
ax.plot(X_test['Month'], y_test, label='Testing Accuracy')

# Set the axis labels and title
ax.set_xlabel('Month')
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy vs. Month')

# Add a legend
ax.legend()

# Show the plot
plt.show()


# Plot the confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(confusion, cmap='Blues', interpolation='nearest')
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = range(len(model.classes_))
plt.xticks(tick_marks, model.classes_, rotation=45)
plt.yticks(tick_marks, model.classes_)
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()

# Plot feature importance
feature_importance = model.feature_importances_
feature_names = X.columns
sorted_idx = feature_importance.argsort()
plt.figure(figsize=(10, 6))
plt.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center')
plt.yticks(range(len(sorted_idx), 0), [feature_names[i] for i in sorted_idx])
plt.xlabel('Feature Importance')
plt.title('Feature Importance Plot')
plt.show()
'''