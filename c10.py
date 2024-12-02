# Define the backtracking function
def find_subsets(nums, target, index=0, current_subset=[], current_sum=0, depth=0):
    """
    Backtracking function to find subsets that sum up to the target.
    """
    global solutions, backtrack_count, all_paths
    
    # Record the current path
    all_paths.append((depth, list(current_subset)))  # Append the current path with its depth for tree representation
    
    # If the current sum matches the target, record the solution
    if current_sum == target:
        solutions.append(list(current_subset))  # Record the solution if target is met
        return
    
    # If the sum exceeds the target or we have processed all elements, backtrack
    if current_sum > target or index >= len(nums):
        backtrack_count += 1  # Increment backtrack count
        return

    # Include the current element and recurse (with depth + 1 for the next level of recursion)
    current_subset.append(nums[index])  # Include the element at the current index
    find_subsets(nums, target, index + 1, current_subset, current_sum + nums[index], depth + 1)  # Move forward with the updated subset and sum
    
    # Exclude the current element and backtrack (with depth + 1)
    current_subset.pop()  # Remove the element to backtrack
    find_subsets(nums, target, index + 1, current_subset, current_sum, depth + 1)  # Move forward without including the current element

# Initialize the variables
nums = [2, 3, 5, 6, 8, 10]  # List of numbers
target = 15  # Target sum to find subsets
solutions = []  # To store viable solutions
backtrack_count = 0  # To count the number of backtracks
all_paths = []  # To record all paths explored

# Call the backtracking function
find_subsets(nums, target)

# Prepare the output
print("Solutions:")
print(solutions)

print("\nBacktrack Count:")
print(backtrack_count)

# Print All Paths Explored with a tree structure
print("\nAll Paths Explored (Recursive Tree):")
current_depth = 0
for depth, path in all_paths:
    indent = "  " * depth  # Indent based on depth for tree-like structure
    print(f"{indent}Path at Depth {depth}: {path}")
