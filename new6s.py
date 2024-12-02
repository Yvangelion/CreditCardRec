import matplotlib.pyplot as plt
import numpy as np
import math

def plot_asymptotic_growth():
    # Values of n
    n_values = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    
    # Asymptotic functions
    o_n = n_values
    o_n2 = n_values**2
    o_n_log_n = n_values * np.log2(n_values)
    o_n_fact = [math.factorial(n) for n in n_values]
    
    # Plotting the functions
    plt.figure(figsize=(12, 8))
    
    plt.plot(n_values, o_n, label='O(n)', marker='o')
    plt.plot(n_values, o_n2, label='O(n^2)', marker='o')
    plt.plot(n_values, o_n_log_n, label='O(n log n)', marker='o')
    plt.plot(n_values, o_n_fact, label='O(n!)', marker='o')
    
    plt.yscale('log')  # Logarithmic scale for better visualization
    plt.title('Asymptotic Growth of O(n), O(n^2), O(n log n), and O(n!)')
    plt.xlabel('n')
    plt.ylabel('Growth (Log Scale)')
    plt.legend()
    plt.grid(True)
    
    plt.show()

# Call the function to plot the graph
plot_asymptotic_growth()
