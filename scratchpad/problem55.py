def divide(dividend: int, divisor: int) -> int:
    if divisor == 0:
        raise ValueError("Division by zero is undefined.")l
    
    quotient = 0
    temp_dividend = dividend

    # Use bit shifts to speed up subtraction
    while temp_dividend >= divisor:
        multiple = divisor
        multiple_count = 1
        
        # Double the divisor until it would be too big
        while (multiple << 1) <= temp_dividend:
            multiple <<= 1
            multiple_count <<= 1
        
        # Subtract and accumulate quotient
        temp_dividend -= multiple
        quotient += multiple_count

    return quotient


# Examples
print(divide(10, 3))  # Output: 3
print(divide(25, 5))  # Output: 5
print(divide(43, 8))  # Output: 5
