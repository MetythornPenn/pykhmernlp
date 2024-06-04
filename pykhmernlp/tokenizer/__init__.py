from typing import List
from khmercut import tokenize 

def khmercut(text: str) -> List[str]:
    """
    Tokenize Khmer text using the khmercut library.

    This function takes a string of Khmer text as input and uses the khmercut 
    library to tokenize it into individual words or tokens. This can be useful 
    for various natural language processing tasks such as text analysis, 
    machine learning, and information retrieval.

    Examples:
        >>> from pykhmernlp.tokenizer import khmercut
        >>> khmercut("ខ្ញុំសុខសប្បាយ")
        ['ខ្ញុំ', 'សុខ', 'សប្បាយ']

    Args:
        text (str): The Khmer text to tokenize. It should be a string containing 
                    valid Khmer characters.

    Returns:
        List[str]: A list of tokens. Each token is a string representing a word 
                   or meaningful unit in the Khmer text.
    """
    return tokenize(text)
