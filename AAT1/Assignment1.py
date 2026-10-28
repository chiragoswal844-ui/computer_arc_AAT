# Signed Binary Arithmetic using 2's Complement
# 8-bit operands and 16-bit arithmetic

def to_binary(n, bits):
    """Convert a signed integer to two's complement binary."""
    return format(n & ((1 << bits) - 1), f'0{bits}b')


def to_signed(binary, bits):
    """Convert two's complement binary to a signed integer."""
    value = int(binary, 2)
    if value & (1 << (bits - 1)):
        value -= (1 << bits)
    return value


def binary_subtraction(a, b):
    operand_bits = 8
    result_bits = 16

    # Display operands in 8-bit format
    bin_a = to_binary(a, operand_bits)
    bin_b = to_binary(b, operand_bits)

    # Sign-extend operands to 16 bits
    ext_a = to_binary(a, result_bits)
    ext_b = to_binary(b, result_bits)

    # Subtraction using 2's complement:
    # A - B = A + (2's complement of B)
    complement_b = (~int(ext_b, 2) + 1) & 0xFFFF

    # Perform 16-bit addition
    result = (int(ext_a, 2) + complement_b) & 0xFFFF
    result_bin = format(result, '016b')
    result_dec = to_signed(result_bin, result_bits)

    # Check signed overflow
    actual_result = a - b
    overflow_8 = not (-128 <= actual_result <= 127)
    overflow_16 = not (-32768 <= actual_result <= 32767)

    print("Operand A (8-bit):", bin_a)
    print("Operand B (8-bit):", bin_b)
    print("Operand A (16-bit):", ext_a)
    print("Operand B (16-bit):", ext_b)
    print("2's complement of B (16-bit):",
          format(complement_b, '016b'))

    print("\nBinary Subtraction:")
    print(" ", ext_a)
    print("+", format(complement_b, '016b'))
    print("-" * 20)
    print(" ", result_bin)

    print("\nResult in binary:", result_bin)
    print("Result in decimal:", result_dec)
    print("8-bit overflow:", "Yes" if overflow_8 else "No")
    print("16-bit overflow:", "Yes" if overflow_16 else "No")
    print("-" * 45)


# Test expressions
print("Expression (a): 35 - (+29)")
binary_subtraction(35, 29)

print("\nExpression (b): (-35) - (-12)")
binary_subtraction(-35, -12)
