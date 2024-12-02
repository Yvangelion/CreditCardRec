import time
import math
import matplotlib.pyplot as plt

# Helper function to measure runtime
def measure_runtime(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# 1. Sum of Natural Numbers (O(n))
def sum_natural_numbers(n):
    total = 0
    for i in range(n):
        total += i
    return total

# 2. Insertion Sort (O(n²))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 3. Merge Sort (O(n log n))
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

# 4. Factorial Function (O(n!))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Input sizes
input_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Measure runtime for each algorithm
sum_times = []
insertion_sort_times = []
merge_sort_times = []
factorial_times = []

for n in input_sizes:
    # Sum of Natural Numbers
    sum_time = measure_runtime(sum_natural_numbers, n)
    sum_times.append(sum_time)
    
    # Insertion Sort
    arr = list(range(n, 0, -1))
    insertion_sort_time = measure_runtime(insertion_sort, arr.copy())
    insertion_sort_times.append(insertion_sort_time)
    
    # Merge Sort
    arr = list(range(n, 0, -1))
    merge_sort_time = measure_runtime(merge_sort, arr.copy())
    merge_sort_times.append(merge_sort_time)
    
    # Factorial Function
    if n <= 20:  # Limit for factorial due to factorial growth
        factorial_time = measure_runtime(factorial, n)
        factorial_times.append(factorial_time)
    else:
        factorial_times.append(None)  # Skip for large n

# Compute asymptotic growth rates
n_values = input_sizes
O_n = [n for n in n_values]
O_n2 = [n**2 for n in n_values]
O_nlogn = [n * math.log(n, 2) for n in n_values]
O_nfact = [math.factorial(n) if n <= 20 else float('inf') for n in n_values]

# Plot the results
plt.figure(figsize=(14, 10))

# Plot for Actual Runtime
plt.subplot(2, 2, 1)
plt.plot(n_values, sum_times, label='Sum of Natural Numbers (O(n))', marker='o')
plt.plot(n_values, insertion_sort_times, label='Insertion Sort (O(n²))', marker='o')
plt.plot(n_values, merge_sort_times, label='Merge Sort (O(n log n))', marker='o')
plt.plot(n_values, factorial_times, label='Factorial (O(n!))', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Actual Runtime of Algorithms')
plt.legend()

# Plot for Asymptotic Growth Rates
plt.subplot(2, 2, 2)
plt.plot(n_values, O_n, label='O(n)', marker='o')
plt.plot(n_values, O_n2, label='O(n²)', marker='o')
plt.plot(n_values, O_nlogn, label='O(n log n)', marker='o')
plt.plot(n_values, O_nfact, label='O(n!)', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Growth Rate')
plt.title('Asymptotic Growth Rates')
plt.yscale('log')  # Use log scale to handle wide range
plt.legend()

plt.tight_layout()
plt.show()
