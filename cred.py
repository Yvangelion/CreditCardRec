import numpy as np
import time

# binary search
def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid  
        elif data[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    return -1  

# interpolation search 
def interpolation_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high and target >= data[low] and target <= data[high]:
        if low == high:
            if data[low] == target:
                return low
            return -1
        pos = low + int(((high - low) * (target - data[low]) / (data[high] - data[low])))
        if data[pos] == target:
            return pos  
        elif data[pos] < target:
            low = pos + 1  
        else:
            high = pos - 1  
    return -1

# exponential search 
def exponential_search(data, target):
    if len(data) == 0:
        return -1
    if data[0] == target:
        return 0
    index = 1
    while index < len(data) and data[index] <= target:
        index *= 2
    return binary_search_range(data, target, index // 2, min(index, len(data)))

def binary_search_range(data, target, left, right):
    while left < right:
        mid = left + (right - left) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1

# generate datasets
np.random.seed(42) # force the same datasets for consistent runs
uniform_data = np.linspace(10, 100, 1_000_000)
skewed_data = np.random.exponential(scale=20, size=1_000_000)
non_uniform_data = np.concatenate([
    np.random.uniform(10, 30, 333_334),
    np.random.uniform(60, 80, 333_333),
    np.random.uniform(90, 100, 333_333)
])
datasets = {"Uniform": uniform_data, "Skewed": skewed_data, "NonUniform": non_uniform_data}

# target value
target = 60

# inject target in the datasets
for data in datasets.values():
    data[500_000] = target
    data.sort()

# perform search
search_methods = {
    "Binary Search": binary_search,
    "Interpolation Search": interpolation_search,
    "Exponential Search": exponential_search,
}
results = {}

# compute execution times

# if computer is too fast use this
print(f"Execution Time Over 10k runs")
iterations = 10_000  
for method_name, method in search_methods.items():
    print(f"\n{method_name} Execution Time:")
    for dataset_name, dataset in datasets.items():
        total_time = 0
        for _ in range(iterations):
            start_time = time.time_ns()  
            result_index = method(dataset, target)
            end_time = time.time_ns() 
            total_time += (end_time - start_time)
        avg_time_ns = total_time // iterations
        print(f"{dataset_name}: {avg_time_ns} ns")

print("------------------------------------------------------")
print(f"\nExecution Time Over 1 run")
# for normal execution without avg of 10k runs
for typem, method in search_methods.items():
    print(f"\n{typem} Execution Time:")
    for dataset_name, dataset in datasets.items():
        start_time = time.time_ns()  
        result_index = method(dataset, target)
        end_time = time.time_ns() 
        execution_time_ns = end_time - start_time 
        print(f"{dataset_name}: {execution_time_ns} ns")
