'''
Mastermind is a two-player game in which the first player attempts to guess the secret code of the second. In this version, the code may be any six-digit number with all distinct digits.

Each turn the first player guesses some number, and the second player responds by saying how many digits in this number correctly matched their location in the secret code. For example, if the secret code were 123456, then a guess of 175286 would score two, since 1 and 6 were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores, determines whether there exists some secret code that could have produced them.

For example, for the following scores you should return True, since they correspond to the secret code 123456:

{175286: 2, 293416: 3, 654321: 0}
However, it is impossible for any key to result in the following scores, so in this case you should return False:

{123456: 4, 345678: 4, 567890: 4}


'''


# mastermind_validator.py

from itertools import permutations

def generate_all_codes():
    """
    Generates all possible six-digit codes with distinct digits.
    
    Returns:
        List of strings representing all valid codes.
    """
    digits = '0123456789'
    return [''.join(p) for p in permutations(digits, 6)]

def count_correct_placements(secret, guess):
    """
    Counts the number of digits that are correctly placed in the guess compared to the secret.
    
    Args:
        secret (str): The secret six-digit code.
        guess (str): The guessed six-digit number.
        
    Returns:
        int: Number of correctly placed digits.
    """
    return sum(s == g for s, g in zip(secret, guess))

def is_valid_code(all_guesses, all_codes=None):
    """
    Determines whether there exists a secret code that satisfies all guess constraints.
    
    Args:
        all_guesses (dict): A dictionary where keys are guess strings and values are their scores.
        all_codes (list, optional): Pre-generated list of all possible codes. If None, it will be generated.
        
    Returns:
        bool: True if at least one valid secret code exists, False otherwise.
    """
    if all_codes is None:
        all_codes = generate_all_codes()
    
    for code in all_codes:
        valid = True
        for guess, score in all_guesses.items():
            if count_correct_placements(code, guess) != score:
                valid = False
                break  # Early pruning
        if valid:
            # Uncomment the following line to see the valid code(s)
            # print(f"Valid secret code found: {code}")
            return True  # Found at least one valid code
    return False  # No valid code found

def main():
    """
    Main function to execute example test cases.
    """
    # Example 1: Should return True
    guesses1 = {
        '175286': 2,
        '293416': 3,
        '654321': 0
    }
    result1 = is_valid_code(guesses1)
    print(f"Test Case 1 Result: {result1}")  # Expected Output: True

    # Example 2: Should return False
    guesses2 = {
        '123456': 4,
        '345678': 4,
        '567890': 4
    }
    result2 = is_valid_code(guesses2)
    print(f"Test Case 2 Result: {result2}")  # Expected Output: False

    # Additional Example 3: Should return True (Multiple possible codes)
    guesses3 = {
        '012345': 1,
        '678901': 2
    }
    result3 = is_valid_code(guesses3)
    print(f"Test Case 3 Result: {result3}")  # Expected Output: True

    # Additional Example 4: Should return False (Conflicting constraints)
    guesses4 = {
        '000000': 6,  # Impossible since all digits must be distinct
    }
    result4 = is_valid_code(guesses4)
    print(f"Test Case 4 Result: {result4}")  # Expected Output: False

if __name__ == "__main__":
    main()
