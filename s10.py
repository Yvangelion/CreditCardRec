import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.optimize import differential_evolution

# Define functions from the first program
def portfolio_returns(x, asset_returns):
    return np.sum(asset_returns * x, axis=1)

def sharpe(x, asset_returns):
    port_returns = portfolio_returns(x, asset_returns)
    return np.mean(port_returns) / np.sqrt(np.var(port_returns))

def obj(x, asset_returns):
    return -sharpe(x, asset_returns) + 100 * (np.sum(x) - 1) ** 2

# Define functions from the second program
def get_financial_data():
    """Retrieve historical financial data."""
    # Generate sample financial data
    dates = pd.date_range(start='1950-01-01', periods=100, freq='Y')
    assets = ['US Total Market', 'International Funds Total Market', 'Bonds', 'Cash']
    np.random.seed(0)  # For reproducibility
    data = np.random.rand(len(dates), len(assets))
    financial_data = pd.DataFrame(data, index=dates, columns=assets)
    return financial_data

def risk_assessment(financial_data):
    """Perform risk assessment based on historical financial data."""
    # Example: Calculate volatility, covariance matrix, or any risk metrics
    # For demonstration purposes, let's calculate annualized volatility
    annualized_volatility = financial_data.std() * np.sqrt(252)
    return annualized_volatility

def predict_returns(financial_data):
    """Perform predictive modeling to predict future returns."""
    # Example: Train a predictive model using historical financial data
    # For demonstration purposes, let's use simple mean returns
    mean_returns = financial_data.mean()
    return mean_returns

def genetic_algorithm(target_allocation, risk_tolerance, investment_length, financial_data):
    """Run genetic algorithm to find optimal asset allocation."""
    population_size = population_sizes[risk_tolerance]
    population = initialize_population(population_size)

    for generation in range(NUM_GENERATIONS):
        fitness = fitness_function(population, target_allocation, risk_tolerance)

        parents_indices = np.argsort(fitness)[:2]
        parent1 = population[parents_indices[0]]
        parent2 = population[parents_indices[1]]

        offspring = crossover(parent1, parent2, risk_tolerance)
        offspring = mutate(offspring, risk_tolerance)

        worst_index = np.argmax(fitness)
        population[worst_index] = offspring

    best_index = np.argmin(fitness)
    best_allocation = population[best_index]
    best_fitness = fitness.min()

    return best_allocation, best_fitness

# Main program
if __name__ == "__main__":
    # Read data
    files = ["merged.csv"]
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

    # Optimization via Genetic Algorithm
    bounds = [(0, 1)] * len(asset_returns.columns)
    result = differential_evolution(obj, bounds, args=(asset_returns,), maxiter=50000)

    # Store the resulting weights in a vector
    sol = result.x
    weights = pd.DataFrame(list(zip(asset_returns.columns, sol)), columns=['Asset', 'Weight'])
    print(weights)

    # Retrieve financial data
    financial_data = get_financial_data()
    
    # Perform risk assessment
    annualized_volatility = risk_assessment(financial_data)
    
    # Predict future returns
    mean_returns = predict_returns(financial_data)

    # Run genetic algorithm for each age group
    ages = [50]
    retirement_age = 80
    for age in ages:
        print(f"\n--- Age: {age} ---")
        risk_tolerance, target_allocation, investment_length = get_risk_tolerance(age, retirement_age)
        print("Based on your age, your risk tolerance is:", risk_tolerance)
        print("Your investment length is:", investment_length)
        
        # Run genetic algorithm
        best_allocation, best_fitness = genetic_algorithm(target_allocation, risk_tolerance, investment_length, financial_data)
        
        # Calculate portfolio returns
        portfolio_returns = calculate_portfolio_returns(best_allocation, mean_returns)
        
        display_results(financial_data, annualized_volatility, best_allocation, best_fitness, portfolio_returns)
