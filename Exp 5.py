from collections import deque
def is_valid(m_left, c_left, m_right, c_right):
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def get_successors(state):
    successors = []
    m_left, c_left, boat, path = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    moves = [
        (1, 0),  
        (2, 0),  
        (0, 1),  
        (0, 2),  
        (1, 1), 
    ]
    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, 'right', path + [(m, c, '→')])
        else:
            new_state = (m_left + m, c_left + c, 'left', path + [(m, c, '←')])
        new_m_left, new_c_left, new_boat, _ = new_state
        new_m_right = 3 - new_m_left
        new_c_right = 3 - new_c_left
        if is_valid(new_m_left, new_c_left, new_m_right, new_c_right):
            successors.append(new_state)
    return successors
def solve():
    start = (3, 3, 'left', [])
    goal = (0, 0, 'right')
    queue = deque([start])
    visited = set()
    while queue:
        state = queue.popleft()
        m_left, c_left, boat, path = state
        if (m_left, c_left, boat) == goal:
            return path
        if (m_left, c_left, boat) in visited:
            continue
        visited.add((m_left, c_left, boat))
        for successor in get_successors(state):
            queue.append(successor)
    return None
def main():
    solution = solve()
    if solution:
        print("Steps to solve Missionaries and Cannibals:")
        for step_num, (m, c, direction) in enumerate(solution, 1):
            print(f"{step_num}. {m} missionary(s), {c} cannibal(s) {direction}")
    else:
        print("No solution found.")
if __name__ == "__main__":
    main()
