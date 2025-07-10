
from itertools import permutations
def solve(addends, result):
    words = addends + [result]
    letters = sorted({ch for w in words for ch in w})
    if len(letters) > 10:
        raise ValueError("Too many distinct letters (max 10).")

    first_letters = {w[0] for w in words}            
    digits = '0123456789'

    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[ch] == '0' for ch in first_letters):
            continue                               
        nums = [int(''.join(mapping[c] for c in w)) for w in addends]
        res  = int(''.join(mapping[c] for c in result))
        if sum(nums) == res:
            print(" + ".join(map(str, nums)), "=", res,
                  "  →", {k:int(v) for k,v in mapping.items()})

if __name__ == "__main__":
    solve(['SEND', 'MORE'], 'MONEY')
