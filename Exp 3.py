
from collections import deque
from math import gcd
def bfs(cap_a: int, cap_b: int, target: int):
    """Return the shortest sequence of states to reach `target`
    in either jug, or None if impossible."""
    start = (0, 0)                
    queue = deque([(start, [])])     
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path + [((a, b), "✔ Goal reached")]
        next_states = [
            ((cap_a, b),           "Fill A"),
            ((a, cap_b),           "Fill B"),
            ((0, b),               "Empty A"),
            ((a, 0),               "Empty B"),
            # pour A → B
            (pour(a, b, cap_b),    "Pour A → B"),
            # pour B → A
            (pour(b, a, cap_a)[::-1], "Pour B → A")
        ]
        for (na, nb), action in next_states:
            if (na, nb) not in visited:
                visited.add((na, nb))
                queue.append(((na, nb), path + [((a, b), action)]))
    return None
def pour(src: int, dst: int, dst_cap: int):
    """Return (src', dst') after pouring src → dst as much as possible."""
    amount = min(src, dst_cap - dst)
    return src - amount, dst + amount
def show_solution(solution, cap_a, cap_b):
    if not solution:
        print("No solution exists for the given inputs.")
        return
    print(f"\nSteps ({len(solution)-1} moves):")
    for (a, b), action in solution:
        print(f"{action:<12s} ->  A:{a:2d}/{cap_a}  B:{b:2d}/{cap_b}")
def main():
    try:
        cap_a, cap_b, target = map(int, input("Enter A B T (e.g. 3 5 4): ").split())
    except ValueError:
        print("❌  Please enter three integers separated by spaces.")
        return

    if target > max(cap_a, cap_b):
        print("❌  Target cannot exceed both jug capacities.")
        return
    if target % gcd(cap_a, cap_b):
        print("❌  Target is not reachable: it is not a multiple of gcd(A,B).")
        return
    solution = bfs(cap_a, cap_b, target)
    show_solution(solution, cap_a, cap_b)
if __name__ == "__main__":
    main()
