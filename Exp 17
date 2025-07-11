import itertools

def cryptarithmetic():
    # Define the cryptarithmetic problem
    letters = 'SENDMOREMONEY'
    digits = '0123456789'
    
    for perm in itertools.permutations(digits, len(set(letters))):
        # Create a dictionary mapping letters to digits
        letter_to_digit = dict(zip(set(letters), perm))
        
        send = int(''.join(letter_to_digit[letter] for letter in 'SEND'))
        more = int(''.join(letter_to_digit[letter] for letter in 'MORE'))
        money = int(''.join(letter_to_digit[letter] for letter in 'MONEY'))
        
        if send + more == money:
            print(f"Solution found: ")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            break
    else:
        print("No solution found.")

cryptarithmetic()
