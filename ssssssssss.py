import numpy as np

# Define parameters
NUM_ASSETS = 4
NUM_GENERATIONS = 100_000

# Define risk tolerance levels and their corresponding penalties, mutation rates, and population sizes
risk_penalties = {"high": 1.0, "medium": 0.5, "low": 0.1}
mutation_rates = {"high": 0.2, "medium": 0.1, "low": 0.05}
population_sizes = {"high": 30, "medium": 20, "low": 10}

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

def genetic_algorithm(target_allocation, risk_tolerance, investment_length):
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

    print("\nOptimal asset allocation:")
    print("US Total Market:", best_allocation[0])
    print("International Funds Total Market:", best_allocation[1])
    print("Bonds:", best_allocation[2])
    print("Cash:", best_allocation[3])
    print(("Final fitness:", best_fitness))

def get_risk_tolerance(age):
    """Determine risk tolerance based on age and investment length."""
    if age < 30:
        target_allocation = np.array([0.70, 0.20, 0.5, 0.5])
        investment_length = 30
        return "high", target_allocation, investment_length
    elif 30 <= age <= 50:
        target_allocation = np.array([0.25, 0.25, 0.25, 0.25])
        investment_length = 20
        return "medium", target_allocation, investment_length
    else:
        target_allocation = np.array([0.15, 0.15, 0.60, 0.10])
        investment_length = 10
        return "low", target_allocation, investment_length

if __name__ == "__main__":
    ages = [21, 31, 55, 66, 80]
    for age in ages:
        print(f"\n--- Age: {age} ---")
        risk_tolerance, target_allocation, investment_length = get_risk_tolerance(age)
        print("Based on your age, your risk tolerance is:", risk_tolerance)
        print("Your investment length is:", investment_length)
        
        print(f"\nRisk Tolerance: {risk_tolerance}")
        genetic_algorithm(target_allocation, risk_tolerance, investment_length)
        print("\n")
