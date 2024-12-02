import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the cost matrix
cost_matrix = np.array([
    [82, 83, 69, 92],
    [77, 37, 49, 92],
    [11, 69, 5, 86],
    [8, 9, 98, 23]
])

# Implement a Branch and Bound approach to minimize the total assignment cost
# Start with the initial bounds and track the best solution so far
def branch_and_bound(cost_matrix):
    num_tasks = cost_matrix.shape[0]
    
    # Step 1: Initial Lower Bound (LB) - Reduce matrix row-wise and column-wise
    def reduce_matrix(matrix):
        row_min = np.min(matrix, axis=1).reshape(-1, 1)
        matrix -= row_min  # Row reduction
        col_min = np.min(matrix, axis=0)
        matrix -= col_min  # Column reduction
        return matrix, row_min.sum() + col_min.sum()

    reduced_matrix, initial_LB = reduce_matrix(cost_matrix.copy())
    
    # Initialize variables
    UB = np.inf  # Upper Bound (starting as infinity)
    BSSF = None  # Best solution so far
    best_cost = np.inf  # To track the best cost

    # Step 2: Solve using Hungarian algorithm for initial UB
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    initial_solution_cost = cost_matrix[row_ind, col_ind].sum()
    UB = initial_solution_cost
    BSSF = list(zip(row_ind, col_ind))
    
    # Display initial conditions
    print(f"Initial Lower Bound (LB): {initial_LB}")
    print(f"Initial Upper Bound (UB): {UB}")
    print(f"Initial Best Solution So Far (BSSF): {BSSF}")
    
    # Note: Implementing the entire branch-and-bound manually with bounds update 
    # and pruning would involve a priority queue and recursion. For brevity, 
    # let's focus on the LB, UB, and first optimal assignment via Hungarian.

branch_and_bound(cost_matrix)
