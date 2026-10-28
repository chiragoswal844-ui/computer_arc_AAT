# Python program for 8-bit rotate operations
# ROL: Rotate Left without Carry
# RCL: Rotate Left through Carry


def rol(binary, positions):
    """Rotate an 8-bit binary number left without carry."""
    value = int(binary, 2)
    print("\nROL - Rotate Left without Carry")
    print("Original number:", binary)

    for i in range(positions):
        msb = (value >> 7) & 1
        value = ((value << 1) | msb) & 0xFF

        print(f"After rotation {i + 1}: {value:08b}")

    print("Final ROL result:", format(value, '08b'))


def rcl(binary, carry, positions):
    """Rotate an 8-bit binary number left through the carry flag."""
    value = int(binary, 2)

    print("\nRCL - Rotate Left through Carry")
    print("Original number:", binary)
    print("Initial carry flag:", carry)

    for i in range(positions):
        msb = (value >> 7) & 1

        # Shift left and insert the previous carry into the LSB
        value = ((value << 1) | carry) & 0xFF

        # The previous MSB becomes the new carry
        carry = msb

        print(
            f"After rotation {i + 1}: "
            f"Binary = {value:08b}, Carry = {carry}"
        )

    print("Final RCL result:", format(value, '08b'))
    print("Final carry flag:", carry)


# (a) ROL left by 2 positions
rol("11110110", 2)

# (b) RCL left by 2 positions
# Assume the initial carry flag is 0
rcl("10000110", 0, 2)

