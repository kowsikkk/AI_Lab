from collections import deque


def greedy_best_first_search(graph, h, start, goal):
    print("\nGreedy Best-First Search")
    open_list = [(start, [start])]
    visited = set()

    while open_list:
        # Sort based on heuristic value
        open_list.sort(key=lambda x: h[x[0]])
        current, path = open_list.pop(0)

        print("Visiting:", current)

        if current == goal:
            print("\nGoal Reached!")
            return path

        visited.add(current)

        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor]))

    print("\nNo Path Found.")
    return None


# ------------------ INPUT SECTION ------------------

graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ").strip()
    neighbors = input(f"Enter neighbors of {node} as (name cost), separated by commas: ").strip()

    neighbor_list = []
    if neighbors:
        for pair in neighbors.split(','):
            name, cost = pair.strip().split()
            neighbor_list.append((name, int(cost)))

    graph[node] = neighbor_list

# Heuristic values
h = {}
print("\nEnter heuristic values:")
for node in graph:
    h[node] = int(input(f"Heuristic for {node}: "))

start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

# ------------------ OUTPUT SECTION ------------------

result = greedy_best_first_search(graph, h, start, goal)

print("\n====================== RESULT ======================")
print("Algorithm: Greedy Best-First Search")

if result:
    print("Path:", " -> ".join(result))
else:
    print("No valid path.")
