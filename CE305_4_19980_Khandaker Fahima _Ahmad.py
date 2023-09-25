def is_valid_number(num_str, base):
    try:
        int(num_str, base)
        return True
    except ValueError:
        return False

def base_conv(num_str, from_base, to_base):
    if not is_valid_number(num_str, from_base):
        print("Invalid input number for the given base.")
        return
    
    decimal_num = int(num_str, from_base)
    result = ""
    
    while decimal_num > 0:
        remainder = decimal_num % to_base
        result = str(remainder) + result
        decimal_num //= to_base
    
    print(result)

# Example usage:
base_conv("123456", 10, 2)  # Convert decimal 12345 to binary
base_conv("2A3", 16, 8)    # Convert hexadecimal 1A3 to octal
base_conv("1011", 2, 16)   # Convert binary 1010 to hexadecimal
