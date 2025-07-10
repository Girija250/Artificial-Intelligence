def solve(n=8):
    cols, diag1, diag2 = set(), set(), set()   
    board = [-1] * n                          
    def bt(r: int) -> bool:                   
        if r == n:
            return True                        
        for c in range(n):
            if c in cols or r - c in diag1 or r + c in diag2:
                continue                      
            cols.add(c); diag1.add(r - c); diag2.add(r + c)
            board[r] = c
            if bt(r + 1):                     
                return True
            cols.remove(c); diag1.remove(r - c); diag2.remove(r + c)
        return False                          

    return board if bt(0) else None          

def print_board(sol):
    n = len(sol)
    for r in range(n):
        print(' '.join('Q' if c == sol[r] else '.' for c in range(n)))
    print()                                 
if __name__ == "__main__":
    solution = solve()                         
    if solution:
        print_board(solution)
    else:
        print("No solution found.")
