def dfs(graph, start, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(start)
    traversal.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)

    return traversal
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    print("DFS Traversal starting from node", start_node, "is:")
    print(dfs(graph, start_node))
