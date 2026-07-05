'''
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''

def full_justify(words, k):
    lines = []
    current_words = []
    current_len = 0

    for word in words:
        # If adding this word exceeds line length, justify current line
        if current_words and current_len + len(word) + len(current_words) > k:
            spaces = k - current_len
            if len(current_words) == 1:
                # Single word: left align
                line = current_words[0] + " " * spaces
            else:
                # Multiple words: distribute spaces
                space_per_gap = spaces // (len(current_words) - 1)
                extra = spaces % (len(current_words) - 1)
                
                line = ""
                for i, w in enumerate(current_words):
                    line += w
                    if i < len(current_words) - 1:  # add spaces between words
                        line += " " * (space_per_gap + (1 if i < extra else 0))
            lines.append(line)
            current_words = []
            current_len = 0

        # Add word to current line
        current_words.append(word)
        current_len += len(word)

    # Handle last line (left justified)
    last_line = " ".join(current_words)
    last_line += " " * (k - len(last_line))
    lines.append(last_line)

    return lines


# Example
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
result = full_justify(words, k)
for r in result:
    print(f'"{r}"')
