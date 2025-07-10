from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return traversal
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    print("BFS Traversal starting from node", start_node, "is:")
    print(bfs(graph, start_node))
