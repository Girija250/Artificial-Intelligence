from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(dist)

cities = list(range(1, n))
min_path = []
min_cost = float('inf')

for perm in permutations(cities):
    path = [0] + list(perm) + [0]  
    cost = sum(dist[path[i]][path[i+1]] for i in range(n))

    if cost < min_cost:
        min_cost = cost
        min_path = path

print("Shortest tour:", ' → '.join(map(str, min_path)))
print("Total cost:", min_cost)
