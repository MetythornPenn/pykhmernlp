from khmercut import tokenize 

def khmercut(text):
    """
    Tokenize Khmer text using the khmercut library.

    Args:
        text (str): The Khmer text to tokenize.

    Returns:
        List[str]: A list of tokens.
    """
    return tokenize(text)
