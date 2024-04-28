import pandas as pd
import numpy as np
from scipy.optimize import differential_evolution

# Read data
files = ["new.csv"]
dfs = [pd.read_csv(file) for file in files]
f = pd.concat(dfs)

# Calculate returns
returns = pd.DataFrame()
for col in f.columns[1:]:
    prices = f[col]
    prices_prev = np.concatenate([[np.nan], prices.values[:-1]])
    returns[col] = (prices - prices_prev) / prices_prev

# Remove first row with NAs and Date column
asset_returns = returns.iloc[1:]

# Function to determine risk tolerance based on age
def get_risk_tolerance(age, retirement_age):
    years_to_retirement = retirement_age - age
    if years_to_retirement > 40:
        return 'high'
    elif years_to_retirement > 20:
        return 'medium'
    else:
        return 'low'

# User input for age and retirement age
age = int(input("Enter your age: "))
retirement_age = int(input("Enter your planned retirement age: "))

# Determine risk tolerance based on age and retirement age
risk_tolerance = get_risk_tolerance(age, retirement_age)

# Objective function to be optimized
def obj(x):
    port_returns = np.sum(asset_returns * x, axis=1)
    mean_return = np.mean(port_returns)
    std_dev = np.std(port_returns)
    # Adjust the objective function based on risk tolerance
    if risk_tolerance == 'high':
        return -mean_return / std_dev  # Maximize Sharpe ratio
    elif risk_tolerance == 'medium':
        return -mean_return  # Maximize return with moderate risk
    else:
        return -std_dev  # Minimize risk with lower return

# Optimization
bounds = [(0, 1)] * len(asset_returns.columns)
result = differential_evolution(obj, bounds, maxiter=50000)

# Store the resulting weights in a vector
sol = result.x
weights = pd.DataFrame(list(zip(asset_returns.columns, sol)), columns=['Asset', 'Weight'])
print(weights)
