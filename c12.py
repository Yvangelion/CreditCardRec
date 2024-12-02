# A Python program to count all subsets with a given sum.

# dp[i][j] is going to store True if sum j is
# possible with array elements from 0 to i.
dp = [[]]

def display(v):
    print(v)

# A recursive function to print all subsets with
# the help of dp[][]. list p[] stores current subset.
def printSubsetsRec(arr, i, sum, p, depth=0):

    # Print the recursive tree structure
    indent = " " * (depth * 4)  # Indentation to represent depth
    print(f"{indent}Called with i={i}, sum={sum}, current subset={p}")

    # If we reached end and sum is non-zero, print the subset
    if (i == 0 and sum != 0 and dp[0][sum]):
        p.append(arr[i])
        display(p)
        p = []
        return

    # If sum becomes 0, print the subset
    if (i == 0 and sum == 0):
        display(p)
        p = []
        return

    # If the given sum can be achieved after ignoring the current element.
    if (dp[i-1][sum]):
        # Create a new list to store the path and recurse
        b = []
        b.extend(p)
        printSubsetsRec(arr, i-1, sum, b, depth + 1)

    # If the given sum can be achieved after considering the current element.
    if (sum >= arr[i] and dp[i-1][sum-arr[i]]):
        p.append(arr[i])
        printSubsetsRec(arr, i-1, sum-arr[i], p, depth + 1)

# Prints all subsets of arr[0..n-1] with sum 0.
def printAllSubsets(arr, n, sum):
    if (n == 0 or sum < 0):
        return

    # Sum 0 can always be achieved with 0 elements
    global dp
    dp = [[False for i in range(sum+1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    # Sum arr[0] can be achieved with a single element
    if (arr[0] <= sum):
        dp[0][arr[0]] = True

    # Fill rest of the entries in dp[][]
    for i in range(1, n):
        for j in range(0, sum + 1):
            if (arr[i] <= j):
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i]])
            else:
                dp[i][j] = dp[i - 1][j]

    if (dp[n-1][sum] == False):
        print("There are no subsets with sum", sum)
        return

    # Now recursively traverse dp[][] to find all paths from dp[n-1][sum]
    p = []
    printSubsetsRec(arr, n-1, sum, p)

# This code is contributed by Lovely Jain

if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    n = len(arr)
    sum = 15
    printAllSubsets(arr, n, sum)
