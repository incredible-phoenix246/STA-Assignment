import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC

# Load your dataset (replace 'test.csv' with the actual file path or place it in the same folder as the scripts)
data = pd.read_csv('test.csv')

# Data preprocessing
# Encode categorical 'Event_Type' as numerical labels
label_encoder = LabelEncoder()
data['Event_Type'] = label_encoder.fit_transform(data['Event_Type'])

# Split the dataset into features (X) and target (y)
X = data.drop('Event_Type', axis=1)
y = data['Event_Type']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def train_logistic_regression(X_train, y_train, X_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def train_decision_tree(X_train, y_train, X_test):
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def train_random_forest(X_train, y_train, X_test):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def train_gradient_boosting(X_train, y_train, X_test):
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def train_support_vector_machine(X_train, y_train, X_test):
    model = SVC()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def evaluate_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

# Example usage:
logistic_regression_pred = train_logistic_regression(X_train, y_train, X_test)
logistic_regression_accuracy, logistic_regression_report = evaluate_model(y_test, logistic_regression_pred)
print(f"Logistic Regression Accuracy: {logistic_regression_accuracy:.2f}\nClassification Report:\n{logistic_regression_report}")

decision_tree_pred = train_decision_tree(X_train, y_train, X_test)
decision_tree_accuracy, decision_tree_report = evaluate_model(y_test, decision_tree_pred)
print(f"Decision Tree Accuracy: {decision_tree_accuracy:.2f}\nClassification Report:\n{decision_tree_report}")

