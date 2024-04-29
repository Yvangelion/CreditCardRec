import pandas as pd
import numpy as np
from scipy.optimize import differential_evolution

# read data
files = ["new.csv"]
dfs = [pd.read_csv(file) for file in files]
f = pd.concat(dfs)

# calc returns
returns = pd.DataFrame()
for col in f.columns[1:]:
    prices = f[col]
    prices_prev = np.concatenate([[np.nan], prices.values[:-1]])
    returns[col] = (prices - prices_prev) / prices_prev

# remove the N/As and date column
asset_returns = returns.iloc[1:]

# determine risk tolerance based on age and years to retirement
def get_risk_tolerance(age, retirement_age):
    years_to_retirement = retirement_age - age
    if years_to_retirement > 40:
        return 'high'
    elif years_to_retirement > 20:
        return 'medium'
    else:
        return 'low'

# request age
age = int(input("Enter your age: "))
# request planned retirement age
retirement_age = int(input("Enter your planned retirement age: "))

# calc risk tolerance based on age and retirement age
risk_tolerance = get_risk_tolerance(age, retirement_age)

# obj function to be optimized
def obj(x):
    port_returns = np.sum(asset_returns * x, axis=1)
    mean_return = np.mean(port_returns)
    std_dev = np.std(port_returns)
    # adjust the objective function based on risk tolerance
    if risk_tolerance == 'high':
        return -mean_return / std_dev  # Maximize Sharpe ratio if high
    elif risk_tolerance == 'medium':
        return -mean_return  # Maximize return with moderate risk if medium
    else:
        return -std_dev  # Minimize risk with lower return if low 

# optimize
bounds = [(0, 1)] * len(asset_returns.columns)
result = differential_evolution(obj, bounds, maxiter=50000)

# store the resulting weights 
sol = result.x
weights = pd.DataFrame(list(zip(asset_returns.columns, sol)), columns=['Asset', 'Weight'])
#print(weights)

# Print optimized portfolio weights and assets
print("Optimized Portfolio Weights:")
print(weights)

# performance metrics
port_returns = np.sum(asset_returns * sol, axis=1)
mean_return = np.mean(port_returns)
std_dev = np.std(port_returns)
sharpe_ratio = mean_return / std_dev

# Display outputs
print("\nPerformance Metrics:")
print(f"Determined Risk Tolerance: {risk_tolerance}")
print(f"Expected Return: {mean_return:.4f}")
print(f"Standard Deviation (Risk): {std_dev:.4f}")
print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
