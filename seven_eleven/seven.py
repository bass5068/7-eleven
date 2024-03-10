"""Seven_Eleven utility."""

def print_7_eleven(number):
    """Print number or Seven, Eleven, or 7-Eleven."""
    if number % 7 == 0 and number % 11 == 0:
        return "7-Eleven"
    elif number % 7 == 0:
        return "seven"
    elif number % 11 == 0:
        return "Eleven"
    else:
        return number
