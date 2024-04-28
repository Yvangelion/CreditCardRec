import numpy as np
import pandas as pd

# Define parameters
NUM_ASSETS = 4
NUM_GENERATIONS = 100_000

# Define risk tolerance levels and their corresponding penalties, mutation rates, and population sizes
risk_penalties = {"high": 1.0, "medium": 0.5, "low": 0.1}
mutation_rates = {"high": 0.2, "medium": 0.1, "low": 0.05}
population_sizes = {"high": 1000, "medium": 1000, "low": 1000}

# Define functions
def initialize_population(population_size):
    """Initialize a population of given size."""
    return np.random.rand(population_size, NUM_ASSETS)

def fitness_function(population, target_allocation, risk_tolerance):
    """Calculate the fitness of each individual in the population."""
    deviation = np.abs(population - target_allocation).sum(axis=1)
    penalty = risk_penalties[risk_tolerance]
    fitness = deviation * penalty
    return fitness

def crossover(parent1, parent2, risk_tolerance):
    """Perform crossover to generate offspring."""
    crossover_point = np.random.randint(1, NUM_ASSETS)
    offspring = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    return offspring

def mutate(individual, risk_tolerance):
    """Perform mutation on an individual."""
    for i in range(len(individual)):
        if np.random.rand() < mutation_rates[risk_tolerance]:
            individual[i] = np.random.rand()
    return individual

def get_risk_tolerance(age,retirement_age):
    """Determine risk tolerance based on age and investment length."""
    investment_length = retirement_age - age
    if age < 30:
        target_allocation = np.array([0.70, 0.20, 0.5, 0.5])
        return "high", target_allocation, investment_length
    elif 30 <= age <= 50:
        target_allocation = np.array([0.25, 0.25, 0.25, 0.25])
        return "medium", target_allocation, investment_length
    else:
        target_allocation = np.array([0.15, 0.15, 0.60, 0.10])
        return "low", target_allocation, investment_length

def calculate_portfolio_returns(allocation, returns):
    """Calculate portfolio returns based on asset allocation and returns."""
    portfolio_returns = np.dot(returns, allocation)
    return portfolio_returns


def get_financial_data():
    """Retrieve historical financial data."""
    # Generate sample financial data
    dates = pd.date_range(start='1950-01-01', periods=100, freq='Y')
    assets = ['US Total Market', 'International Funds Total Market', 'Bonds', 'Cash']
    np.random.seed(0)  # For reproducibility
    data = np.random.rand(len(dates), len(assets))
    financial_data = pd.DataFrame(data, index=dates, columns=assets)
    
    filename = "java.csv"
    financial_data = pd.DataFrame(data, index=dates, columns=assets)
    
    # Save the financial data to a CSV file
    financial_data.to_csv(filename)
    
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

def display_results(financial_data, annualized_volatility, best_allocation, best_fitness,portfolio_returns):
    """Display financial data, risk assessment, optimal asset allocation, and fitness."""
    print("\n--- Financial Data ---")
    print(financial_data.head())
    print("\n--- Risk Assessment (Annualized Volatility) ---")
    print(annualized_volatility)
    print("\nOptimal asset allocation:")
    print("US Total Market:", best_allocation[0])
    print("International Funds Total Market:", best_allocation[1])
    print("Bonds:", best_allocation[2])
    print("Cash:", best_allocation[3])
    print("Final fitness:", best_fitness)
    print("Portfolio Returns:", portfolio_returns)
    


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

if __name__ == "__main__":

    
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
        risk_tolerance, target_allocation, investment_length = get_risk_tolerance(age,retirement_age)
        print("Based on your age, your risk tolerance is:", risk_tolerance)
        print("Your investment length is:", investment_length)
        
        
        # Run genetic algorithm
        best_allocation, best_fitness = genetic_algorithm(target_allocation, risk_tolerance, investment_length, financial_data)
        
        # Calculate portfolio returns
        portfolio_returns = calculate_portfolio_returns(best_allocation, mean_returns)
        
        
        display_results(financial_data, annualized_volatility, best_allocation, best_fitness,portfolio_returns)



    