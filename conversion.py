def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""
    # Handle the integer part
    integer_part = int(decimal)
    while integer_part > 0:
        binary = str(integer_part % 2) + binary
        integer_part //= 2

    return binary

def binary_to_decimal(binary):
    return int(binary, 2)  # Convert binary to decimal

def binary_to_hexadecimal(binary):
    decimal_value = int(binary, 2)  # Convert binary to decimal
    return hex(decimal_value)[2:]   # Convert decimal to hexadecimal and remove '0x'

def binary_to_octal(binary):
    decimal_value = int(binary, 2)  # Convert binary to decimal
    return oct(decimal_value)[2:]   # Convert decimal to octal and remove '0o'

# Main menu
def main():
    print("Choose an option:")
    print("1: Convert decimal numbers to binary")
    print("2: Convert binary numbers to hexadecimal, octal, or decimal")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        decimal_number = float(input("Enter a decimal number: "))
        binary_representation = decimal_to_binary(decimal_number)
        print(f"Binary representation of {decimal_number} is {binary_representation}")
    
    elif choice == 2:
        binary_number = input("Enter a binary number: ")
        print("Choose the base to convert to:")
        print("1: Convert to hexadecimal")
        print("2: Convert to octal")
        print("3: Convert to decimal")
        base_choice = int(input("Enter your choice (1, 2, or 3): "))
        
        if base_choice == 1:
            hex_representation = binary_to_hexadecimal(binary_number)
            print(f"Hexadecimal representation of {binary_number} is {hex_representation}")
        elif base_choice == 2:
            octal_representation = binary_to_octal(binary_number)
            print(f"Octal representation of {binary_number} is {octal_representation}")
        elif base_choice == 3:
            decimal_representation = binary_to_decimal(binary_number)
            print(f"Decimal representation of {binary_number} is {decimal_representation}")
        else:
            print("Invalid choice for base conversion")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
# if __name__ == "_main_":
main()