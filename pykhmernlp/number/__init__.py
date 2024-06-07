import re 

def to_latin_num(khmer_number: str) -> str:
    """
    Convert a string of Khmer numbers to Latin numbers.

    Args:
        khmer_number (str): A string containing Khmer numbers.

    Returns:
        str: A string with Khmer numbers converted to Latin numbers.
    """
    khmer_to_latin_map = {
        '០': '0',
        '១': '1',
        '២': '2',
        '៣': '3',
        '៤': '4',
        '៥': '5',
        '៦': '6',
        '៧': '7',
        '៨': '8',
        '៩': '9'
    }

    def replace_khmer_digit(match: re.Match) -> str:
        return khmer_to_latin_map[match.group(0)]

    pattern = re.compile('|'.join(re.escape(k) for k in khmer_to_latin_map.keys()))
    latin_number = pattern.sub(replace_khmer_digit, khmer_number)

    return latin_number


def to_khmer_num(latin_number: str) -> str:
    """
    Convert a string of Latin numbers to Khmer numbers.

    Args:
        latin_number (str): A string containing Latin numbers.

    Returns:
        str: A string with Latin numbers converted to Khmer numbers.
    """
    latin_to_khmer_map = {
        '0': '០',
        '1': '១',
        '2': '២',
        '3': '៣',
        '4': '៤',
        '5': '៥',
        '6': '៦',
        '7': '៧',
        '8': '៨',
        '9': '៩'
    }

    def replace_latin_digit(match: re.Match) -> str:
        return latin_to_khmer_map[match.group(0)]

    pattern = re.compile('|'.join(re.escape(l) for l in latin_to_khmer_map.keys()))
    khmer_number = pattern.sub(replace_latin_digit, latin_number)

    return khmer_number