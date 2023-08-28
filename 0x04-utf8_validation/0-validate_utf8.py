#!/usr/bin/python3
""" UTF-8 validation """


def validUTF8(data):
    # Count of the remaining bytes to validate in the current character
    remaining_bytes = 0

    for num in data:
        # Check if the most significant bit is 0 (ASCII character)
        if num >> 7 == 0:
            if remaining_bytes > 0:
                return False  # Continuation byte expecte
        else:
            if remaining_bytes == 0:
                # Determine the number of bytes in the current character
                if num >> 5 == 0b110:
                    remaining_bytes = 1
                elif num >> 4 == 0b1110:
                    remaining_bytes = 2
                elif num >> 3 == 0b11110:
                    remaining_bytes = 3
                else:
                    return False  # Invalid start byte

            else:
                # Check if the current byte is a continuation byte
                if num >> 6 != 0b10:
                    return False  # Invalid continuation byte
                remaining_bytes -= 1

        if remaining_bytes < 0:
            return False  # More continuation bytes than expected

    # All bytes and continuation bytes matched
    return remaining_bytes == 0

