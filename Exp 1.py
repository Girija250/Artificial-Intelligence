from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)          # target board

# Manhattan‑distance heuristic
def h(s):
    return sum(abs((v-1)//3 - i//3) + abs((v-1)%3 - i%3)
               for i, v in enumerate(s) if v)

# neighbouring boards after one slide
def nbrs(s):
    i = s.index(0); r, c = divmod(i, 3)
    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr*3 + nc
            t = list(s); t[i], t[j] = t[j], t[i]
            yield tuple(t)

def astar(start):
    pq, seen = [(h(start), 0, start, [])], {start}
    while pq:
        f, g, s, path = heappop(pq)
        if s == goal:
            return path                        # solved
        for n in nbrs(s):
            if n not in seen:
                seen.add(n)
                heappush(pq, (g+1+h(n), g+1, n, path+[n]))

# -------- run ----------
start = tuple(map(int, input("Enter 9 numbers (0 = blank): ").split()))
solution = astar(start)
print(f"\nSolved in {len(solution)} moves:")
for state in solution:
    print(state[:3], "\n", state[3:6], "\n", state[6:], "\n")
