'''
This problem  Google.

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.

'''


'''
Problem Statement
UTF-8 Validation

UTF-8 is a character encoding capable of encoding all possible characters (called code points) in Unicode. It uses one to four bytes for each symbol. The encoding has specific rules that determine how bytes should be structured to represent valid characters.

Given an array of integers representing the bytes of a data stream, determine if it is a valid UTF-8 encoding.

Rules for UTF-8 Encoding
Single-Byte Characters (ASCII):

Format: 0xxxxxxx
Explanation: The first bit is 0, followed by seven bits that represent the character. This covers characters from U+0000 to U+007F.
Multi-Byte Characters:

2-Byte Characters:
Format: 110xxxxx 10xxxxxx
Explanation: The first byte starts with 110, followed by five bits of data. The second byte starts with 10, followed by six bits of data.
3-Byte Characters:
Format: 1110xxxx 10xxxxxx 10xxxxxx
Explanation: The first byte starts with 1110, followed by four bits of data. The next two bytes start with 10, each followed by six bits of data.
4-Byte Characters:
Format: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Explanation: The first byte starts with 11110, followed by three bits of data. The next three bytes start with 10, each followed by six bits of data.
Continuation Bytes:

Any byte that starts with 10 is a continuation byte and must follow a leading byte that indicates a multi-byte character.

'''

def valid_utf8(data):
    """
    Determines if a given data stream is a valid UTF-8 encoding.

    :param data: List[int] - A list of integers representing bytes (0 <= byte <= 255)
    :return: bool - True if data is a valid UTF-8 encoding, False otherwise
    """
    num_bytes = 0  # Number of bytes in the current UTF-8 character

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for idx, byte in enumerate(data):
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If no leading 1's, it's a single-byte character
            if num_bytes == 0:
                continue

            # UTF-8 allows a maximum of 4 bytes per character
            if num_bytes > 4:
                print(f"Invalid sequence at byte index {idx}: Too many leading 1's.")
                return False

            # For multi-byte characters, at least one continuation byte is required
            if num_bytes == 1:
                print(f"Invalid sequence at byte index {idx}: Leading byte indicates 1 byte, which is invalid.")
                return False

        else:
            # For continuation bytes, the first two bits must be '10'
            if not (byte & mask1 and not (byte & mask2)):
                print(f"Invalid continuation byte at index {idx}: {format(byte, '08b')}")
                return False
        # Decrement the number of continuation bytes expected
        num_bytes = max(num_bytes - 1, 0)

    # All characters should be fully processed
    if num_bytes != 0:
        print("Invalid sequence: Not enough continuation bytes.")
        return False

    return True


def run_tests():
    test_cases = [
        {
            'data': [197, 130, 1],
            'expected': True,
            'description': 'Valid 2-byte character followed by single-byte character'
        },
        {
            'data': [235, 140, 4],
            'expected': False,
            'description': 'Invalid 3-byte character with incorrect continuation byte'
        },
        {
            'data': [240, 162, 138, 147, 17],
            'expected': True,
            'description': 'Valid 4-byte character followed by single-byte character'
        },
        {
            'data': [255],
            'expected': False,
            'description': 'Invalid single-byte character starting with 11111111'
        },
        {
            'data': [0],
            'expected': True,
            'description': 'Valid single-byte character (null character)'
        },
        {
            'data': [145],
            'expected': False,
            'description': 'Continuation byte without a leading byte'
        },
        {
            'data': [230, 136, 145],
            'expected': True,
            'description': 'Valid 3-byte character'
        },
        {
            'data': [250, 145, 145, 145, 145],
            'expected': False,
            'description': 'Invalid 5-byte character (UTF-8 supports up to 4 bytes)'
        },
        {
            'data': [228, 189, 160, 229, 165, 189],
            'expected': True,
            'description': 'Valid multiple 3-byte characters (e.g., Chinese characters)'
        },
        {
            'data': [240, 162, 138, 147],
            'expected': True,
            'description': 'Valid 4-byte character'
        },
        {
            'data': [240, 162, 138],
            'expected': False,
            'description': 'Incomplete 4-byte character'
        },
    ]

    for idx, test in enumerate(test_cases):
        result = valid_utf8(test['data'])
        assert result == test['expected'], f"Test case {idx + 1} failed: {test['description']}"
        print(f"Test case {idx + 1} passed: {test['description']}")

    print("All test cases passed!")

# Run the tests
run_tests()
