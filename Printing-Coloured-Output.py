from colorama import Fore, Back

def print_colored_text(text, color):
    """
    Print text with a specified color.

    Args:
        text (str): The text to print.
        color (str): The color to use. Can be one of 'BLACK', 'YELLOW', 'RED', 'GREEN'.

    Returns:
        None

    Example:
        >>> print_colored_text('Hello, World!', 'RED')
        Hello, World! (printed in red)
    """
    color_map = {
        'BLACK': Fore.BLACK,
        'YELLOW': Fore.YELLOW,
        'RED': Fore.RED,
        'GREEN': Fore.GREEN
    }
    print(color_map[color] + text)

def print_colored_background(text, color):
    """
    Print text with a specified background color.

    Args:
        text (str): The text to print.
        color (str): The background color to use. Can be one of 'BLUE'.

    Returns:
        None

    Example:
        >>> print_colored_background('Hello, World!', 'BLUE')
        Hello, World! (printed with blue background)
    """
    color_map = {
        'BLUE': Back.BLUE
    }
    print(color_map[color] + text)

# Example usage:
print_colored_text('PyCodeCollection', 'BLACK')
print_colored_text('Happy Coding', 'YELLOW')
print_colored_text('PyCodeCollection', 'RED')
print_colored_text('Happy Coding', 'RED')
print_colored_text('Thank You', 'YELLOW')
print_colored_text('ASANTE SANA', 'GREEN')
print_colored_background('PyCodeCollection', 'BLUE')