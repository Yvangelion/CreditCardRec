import time
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the sum of n natural numbers using a for loop
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Function to perform insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function to perform merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Function to calculate factorial recursively
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Function to measure runtime
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Input sizes
n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Lists to store runtimes
runtimes_sum = []
runtimes_insertion = []
runtimes_merge = []
runtimes_factorial = []

# Measure runtime for each algorithm
for n in n_values:
    # For sum of n natural numbers
    runtimes_sum.append(measure_time(sum_natural_numbers, n))
    
    # For insertion sort
    arr = list(range(n, 0, -1))  # Worst case: reverse sorted array
    runtimes_insertion.append(measure_time(insertion_sort, arr))
    
    # For merge sort
    arr = list(range(n, 0, -1))  # Worst case: reverse sorted array
    runtimes_merge.append(measure_time(merge_sort, arr))
    
    # For factorial
    runtimes_factorial.append(measure_time(factorial, n))

# Plotting the results
plt.figure(figsize=(10, 6))

# Plot runtimes
plt.plot(n_values, runtimes_sum, label='Sum of N Natural Numbers (O(n))')
plt.plot(n_values, runtimes_insertion, label='Insertion Sort (O(n^2))')
plt.plot(n_values, runtimes_merge, label='Merge Sort (O(n log n))')
plt.plot(n_values, runtimes_factorial, label='Factorial (O(n!))')

# Labels and title
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Runtime vs Asymptotic Growth')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
