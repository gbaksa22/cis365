import heapq

class Node:
    def __init__(self):
        self.parent = None
        self.f = float('inf') #init total cost to infinity
        self.g = float('inf') #init cost from start to infinity
        self.h = 0 #init heuristic estimate  to 0

# Heuristic function
def h_value(node, goal):
    # Manhattan distance - asked ChatGPT for help
    node_x = ord(node[0]) #column letter to ASCII 
    node_y = int(node[1]) #column letter to integer
    goal_x = ord(goal[0]) 
    goal_y = int(goal[1])
    return abs(node_x - goal_x) + abs(node_y - goal_y)

# Trace the path from start to goal
def trace_path(node_details, goal):
    print("The path is:")
    path = []
    current_node = goal

    while node_details[current_node].parent is not None:
        path.append(current_node)
        current_node = node_details[current_node].parent

    path.append(current_node)  # Add the start node
    path.reverse()

    for node in path:
        print(node, "-->", end=" ")
    print("Goal reached")

def a_star(graph, start, goal):
    # Check to make sure nodes are in the graph
    if start not in graph or goal not in graph:
        print("Invalid start or goal node")
        return

    node_details = {node: Node() for node in graph}

    # Initialize start node
    node_details[start].f = 0
    node_details[start].g = 0
    node_details[start].parent = None

    open_set = [] 
    heapq.heappush(open_set, (0, start))  # (f_value, node)

    closed_set = set() # To keep track of nodes that have already been explored

    while open_set:
        # Get the node with the lowest f value
        _, current_node = heapq.heappop(open_set) # Retrieves and removes node with lowest f value

        if current_node == goal:
            trace_path(node_details, goal)
            return

        closed_set.add(current_node)

        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor in closed_set:
                continue

            tentative_g = node_details[current_node].g + 1  # Assume edge weight is 1

            if tentative_g < node_details[neighbor].g: # Checks if new cost is better
                node_details[neighbor].parent = current_node
                node_details[neighbor].g = tentative_g
                node_details[neighbor].h = h_value(neighbor, goal)
                node_details[neighbor].f = node_details[neighbor].g + node_details[neighbor].h

                if neighbor not in [n[1] for n in open_set]:
                    heapq.heappush(open_set, (node_details[neighbor].f, neighbor))

    print("Path not found")
    return

