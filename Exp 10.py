from heapq import heappush, heappop
def a_star(graph, h, start, goal):
    """Return (cost, path) from start to goal using A*."""
    open_set = []                          
    heappush(open_set, (h[start], 0, start, None))

    came_from = {}                        
    g_cost = {start: 0}                    

    while open_set:
        f, g, node, parent = heappop(open_set)

        if node in came_from:          
            continue
        came_from[node] = parent           

        if node == goal:                 
            path = []
            while node is not None:
                path.append(node)
                node = came_from[node]
            return g, path[::-1]         

        for nei, w in graph[node]:       
            new_g = g + w
            if nei not in g_cost or new_g < g_cost[nei]:
                g_cost[nei] = new_g
                f = new_g + h[nei]
                heappush(open_set, (f, new_g, nei, node))

    return None, []                       

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

h = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

if __name__ == "__main__":
    start, goal = 'A', 'D'
    cost, path = a_star(graph, h, start, goal)
    if path:
        print(f"Shortest path: {' → '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")
