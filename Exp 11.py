
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW', 'T'],
    'T': ['V']
}
colors = ['Red', 'Green', 'Blue']

def is_valid(state, region, color):
    for neighbor in neighbors[region]:
        if neighbor in state and state[neighbor] == color:
            return False
    return True

def backtrack(state):
    if len(state) == len(neighbors):
        return state
    unassigned = [r for r in neighbors if r not in state][0]

    for color in colors:
        if is_valid(state, unassigned, color):
            state[unassigned] = color
            result = backtrack(state)
            if result:
                return result
            del state[unassigned] 

    return None
solution = backtrack({})
if solution:
    print("Solution:")
    for region in sorted(solution):
        print(f"{region}: {solution[region]}")
else:
    print("No solution found.")
