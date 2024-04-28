import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load portfolio returns data from CSV file
portfolio_returns = pd.read_csv("port.csv")

# Ask for user input
age = int(input("Enter your age: "))
retirement_age = int(input("Enter your retirement age: "))
risk_tolerance = float(input("Enter your risk tolerance (0-1): "))

# Prepare data for prediction
X = portfolio_returns.drop("Year", axis=1)
y = portfolio_returns["Year"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future returns
future_returns = model.predict(X_test)

# Create asset allocation based on predicted returns and risk tolerance
allocation = {}
for col, pred_return in zip(X.columns, future_returns):
    allocation[col] = pred_return * risk_tolerance

# Print asset allocation
print("Asset Allocation:")
for asset, weight in allocation.items():
    print(f"{asset}: {weight:.2f}%")
