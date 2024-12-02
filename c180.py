import numpy as np
from scipy.optimize import linprog

# Objective function: maximize z = 3x + 5y, so we minimize -z
c = [-3, -5]

# Coefficients for inequality constraints:
# x + 2y <= 8
# 4x + y <= 12
A = [[1, 2], [4, 1]]
b = [8, 12]

# Bounds for x and y (non-negative integers)
x_bounds = (0, None)
y_bounds = (0, None)

# Function to solve LP relaxation
def solve_lp():
    result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    return result

# Function to apply Branch and Bound method
def branch_and_bound():
    # First, solve the LP relaxation (relaxed solution without integer constraints)
    lp_solution = solve_lp()

    if lp_solution.success:
        print(f"LP Relaxation Solution: x = {lp_solution.x[0]}, y = {lp_solution.x[1]}, z = {-lp_solution.fun}")
        
        # Check if the LP solution is already integer
        if lp_solution.x[0].is_integer() and lp_solution.x[1].is_integer():
            print(f"Integer Solution: x = {int(lp_solution.x[0])}, y = {int(lp_solution.x[1])}, z = {-lp_solution.fun}")
            return int(lp_solution.x[0]), int(lp_solution.x[1]), -lp_solution.fun
        else:
            # Branching step: Try rounding x and y down or up and solve again
            x_branch_low = int(np.floor(lp_solution.x[0]))
            y_branch_low = int(np.floor(lp_solution.x[1]))

            # Check the branch for integer solutions
            print(f"Branching: Lower Bound Solution: x = {x_branch_low}, y = {y_branch_low}")
            lower_bound = evaluate_solution(x_branch_low, y_branch_low)

            # Return the best integer solution found
            return lower_bound
    else:
        print("LP Relaxation failed to find a solution.")
        return None

# Evaluate solution by checking constraints and calculating the objective value
def evaluate_solution(x, y):
    if x + 2*y <= 8 and 4*x + y <= 12:
        z = 3*x + 5*y
        print(f"Valid solution: x = {x}, y = {y}, z = {z}")
        return x, y, z
    else:
        print(f"Invalid solution: x = {x}, y = {y}")
        return None

# Main execution
if __name__ == "__main__":
    branch_and_bound()
