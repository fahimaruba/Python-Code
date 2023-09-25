def float_to_14bit_binary(floating_dec):
    # Handle the sign
    if floating_dec < 0:
        sign_bit = "1"
        floating_dec = abs(floating_dec)
    else:
        sign_bit = "0"
    
    # Separate the integer and fractional parts
    integer_part = int(floating_dec)
    fractional_part = floating_dec - integer_part
    
    # Convert integer part to binary
    integer_binary = bin(integer_part)[2:]
    
    # Convert fractional part to binary
    fractional_binary = ""
    while fractional_part > 0 and len(fractional_binary) < 8:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit
    
    # Pad with zeros if necessary
    while len(fractional_binary) < 8:
        fractional_binary += "0"
    
    # Combine the sign, integer, and fractional parts
    result = sign_bit + integer_binary + fractional_binary
    
    # Pad with zeros to make it 14 bits in total
    while len(result) < 14:
        result += "0"
    
    return result

# Example usage:
floating_dec = -26.625
binary_representation = float_to_14bit_binary(floating_dec)
print(binary_representation)
