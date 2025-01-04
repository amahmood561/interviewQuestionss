'''
Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
'''

def is_palindrome(number):
    if number < 0:
        return False  # Negative numbers are not palindromes
    
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10  # Extract the last digit
        reversed_number = reversed_number * 10 + digit  # Build the reversed number
        number = number // 10  # Remove the last digit
    
    return original_number == reversed_number

# Test cases
print(is_palindrome(121))  # True
print(is_palindrome(888))  # True
print(is_palindrome(678))  # False
print(is_palindrome(-121))  # False
