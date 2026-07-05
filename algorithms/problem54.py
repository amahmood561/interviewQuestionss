def divide(dividend: int, divisor: int) -> int:
    # Edge case: divisor is 0 (though problem says positive ints)
    if divisor == 0:
        raise ValueError("Division by zero is undefined.")
    
    quotient = 0
    # Work with copies so original inputs aren’t modified
    temp_dividend = dividend
    
    # We shift divisor left until it’s just less than or equal to dividend
    while temp_dividend >= divisor:
        multiple = divisor
        multiple_count = 1
        
        # Keep doubling until the next double would be too big
        while (multiple << 1) <= temp_dividend:
            multiple <<= 1
            multiple_count <<= 1
        
        # Subtract the largest found multiple from dividend
        temp_dividend -= multiple
        quotient += multiple_count
    
    return quotient


# Example:
print(divide(10, 3))  # Output: 3
print(divide(25, 5))  # Output: 5
print(divide(43, 8))  # Output: 5
