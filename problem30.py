'''

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

'''
def break_string_into_lines(s: str, k: int):
    words = s.split()
    lines = []
    current_line = ""

    for word in words:
        if len(word) > k:
            # If any word is longer than k, return None
            return None

        if not current_line:
            # Start a new line with the current word
            current_line = word
        else:
            # Check if adding the word exceeds the limit
            if len(current_line) + 1 + len(word) <= k:
                current_line += ' ' + word
            else:
                # Append the current line and start a new one
                lines.append(current_line)
                current_line = word

    # Append the last line if it's not empty
    if current_line:
        lines.append(current_line)

    return lines

# Example usage:
s = "the quick brown fox jumps over the lazy dog"
k = 10
result = break_string_into_lines(s, k)
print(result)  # Output: ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog']
