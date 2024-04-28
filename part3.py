import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import random

class Engine:
    def __init__(self, start_date, benchmark=["SPY"], portfolio=[], data_file="", weights=[]):
        self.start_date = start_date
        self.benchmark = benchmark
        self.portfolio = portfolio
        self.data_file = data_file
        self.weights = weights
    
    def load_data(self):
        data = pd.read_csv(self.data_file, parse_dates=['Date'], index_col='Date')
        return data.loc[self.start_date:]
    
    def calculate_returns(self):
        data = self.load_data()
        portfolio_returns = pd.DataFrame(index=data.index)
        for asset, weight in zip(self.portfolio, self.weights):
            asset_returns = data[asset].pct_change().rename(asset)
            portfolio_returns = portfolio_returns.join(asset_returns)
        portfolio_returns['Portfolio'] = (portfolio_returns[self.portfolio] * self.weights).sum(axis=1)
        return portfolio_returns.dropna()
    
    def predict_optimal_allocation(self):
        data = self.load_data()
        X = data[self.portfolio]
        y = data[self.benchmark[0]]  # Predict against benchmark
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return mse, model.feature_importances_
    
    def returns(engine):
        returns = engine.calculate_returns()
        sharpe_ratio = (returns.mean() / returns.std()) * (252 ** 0.5)
        cumulative_returns = (1 + returns).cumprod() - 1
        total_cumulative_return = cumulative_returns['Portfolio'].iloc[-1]  # Total cumulative return of the portfolio at the last date
        data = {
            'Sharpe Ratio': sharpe_ratio,
            'Total Cumulative Return': total_cumulative_return
        }
        return data

class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def initialize_population(self, n_assets):
        population = []
        for _ in range(self.population_size):
            weights = np.random.random(n_assets)
            weights /= np.sum(weights)  # Normalize weights to sum to 1
            population.append(weights)
        return population

    def fitness(self, population, engine):
        fitness_scores = []
        for weights in population:
            engine.weights = weights
            mse, _ = engine.predict_optimal_allocation()
            fitness_scores.append(1 / (1 + mse))  # Invert MSE to get fitness score
        return np.array(fitness_scores)

    def selection(self, population, scores):
        selected_indices = np.random.choice(len(population), size=self.population_size, replace=True, p=scores/scores.sum())
        return [population[i] for i in selected_indices]

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2

    def mutation(self, population):
        for i in range(len(population)):
            if random.random() < self.mutation_rate:
                mutation_point = random.randint(0, len(population[i]) - 1)
                population[i][mutation_point] = random.random()
                population[i] /= np.sum(population[i])  # Normalize weights
        return population

    def optimize(self, engine):
        n_assets = len(engine.portfolio)
        population = self.initialize_population(n_assets)
        for _ in range(self.generations):
            scores = self.fitness(population, engine)
            selected_population = self.selection(population, scores)
            children = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = random.sample(selected_population, 2)
                child1, child2 = self.crossover(parent1, parent2)
                children.append(child1)
                children.append(child2)
            population = self.mutation(children)
            # Enforce sum to 1 constraint
            population = [weights / np.sum(weights) for weights in population]
        best_solution = population[np.argmax(scores)]
        return best_solution



if __name__ == "__main__":    
    # Example usage
    portfolio = Engine(
        start_date="2018-01-01",
        benchmark=["SPY"],
        portfolio=["AAPL", "BABA", "CASH", "GUY"],
        data_file="financial_data.csv",
        weights=[0.21798563,0.25281468,0.39330413,0.13589556]
    )

    print(Engine.returns(portfolio))
    genetic_algo = GeneticAlgorithm(population_size=100, generations=50, mutation_rate=0.1)
    optimized_weights = genetic_algo.optimize(portfolio)
    print(optimized_weights)
    portfolio.weights = optimized_weights
    print(portfolio.predict_optimal_allocation())
