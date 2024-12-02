import time
import matplotlib.pyplot as plt
import numpy as np

# Algorithms to be tested

# 1. Sum of first n natural numbers (O(n))
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 2. Insertion Sort (O(n^2))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 3. Mergesort (O(n log n))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 4. Factorial (O(n!))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input size
n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Arrays to store the runtimes
time_sum = []
time_insertion = []
time_merge = []
time_factorial = []

# Measure time for each algorithm
for n in n_values:
    arr = list(np.random.randint(0, 100, n))  # Create a random array for sorting algorithms

    # Time for sum of natural numbers
    start_time = time.time()
    sum_natural_numbers(n)
    time_sum.append(time.time() - start_time)

    # Time for insertion sort
    start_time = time.time()
    insertion_sort(arr.copy())
    time_insertion.append(time.time() - start_time)

    # Time for merge sort
    start_time = time.time()
    merge_sort(arr.copy())
    time_merge.append(time.time() - start_time)

    # Time for factorial
    start_time = time.time()
    factorial(n)
    time_factorial.append(time.time() - start_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, time_sum, label="Sum of natural numbers (O(n))", marker='o')
plt.plot(n_values, time_insertion, label="Insertion Sort (O(n^2))", marker='o')
plt.plot(n_values, time_merge, label="Merge Sort (O(n log n))", marker='o')
plt.plot(n_values, time_factorial, label="Factorial (O(n!))", marker='o')

plt.xlabel('Input Size (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime vs Asymptotic Growth')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Logarithmic scale for better visualization
plt.show()
