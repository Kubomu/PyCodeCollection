def decimal_to_binary(decimal):
    """
    Convert a decimal number (integer or floating-point) to its binary representation.
    Handles both the integer and fractional parts of the number.
    """
    if decimal == 0:
        return "0"  # Return "0" if the input is zero

    binary = ""
    # Handle the integer part
    integer_part = int(decimal)  # Extract the integer part of the decimal number
    while integer_part > 0:
        binary = str(integer_part % 2) + binary  # Append the binary digit
        integer_part //= 2  # Reduce the integer part by dividing by 2

    # Handle the fractional part
    fractional_part = decimal - int(decimal)  # Extract the fractional part
    if fractional_part > 0:
        binary += "."  # Add the binary point for the fractional part
        while fractional_part > 0:
            fractional_part *= 2  # Multiply fractional part by 2
            bit = int(fractional_part)  # Extract the integer part (0 or 1)
            binary += str(bit)  # Append the binary digit
            fractional_part -= bit  # Subtract the integer part from the result

    return binary


def binary_to_decimal(binary):
    """
    Convert a binary string to its decimal equivalent.
    """
    return int(binary, 2)  # Use Python's built-in function to parse binary


def binary_to_hexadecimal(binary):
    """
    Convert a binary string to its hexadecimal equivalent.
    """
    decimal_value = int(binary, 2)  # Convert binary to decimal
    return hex(decimal_value)[2:]  # Convert decimal to hexadecimal and strip '0x'


def binary_to_octal(binary):
    """
    Convert a binary string to its octal equivalent.
    """
    decimal_value = int(binary, 2)  # Convert binary to decimal
    return oct(decimal_value)[2:]  # Convert decimal to octal and strip '0o'


# Main menu
def main():
    """
    Display the main menu for the program and handle user choices.
    """
    while True:
        # Display the menu options
        print("\nChoose an option:")
        print("1: Convert decimal numbers to binary")
        print("2: Convert binary numbers to hexadecimal, octal, or decimal")
        print("3: Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            try:
                # Prompt user for a decimal number and convert to binary
                decimal_number = float(input("Enter a decimal number: "))
                binary_representation = decimal_to_binary(decimal_number)
                print(f"Binary representation of {decimal_number} is {binary_representation}")
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")
        
        elif choice == "2":
            # Prompt user for a binary number and choose conversion type
            binary_number = input("Enter a binary number: ")
            print("Choose the base to convert to:")
            print("1: Convert to hexadecimal")
            print("2: Convert to octal")
            print("3: Convert to decimal")
            base_choice = input("Enter your choice (1, 2, or 3): ")
            
            try:
                if base_choice == "1":
                    # Convert binary to hexadecimal
                    hex_representation = binary_to_hexadecimal(binary_number)
                    print(f"Hexadecimal representation of {binary_number} is {hex_representation}")
                elif base_choice == "2":
                    # Convert binary to octal
                    octal_representation = binary_to_octal(binary_number)
                    print(f"Octal representation of {binary_number} is {octal_representation}")
                elif base_choice == "3":
                    # Convert binary to decimal
                    decimal_representation = binary_to_decimal(binary_number)
                    print(f"Decimal representation of {binary_number} is {decimal_representation}")
                else:
                    print("Invalid choice for base conversion.")
            except ValueError:
                print("Invalid binary number! Please enter a valid binary string.")
        
        elif choice == "3":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()
