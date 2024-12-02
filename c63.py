import numpy as np
import heapq

# Distance matrix
dist = np.array([
    [0, 29, 20, 21, 16],
    [29, 0, 15, 17, 18],
    [20, 15, 0, 28, 23],
    [21, 17, 28, 0, 25],
    [16, 18, 23, 25, 0]
], dtype=float)  # Explicitly set dtype to float


# Reduce the matrix and compute the cost
def reduce_matrix(matrix):
    # Copy the matrix to avoid modifying the original
    reduced_matrix = matrix.copy()
    total_reduction_cost = 0

    # Row reduction
    for i in range(len(reduced_matrix)):
        min_val = np.min(reduced_matrix[i])
        if min_val != np.inf and min_val > 0:
            reduced_matrix[i] -= min_val
            total_reduction_cost += min_val

    # Column reduction
    for j in range(len(reduced_matrix[0])):
        min_val = np.min(reduced_matrix[:, j])
        if min_val != np.inf and min_val > 0:
            reduced_matrix[:, j] -= min_val
            total_reduction_cost += min_val

    return reduced_matrix, total_reduction_cost

# Branch and Bound for TSP
def branch_and_bound_tsp(matrix):
    n = len(matrix)
    pq = []  # Priority queue to store nodes
    min_cost = float('inf')  # Minimum cost found so far
    best_path = None

    # Initial reduction and add the root node to the queue
    reduced_matrix, cost = reduce_matrix(matrix)
    root_node = (cost, 0, [0], reduced_matrix)
    heapq.heappush(pq, root_node)

    while pq:
        # Get the node with the smallest cost
        current_cost, current_city, current_path, current_matrix = heapq.heappop(pq)

        # If the path includes all cities, complete the tour and update the best path
        if len(current_path) == n:
            final_cost = current_cost + matrix[current_path[-1]][current_path[0]]
            if final_cost < min_cost:
                min_cost = final_cost
                best_path = current_path + [current_path[0]]
            continue

        # Explore child nodes (next cities)
        for next_city in range(n):
            if next_city not in current_path and current_matrix[current_city][next_city] != np.inf:
                # Create a new reduced matrix for the child node
                child_matrix = current_matrix.copy()
                child_matrix[current_city, :] = np.inf
                child_matrix[:, next_city] = np.inf
                child_matrix[next_city][current_city] = np.inf

                # Reduce the matrix and compute the cost
                reduced_child_matrix, reduction_cost = reduce_matrix(child_matrix)
                child_cost = current_cost + current_matrix[current_city][next_city] + reduction_cost

                # Add the child node to the priority queue
                heapq.heappush(pq, (child_cost, next_city, current_path + [next_city], reduced_child_matrix))

    return min_cost, best_path

# Solve the TSP
min_cost, best_path = branch_and_bound_tsp(dist)
min_cost, best_path

print(min_cost)
print(best_path)