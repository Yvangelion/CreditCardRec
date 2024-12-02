import numpy as np

def tsp_branch_and_bound(distance_matrix):
    n = len(distance_matrix)
    best_cost = float('inf')
    best_path = []
    path_costs = []  # List to store all considered path costs

    # Helper function to reduce the matrix and compute the cost
    def reduce_matrix(matrix):
        cost = 0
        # Row reduction
        for i in range(n):
            min_value = min(matrix[i])
            if min_value != float('inf'):
                cost += min_value
                matrix[i] -= min_value
        # Column reduction
        for j in range(n):
            min_value = min(matrix[:, j])
            if min_value != float('inf'):
                cost += min_value
                matrix[:, j] -= min_value
        return cost

    # Helper function for branch and bound
    def branch_and_bound(path, current_cost, matrix):
        nonlocal best_cost, best_path, path_costs
        current_city = path[-1]
        
        # Check if we have a complete path
        if len(path) == n:
            final_cost = current_cost + distance_matrix[current_city][path[0]]
            path_costs.append((path + [path[0]], final_cost))  # Store path and its cost
            if final_cost < best_cost:
                best_cost = final_cost
                best_path = path[:]
            return
        
        # Iterate over all possible next cities
        for next_city in range(n):
            if next_city not in path and matrix[current_city][next_city] != float('inf'):
                # Make a copy of the matrix for branching
                temp_matrix = matrix.copy()
                # Add the cost of going to the next city
                new_cost = current_cost + temp_matrix[current_city][next_city]
                # Set the outgoing and incoming paths of current city to infinity
                temp_matrix[current_city, :] = float('inf')
                temp_matrix[:, next_city] = float('inf')
                temp_matrix[next_city][current_city] = float('inf')
                # Reduce the matrix and get the reduction cost
                reduction_cost = reduce_matrix(temp_matrix)
                new_cost += reduction_cost
                # Check if this path is promising
                if new_cost < best_cost:
                    branch_and_bound(path + [next_city], new_cost, temp_matrix)

    # Initial matrix reduction and setup
    initial_matrix = np.array(distance_matrix, dtype=float)
    initial_cost = reduce_matrix(initial_matrix)
    # Start with the first city
    branch_and_bound([0], initial_cost, initial_matrix)
    
    # After completing the branch and bound, return the best cost, best path, and all paths considered
    return best_cost, best_path, path_costs

# Distance matrix
distance_matrix = [
    [0, 29, 20, 21, 16],
    [29, 0, 15, 17, 18],
    [20, 15, 0, 28, 23],
    [21, 17, 28, 0, 25],
    [16, 18, 23, 25, 0]
]

# Solve TSP
min_cost, min_path, path_costs = tsp_branch_and_bound(distance_matrix)
print("Minimum Cost:", min_cost)
print("Minimum Path:", min_path + [min_path[0]])

# Print all the considered paths and their costs
print("\nConsidered Paths and Costs:")
for path, cost in path_costs:
    print(f"Path: {path}, Cost: {cost}")
