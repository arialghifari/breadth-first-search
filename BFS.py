from queue import Queue

# initialize node
adj_list = {
    "A": ["B", "C"],
    "B": ["D", "G"],
    "C": ["E", "F"],
    "D": [],
    "E": ["G"],
    "F": ["H"],
    "G": ["H"],
    "H": [],
}

# initialize data structure
visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

# initialize node
for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = "A"  # source node
visited[s] = True
level[s] = 0
queue.put(s)  # put node to queue

# start traversing node
while not queue.empty():
    node = queue.get()  # get node from queue
    bfs_traversal_output.append(node)

    # start traversing each child node
    for child_node in adj_list[node]:
        if not visited[child_node]:
            visited[child_node] = True
            parent[child_node] = node
            level[child_node] = level[node] + 1
            queue.put(child_node)  # add child node to queue

# shortest path from source node to target node
t = "H"  # target node
t_print = t

path = []
while t is not None:  # from target node look for its parent
    path.append(t)
    t = parent[t]
path.reverse()

print("Shortest step from A to H is:")
print(str(level[t_print]) + " steps")
print("------------------------------------------")
print("Shortest path is: ")
print(path)
