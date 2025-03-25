from itertools import permutations

def solve_crypt_arithmetic():
    letters = 'SENDMOREMONEY'
    unique_letters = set(letters)
    
    for perm in permutations(range(10), len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, perm))
        
        if letter_to_digit['S'] == 0 or letter_to_digit['M'] == 0:
            continue
        
        send = int(''.join(str(letter_to_digit[char]) for char in 'SEND'))
        more = int(''.join(str(letter_to_digit[char]) for char in 'MORE'))
        money = int(''.join(str(letter_to_digit[char]) for char in 'MONEY'))
        
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print(f"Mapping: {letter_to_digit}")
            return
    print("No solution found.")

solve_crypt_arithmetic()
