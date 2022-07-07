from queue import Queue

# Initialize node
node_list = {
    "A": ["B", "C"],
    "B": ["D", "G"],
    "C": ["E", "F"],
    "D": [],
    "E": ["G"],
    "F": ["H"],
    "G": ["H"],
    "H": [],
}

# Initialize data structure
visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

# Initialize node
for node in node_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

# Start traversing node from source node
s = "A"  # source node

try:
    visited[s] = True
    level[s] = 0
    queue.put(s)  # put node to queue

    while not queue.empty():
        node = queue.get()  # get first node from queue
        bfs_traversal_output.append(node)  # put visited node to traversal

        # start traversing each child node
        for child_node in node_list[node]:
            if not visited[child_node]:
                visited[child_node] = True
                parent[child_node] = node
                level[child_node] = level[node] + 1
                queue.put(child_node)  # add child node to queue
except:
    print("Source node " + s + " is not available")
    exit()


# Find the shortest path from source node to target node
t = "H"  # target node
t_for_print = t

try:
    path = []
    while t is not None:  # from target node look for its parent
        path.append(t)
        t = parent[t]
    path.reverse()

    print("BFS Traversal:")
    print(bfs_traversal_output)
    print("------------------------------------------")
    print("Shortest step:")
    print(str(level[t_for_print]) + " steps")
    print("------------------------------------------")
    print("Shortest path: ")
    print(path)
except:
    print("Target node " + t + " is not available")
    exit()
