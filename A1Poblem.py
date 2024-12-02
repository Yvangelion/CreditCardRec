import time
import matplotlib.pyplot as plt
import numpy as np
import math

def sum_of_n(n):
    total_sum = 0
    for current_number  in range(1, n + 1):
        total_sum += current_number
        
    return total_sum



def insertion_sort(array):
    for current_index in  range(1, len(array)):
        key_value = array[current_index]
        
        previous_index = current_index - 1
        while previous_index >= 0  and key_value < array[previous_index]:
            array[previous_index + 1] =   array[previous_index]
            
            previous_index -= 1
        array[previous_index + 1] = key_value
    return array

def merge_sort(array):
    if len(array) > 1:
        middle_index = len(array) // 2
        left_half = array[:middle_index ]  
        
        right_half = array[middle_index:]

        merge_sort( left_half)
        merge_sort(right_half)

        left_index = right_index = merge_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                
                array[merge_index] = left_half[left_index]
                left_index += 1
            else:
                array[merge_index] = right_half[right_index]
                
                right_index += 1
            merge_index += 1

        while left_index < len(left_half):
            array[merge_index] = left_half[left_index]
            left_index += 1
            merge_index += 1
            
            

        while right_index < len(right_half):
            array[merge_index] =   right_half[right_index]
            right_index += 1
            merge_index  += 1

    return array

def facto(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n *  facto(n - 1)


n_input = [10, 20, 30, 40,  50,  60, 70, 80, 90, 100]


sum_times = []
for n in n_input:
    
    start_time = time.time()
    sum_of_n(n)
    end_time = time.time()
    sum_times.append(end_time - start_time)


insertion_times = []
for n in n_input: 
    value = list(range(n, 0, -1))  
    start_time = time.time()
    
    insertion_sort(value)
    end_time =   time.time()
    insertion_times.append(end_time - start_time)


merge_times = []
for n in n_input:
    value =   list(range(n, 0, -1))  
    start_time = time.time()
    merge_sort(value)
    end_time = time.time()
    
    merge_times.append(end_time - start_time)

facto_times = []
for n in n_input:
    start_time   = time.time()
    facto(n)
    end_time = time.time()
    facto_times.append(end_time - start_time)




n_log_n = [n * np.log2(n) for n in n_input]
n_square = [n**2 for n in n_input]
facto_n = [math.factorial(n)  for n in n_input]



plt.figure(figsize=(10, 7))


#1
plt.subplot(2, 2, 1)
plt.plot(n_input, sum_times, 'r-o', label="Actual Runtime")
plt.plot(n_input, n_input, 'b--', label="O(n)")
plt.xlabel('Input Size n')
plt.ylabel('Time')
plt.title('O(n) Runtime vs Asymptotic Growth')
plt.legend()

#2
plt.subplot(2, 2, 2)
plt.plot(n_input, insertion_times, 'r-o', label="Actual Runtime")
plt.plot(n_input, n_square, 'b--', label="O(n^2)")
plt.xlabel('Input Size n')
plt.ylabel('Time')
plt.title('O(n^2) Runtime vs Asymptotic Growth')
plt.legend()

#3
plt.subplot(2, 2, 3)
plt.plot(n_input, merge_times, 'r-o', label="Actual Runtime")
plt.plot(n_input, n_log_n, 'b--', label="O(n log n)")
plt.xlabel('Input Size n')
plt.ylabel('Time')
plt.title('O(n log n) Runtime vs Asymptotic Growth')
plt.legend()

#4
plt.subplot(2, 2, 4)
plt.plot(n_input, facto_times, 'r-o', label="Actual Runtime")
plt.plot(n_input, facto_n, 'b--', label="O(n!)")
plt.xlabel('Input Size n')
plt.ylabel('Time')
plt.title('O(n!) Runtime vs Asymptotic Growth')
plt.legend()

plt.tight_layout()
plt.show()
