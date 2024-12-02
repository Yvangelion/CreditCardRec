import matplotlib.pyplot as plt

# Define the function with O(n) complexity
def linear_function(n):
    return 2 * n

# Input list
n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Calculate the output for each value of n
output_values = [linear_function(n) for n in n_values]

# Plotting the graph
plt.plot(n_values, output_values, marker='o')
plt.title("O(n) Complexity Graph")
plt.xlabel("Input size n")
plt.ylabel("Output")
plt.grid(True)
plt.show()
