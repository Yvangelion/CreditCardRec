import time
import matplotlib.pyplot as plt
import numpy as np

# O(n) - Sum of n natural numbers
def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# O(n^2) - Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# O(n log n) - Merge Sort
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

# O(n!) - Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to measure the execution time
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Function to generate an array of size n
def generate_array(n):
    return np.random.randint(1, 100, n)






input_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Lists to store times
times_sum_n = []
times_insertion_sort = []
times_merge_sort = []
times_factorial = []

for n in input_sizes:
    # Measure O(n)
    times_sum_n.append(measure_time(sum_n, n))
    
    # Measure O(n^2)
    arr = generate_array(n)
    times_insertion_sort.append(measure_time(insertion_sort, arr))
    
    # Measure O(n log n)
    arr = generate_array(n)
    times_merge_sort.append(measure_time(merge_sort, arr))
    
    # Measure O(n!)
    times_factorial.append(measure_time(factorial, n))

# Plotting the results
plt.figure(figsize=(14, 8))

plt.plot(input_sizes, times_sum_n, 'o-', label='O(n) - Sum of n natural numbers',linestyle='dotted')
plt.plot(input_sizes, times_insertion_sort, 'o-', label='O(n^2) - Insertion Sort',linestyle='dotted')
plt.plot(input_sizes, times_merge_sort, 'o-', label='O(n log n) - Merge Sort',linestyle='dotted')
plt.plot(input_sizes, times_factorial, 'o-', label='O(n!) - Factorial',linestyle='dotted')

plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Asymptotic Growth Rates')
plt.legend()
plt.grid(True)
plt.show()
