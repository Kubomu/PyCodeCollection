import periodictable

def get_element_info(Atomic_No: int) -> None:
    """
    Retrieves and prints information about an element given its atomic number.

    Args:
        Atomic_No (int): The atomic number of the element.

    Returns:
        None

    Example:
        >>> get_element_info(6)
        Element Name:  Carbon
        Symbol:  C
        Atomic Number:  6
        Atomic Mass:  12.0107
        Density:  2.26
    """
    element = periodictable.elements[Atomic_No]
    print('Element Name: ', element.name)
    print('Symbol: ', element.symbol)
    print('Atomic Number: ', element.number)
    print('Atomic Mass: ', element.mass)
    print('Density: ', element.density)

# Example usage:
Atomic_No = int(input('Enter Element Atomic No: '))
get_element_info(Atomic_No)