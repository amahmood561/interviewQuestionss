'''

Coding Challenge: Anagram Checker
Write a Python function called are_anagrams that takes two strings as
 input and returns True if the strings are anagrams of each other, and False otherwise.
Ignore spaces, capitalization, and special characters.
are_anagrams("Listen", "Silent")  # True
are_anagrams("Hello, World!", "dlroW ,olleH")  # True
are_anagrams("Python", "Java")  # False

'''

import string

def are_anagrams(str1, str2):
    # Remove spaces and special characters, and convert to lowercase
    clean_str1 = ''.join(filter(str.isalnum, str1)).lower()
    clean_str2 = ''.join(filter(str.isalnum, str2)).lower()
    
    # Check if sorted characters are equal
    return sorted(clean_str1) == sorted(clean_str2)

# Test cases
print(are_anagrams("Listen", "Silent"))  # True
print(are_anagrams("Hello, World!", "dlroW ,olleH"))  # True
print(are_anagrams("Python", "Java"))  # False
