import re
from typing import List, Union

# Regular expressions to clean up text
_RE_REMOVE_NEWLINES = re.compile(r"\s*\n\s*")
_RE_DUPLICATE_SPACES = re.compile(r" +")

# Characters to be removed
_ZERO_WIDTH_CHARS = "\u200b\u200c"  # ZWSP, ZWNJ
_TRANSLATE_TABLE = str.maketrans('', '', _ZERO_WIDTH_CHARS)

def remove_duplicate_spaces(text: str) -> str:
    """
    Remove duplicate spaces. Replace multiple spaces with one space.

    Multiple newline characters and empty lines will be replaced
    with one newline character.

    :param str text: input text
    :return: text without duplicated spaces and newlines
    :rtype: str

    :Example:
    ::

        from pykhmernlp import remove_duplicate_spaces

        remove_duplicate_spaces('ក    គ    ថ')
        # output: 'ក គ ថ'
    """
    text = _RE_DUPLICATE_SPACES.sub(" ", text)
    text = _RE_REMOVE_NEWLINES.sub("\n", text)
    return text.strip()

def remove_zero_width_characters(text: str) -> str:
    """
    Remove zero-width characters.

    These non-visible characters may cause unexpected result from the
    user's point of view. Removing them can make string matching more robust.

    Characters to be removed:

        * Zero-width space (ZWSP)
        * Zero-width non-joiner (ZWJP)

    :param str text: input text
    :return: text without zero-width characters
    :rtype: str
    """
    return text.translate(_TRANSLATE_TABLE)

# # Example usage:
# if __name__ == "__main__":
#     example_text = 'ក    គ    ថ'
#     print(remove_duplicate_spaces(example_text))  # Output: 'ក គ ថ'
    
#     example_text_with_zw = 'ក\u200bគ\u200cថ'
#     print(remove_zero_width_characters(example_text_with_zw))  # Output: 'កគថ'
