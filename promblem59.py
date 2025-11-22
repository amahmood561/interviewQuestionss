# Use urllib.request to send network request if needed.
Empty a String

import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line


def code_here():
    parts = inputData.split()
    t = int(parts[0])
    print(t)
    out_lines = []

    def can_be_empty(s):
        stack = []
        for ch in s:
            stack.append(ch)
            if (len(stack) >= 3 and stack[-3] == '1' and stack[-2] == '0' and stack[-1] == '0'):
                #remove 100
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0
    idx = 1
    for _ in range(t):
        s = parts[idx]
        idx += 1
        # check if empty
        if can_be_empty(s):
            out_lines.append("yes")
        # yes
        else: 
            out_lines.append("no")
    return "\n".join(out_lines)


print(code_here())


# Use urllib.request to send network request if needed.
Longest substring

import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line


def code_here():
    s = inputData.strip()
    last_index = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        ch = s[right]
        if ch in last_index and last_index[ch] >=left:
            left = last_index[ch] + 1
        last_index[ch] = right
        max_len = max(max_len, right-left+1)
    return max_len


print(code_here())



Palindrome

inputData = ''

for line in fileinput.input():
    inputData += line


def code_here():
    s = inputData.strip().replace(" ", "")
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    # now countodd
    odd_count = 0
    for v in freq.values():
        if v % 2 == 1:
            odd_count += 1
    result = 0
    if odd_count > 1:
        result = odd_count - 1
    return result


print(code_here())