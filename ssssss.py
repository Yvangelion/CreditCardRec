import numpy as np
import random

# Define parameters
num_assets = 5
initial_population_size = 50
mutation_rate = 0.1
num_generations = 100
portfolio_value = 1000000  # $1,000,000
expected_rate_of_return = 0.08
num_periods = 10
regular_contribution = 50000  # $50,000

# Define asset returns (sample data)
asset_returns = [0.1, 0.05, 0.08, 0.12, 0.06]

# Define functions for Genetic Algorithm

def initialize_population(population_size, num_assets):
    population = []
    for _ in range(population_size):
        weights = np.random.rand(num_assets)
        weights /= np.sum(weights)  # Normalize weights
        population.append(weights)
    return population

def calculate_fitness(weights):
    portfolio_return = np.dot(weights, asset_returns)
    future_value = portfolio_value * (1 + portfolio_return)**num_periods + \
                   regular_contribution * ((1 + portfolio_return)**num_periods - 1) / portfolio_return
    return future_value

def crossover(parent1, parent2):
    crossover_point = random.randint(1, num_assets - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutate(weights):
    for i in range(num_assets):
        if random.random() < mutation_rate:
            weights[i] = random.random()
    weights /= np.sum(weights)  # Normalize weights after mutation
    return weights

# Main Genetic Algorithm
population = initialize_population(initial_population_size, num_assets)
for generation in range(num_generations):
    # Calculate fitness for each individual
    fitness_scores = [calculate_fitness(individual) for individual in population]
    
    # Select parents for crossover (tournament selection)
    parents = []
    for _ in range(initial_population_size):
        tournament_indices = random.sample(range(initial_population_size), 2)
        tournament_scores = [fitness_scores[i] for i in tournament_indices]
        winner_index = tournament_indices[np.argmax(tournament_scores)]
        parents.append(population[winner_index])
    
    # Perform crossover and mutation
    new_population = []
    for i in range(0, initial_population_size, 2):
        child1, child2 = crossover(parents[i], parents[i+1])
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])
    
    population = new_population

# Find the best individual (highest fitness score)
best_index = np.argmax([calculate_fitness(individual) for individual in population])
best_weights = population[best_index]

print("Optimal asset allocation weights:", best_weights)
print("Expected portfolio return:", np.dot(best_weights, asset_returns))


optimal_weights_percentage_rounded = [round(weight * 100, 2) for weight in best_weights]
print("Optimal asset allocation weights (in percentages, rounded to 2 decimal places):", optimal_weights_percentage_rounded)
