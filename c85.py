import heapq
import copy

N = 4

# State space tree node
class Node:
    def __init__(self, x, y, assigned, parent):
        self.parent = parent
        self.pathCost = 0  # Cost of the path to reach this node (UB)
        self.cost = 0  # Estimated total cost (LB)
        self.workerID = x
        self.jobID = y
        self.assigned = copy.deepcopy(assigned)
        if y != -1:
            self.assigned[y] = True

# Custom heap class with push and pop functions
class CustomHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, (node.cost, node))

    def pop(self):
        if self.heap:
            _, node = heapq.heappop(self.heap)
            return node
        return None

# Function to allocate a new search tree node
# Here Person x is assigned to job y
def new_node(x, y, assigned, parent):
    return Node(x, y, assigned, parent)

# Function to calculate the least promising cost
# of node after worker x is assigned to job y.
def calculate_cost(cost_matrix, x, y, assigned):
    cost = 0

    # to store unavailable jobs
    available = [True] * N

    # start from the next worker
    for i in range(x + 1, N):
        min_val, min_index = float('inf'), -1

        # do for each job
        for j in range(N):
            # if job is unassigned
            if not assigned[j] and available[j] and cost_matrix[i][j] < min_val:
                # store job number
                min_index = j

                # store cost
                min_val = cost_matrix[i][j]

        # add cost of next worker
        cost += min_val

        # job becomes unavailable
        available[min_index] = False

    return cost

# Print Assignments
def print_assignments(min_node):
    if min_node.parent is None:
        return

    print_assignments(min_node.parent)
    print("Assign Worker {} to Job {}".format(chr(min_node.workerID + ord('A')), min_node.jobID))

# Finds minimum cost using Branch and Bound
def find_min_cost(cost_matrix):
    # Create a priority queue to store live nodes of the search tree
    pq = CustomHeap()

    # initialize heap to dummy node with cost 0
    assigned = [False] * N
    root = new_node(-1, -1, assigned, None)
    root.pathCost = root.cost = 0
    root.workerID = -1

    # Add dummy node to list of live nodes;
    pq.push(root)

    # Initialize the minimum cost with a very large number
    min_cost = float('inf')

    # Finds a live node with least estimated cost,
    # add its children to the list of live nodes and
    # finally deletes it from the list.
    while True:
        # Find a live node with least estimated cost
        min_node = pq.pop()

        # i stores the next worker
        i = min_node.workerID + 1

        # if all workers are assigned a job
        if i == N:
            print_assignments(min_node)
            min_cost = min(min_cost, min_node.cost)
            print(f"Current Min Cost: {min_cost}")
            return min_cost

        # do for each job
        for j in range(N):
            # If unassigned
            if not min_node.assigned[j]:
                # create a new tree node
                child = new_node(i, j, min_node.assigned, min_node)

                # cost for ancestors nodes including the current node (UB)
                child.pathCost = min_node.pathCost + cost_matrix[i][j]

                # calculate its lower bound (LB)
                child.cost = child.pathCost + calculate_cost(cost_matrix, i, j, child.assigned)

                # Display LB and UB for the current node
                print(f"Worker {i}, Job {j} -> LB: {child.cost}, UB: {child.pathCost}")

                # Add child to list of live nodes;
                pq.push(child)

                # Update the minimum cost if a better cost is found
                min_cost = min(min_cost, child.cost)

                # Print current minimum cost
                print(f"BSSF: {min_cost}")

# Driver code
if __name__ == "__main__":
    # x-coordinate represents a Worker
    # y-coordinate represents a Job
    cost_matrix = [
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ]

    # Optimal Cost
    optimal_cost = find_min_cost(cost_matrix)
    if optimal_cost is not None:
        print("\nOptimal Cost is {}".format(optimal_cost))
    else:
        print("\nNo optimal solution found.")