#ChatGPT assisted in setting up the graph
graph = {
    "a1": ["b1", "a2", "b2"],
    "b1": ["a1", "c1", "a2", "b2", "c2"],
    "c1": ["b1", "d1", "c2", "b2", "d2"],
    "d1": ["c1", "e1", "d2", "c2", "e2"],
    "e1": ["d1", "f1", "e2", "d2", "f2"],
    "f1": ["e1", "g1", "f2", "e2", "g2"],
    "g1": ["f1", "h1", "g2", "f2", "h2"],
    "h1": ["g1", "h2", "g2"],

    "a2": ["a1", "b2", "a3", "b1", "b3"],
    "b2": ["b1", "a2", "c2", "b3", "a1", "c1", "a3", "c3"],
    "c2": ["c1", "b2", "d2", "c3", "b1", "d1", "b3", "d3"],
    "d2": ["d1", "c2", "e2", "d3", "c1", "c3", "e1"],  # Removed connection to e3
    "e2": ["d1", "e1", "f1", "d2", "f2", "d3"],  # Removed connection to e3, f3
    "f2": ["e1", "f1", "g1", "e2"],  # Removed connections to g2, f3, g3, e3
    "g2": ["g1", "h2", "f1", "h1", "h3", "g3", "f3"],
    "h2": ["h1", "g2", "h3", "g1", "g3"],

    "a3": ["a2", "b3", "a4", "b2", "b4"],
    "b3": ["b2", "a3", "c3", "b4", "a2", "a4", "c2", "c4"],
    "c3": ["c2", "b3", "d3", "c4", "b2", "b4", "d2", "d4"],
    "d3": ["c3", "c2", "d2", "e2", "c4", "d4"],  # Removed connection to e3 and e4
    "e3": ["e4", "f3", "f4"],  # Removed connections to e2, d2, f2, d3, d4
    "f3": ["f4", "e3", "e4", "g4", "g3", "g2"],  # Removed connection to f2, e2
    "g3": ["g4", "g2", "h2", "h3", "h4", "f4", "f3"],  # Removed connection to f2
    "h3": ["h2", "g2", "g3", "h4", "g4"],

    "a4": ["a3", "b4", "a5", "b3", "b5"],
    "b4": ["b3", "a4", "a3", "c3", "a5", "b5", "c4"],  # Removed connection to c5
    "c4": ["c3", "d4", "b3", "b4", "b5", "d3"],  # Removed connection to c5, d5
    "d4": ["c4", "c3", "d3"],  # Removed connections to d5, e5, e4, e3, c5
    "e4": ["e3", "f3", "f4", "f5", "e5"],  # Removed connection to d3, d4, d5
    "f4": ["f3", "g3", "g4", "f5", "e5", "e4", "e3"],  # Removed connection to g5
    "g4": ["g3", "f3", "f4", "f5", "h3", "h4", "h5"],  # Removed connection to g5
    "h4": ["h3", "g4", "h5", "g3", "g5"],

    "a5": ["a4", "b5", "a6", "b4", "b6"],
    "b5": ["b4", "a5", "a4", "a6", "b6", "c4"],  # Removed connection to c5, c6
    "c5": ["d5", "d6", "c6"],  # Removed connection to all but c6, d5, d6
    "d5": ["c5", "c6", "d6", "e6"],  # Removed connections to e5, d4, e4, c4
    "e5": ["e4", "f4", "f5", "f6", "e6", "d6"],  # Removed connection to d4, d5
    "f5": ["f4", "f6", "e5", "g4", "e4", "e6"],  # Removed connection to g5, g6
    "g5": ["g6", "h4", "h5", "h6"],  # Removed connections to f4, f5, f6, g4
    "h5": ["h4", "g5", "h6", "g4", "g6"],

    "a6": ["a5", "b6", "a7", "b5", "b7"],
    "b6": ["a6", "a5", "a7", "b5", "b7"],  # Removed connections to c5, c6, c7
    "c6": ["c7", "d6", "c5", "d5", "d7"], # Removed connections to b5, b6, b7
    "d6": ["c6", "e6", "d7", "c5", "e5", "d5", "c7", "e7"],
    "e6": ["e5", "f6", "e7", "d5", "f5", "d6", "d7", "f7"],
    "f6": ["f5", "e6", "f7", "e5", "e7"],  # Removed connections to g5, g6, g7
    "g6": ["g7", "g5", "h5", "h6", "h7"],  # Removed connections to f5, f6, f7
    "h6": ["g5", "h5", "g6", "g7"],  # Removed connection to h7

    "a7": ["a6", "b7", "a8", "b6", "b8"],
    "b7": ["a7", "a6", "a8", "b6", "b8"],  # Removed connections to c6, c7, c8
    "c7": ["c6", "d6", "d7"],  # Removed connection to b6, b7, b8, c8, d8
    "d7": ["d6", "c7", "e7", "c6", "e6", "e8"], # Removed connection to c8, d8
    "e7": ["d6", "d7", "d8", "e6", "e8", "f6", "f7", "f8"],
    "f7": ["e6", "e7", "e8", "f6", "f8"],  # Removed connections to g6, g7, g8
    "g7": ["g6", "g8", "h6", "h7", "h8"],  # Removed connections to f7, f8
    "h7": ["g6", "g7", "g8", "h8"],

    "a8": ["a7", "b8", "a9", "b7", "b9"],
    "b8": ["b7", "a8", "c9", "a7", "a9", "b9"],  # Removed connection to c7, c8
    "c8": ["b9", "c9", "d9", "d8"],  # Removed connection to b7, b8, c7, d7
    "d8": ["c8", "c9", "d9", "e7", "e8", "e9"], # removed connection to c7, d7
    "e8": ["d7", "d8", "d9", "e7", "e9", "f7", "f8", "f9"],
    "f8": ["e7", "e8", "e9", "f7", "f9", "g9"],  # Removed connection to g7, g8
    "g8": ["f9", "g7", "g9", "h7", "h8", "h9"],  # Removed connection to f7, f8
    "h8": ["h7", "g8", "h9", "g7", "g9"],

    "a9": ["a8", "b8", "b9"],
    "b9": ["b8", "a9", "c9", "a8", "c8"],
    "c9": ["c8", "b9", "d9", "b8", "d8"],
    "d9": ["d8", "c9", "e9", "c8", "e8"],
    "e9": ["e8", "d9", "f9", "d8", "f8"],
    "f9": ["f8", "e9", "g9", "e8", "g8"],
    "g9": ["g8", "f9", "h9", "f8", "h8"],
    "h9": ["h8", "g8", "g9"]
}

def main():
    start = "a1"
    goal = "h9"
    a_star(graph, start, goal)

if __name__ == "__main__":
    main()

