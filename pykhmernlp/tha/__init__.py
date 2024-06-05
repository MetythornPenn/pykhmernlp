
import tha.normalize
import tha.phone_numbers
import tha.urls
import tha.datetime
import tha.hashtags
import tha.ascii_lines
import tha.license_plate
import tha.cardinals
import tha.decimals
import tha.ordinals
import tha.currency
import tha.parenthesis
import tha.repeater


def normalize(text: str) -> str:
    """
    Normalize text by removing zero-width spaces.

    Args:
        text (str): The text to normalize.

    Returns:
        str: The normalized text.
    """
    return tha.normalize.processor(text)


def process_phone_numbers(text: str, chunk_size: int = 2) -> str:
    """
    Process phone numbers in the text by chunking digits with a specified chunk size.

    Args:
        text (str): The text containing phone numbers.
        chunk_size (int): The size of each digit chunk.

    Returns:
        str: The processed text with phone numbers chunked.
    """

    return tha.phone_numbers.processor(text, chunk_size=chunk_size)


def process_urls(text: str) -> str:
    """
    Process URLs and emails in the text by replacing them with tokens.

    Args:
        text (str): The text containing URLs and emails.

    Returns:
        str: The processed text with URLs and emails replaced.
    """
    return tha.urls.processor(text)


def process_time(text: str) -> str:
    """
    Process time expressions in the text by formatting them.

    Args:
        text (str): The text containing time expressions.

    Returns:
        str: The processed text with time expressions formatted.
    """
    return tha.datetime.time_processor(text)



def process_date(text: str) -> str:
    """
    Process date expressions in the text by formatting them.

    Args:
        text (str): The text containing date expressions.

    Returns:
        str: The processed text with date expressions formatted.
    """
    return tha.datetime.date_processor(text)


def process_hashtags(text: str) -> str:
    """
    Process hashtags in the text by removing them.

    Args:
        text (str): The text containing hashtags.

    Returns:
        str: The processed text with hashtags removed.
    """
    return tha.hashtags.processor(text)


def process_ascii_lines(text: str) -> str:
    """
    Process ASCII lines in the text by removing them.

    Args:
        text (str): The text containing ASCII lines.

    Returns:
        str: The processed text with ASCII lines removed.
    """
    return tha.ascii_lines.processor(text)


def process_license_plate(text: str) -> str:
    """
    Process Cambodia license plate numbers in the text by formatting them.

    Args:
        text (str): The text containing Cambodia license plate numbers.

    Returns:
        str: The processed text with license plate numbers formatted.
    """

    return tha.license_plate.processor(text)


def process_cardinals(text: str) -> str:
    """
    Process cardinal numbers in the text by converting them to Khmer words.

    Args:
        text (str): The text containing cardinal numbers.

    Returns:
        str: The processed text with cardinal numbers converted to Khmer words.
    """

    return tha.cardinals.processor(text)


def process_decimals(text: str) -> str:
    """
    Process decimal numbers in the text by converting them to Khmer words.

    Args:
        text (str): The text containing decimal numbers.

    Returns:
        str: The processed text with decimal numbers converted to Khmer words.
    """
    return tha.decimals.processor(text)


def process_ordinals(text: str) -> str:
    """
    Process ordinal numbers in the text by converting them to Khmer words.

    Args:
        text (str): The text containing ordinal numbers.

    Returns:
        str: The processed text with ordinal numbers converted to Khmer words.
    """
    return tha.ordinals.processor(text)


def process_currency(text: str) -> str:
    """
    Process currency expressions in the text by converting them to Khmer words.

    Args:
        text (str): The text containing currency expressions.

    Returns:
        str: The processed text with currency expressions converted to Khmer words.
    """

    return tha.currency.processor(text)


def process_parenthesis(text: str) -> str:
    """
    Process parenthesis in the text by removing them.

    Args:
        text (str): The text containing parenthesis.

    Returns:
        str: The processed text with parenthesis removed.
    """

    return tha.parenthesis.processor(text)


def process_repeater(text: str, tokenizer) -> str:
    """
    Process repeated words or phrases in the text by replacing them with a single instance.

    Args:
        text (str): The text containing repeated words or phrases.
        tokenizer: A function used for tokenization.

    Returns:
        str: The processed text with repeated words or phrases replaced.
    """

    return tha.repeater.processor(text, tokenizer=tokenizer)
