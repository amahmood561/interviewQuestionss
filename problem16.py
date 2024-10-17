
'''

This problem was asked by Quantcast.

You are presented with an array representing a Boolean expression. The elements are of two kinds:

T and F, representing the values True and False.
&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).

'''
def count_ways(expression):
    memo = {}
    
    def count_ways_helper(i, j, is_true):
        key = (i, j, is_true)
        if key in memo:
            return memo[key]
        
        # Base case: single operand
        if i == j:
            if is_true:
                memo[key] = 1 if expression[i] == 'T' else 0
            else:
                memo[key] = 1 if expression[i] == 'F' else 0
            return memo[key]
        
        ways = 0
        for k in range(i + 1, j, 2):
            operator = expression[k]
            
            # Compute number of ways for left and right sub-expressions
            left_true = count_ways_helper(i, k - 1, True)
            left_false = count_ways_helper(i, k - 1, False)
            right_true = count_ways_helper(k + 1, j, True)
            right_false = count_ways_helper(k + 1, j, False)
            
            # Total ways for left and right
            total_left = left_true + left_false
            total_right = right_true + right_false
            
            if operator == '&':
                if is_true:
                    ways += left_true * right_true
                else:
                    ways += (total_left * total_right) - (left_true * right_true)
            elif operator == '|':
                if is_true:
                    ways += (left_true * right_true) + (left_true * right_false) + (left_false * right_true)
                else:
                    ways += left_false * right_false
            elif operator == '^':
                if is_true:
                    ways += (left_true * right_false) + (left_false * right_true)
                else:
                    ways += (left_true * right_true) + (left_false * right_false)
        
        memo[key] = ways
        return ways
    
    n = len(expression)
    return count_ways_helper(0, n - 1, True)

# Example Usage
expr = ['F', '|', 'T', '&', 'T']
print(count_ways(expr))  # Output: 2
