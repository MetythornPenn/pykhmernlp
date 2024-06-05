[Tha](https://github.com/seanghay/tha) : Khmer Text Normalization and Verbalization Toolkit.



## Normalize

    Normalize text by removing zero-width spaces.

    Args:
        text (str): The text to normalize.

    Returns:
        str: The normalized text.

```python
from pykhmernlp.tha import normalize
text_normalize = "មិន\u200bឲ្យ"

print("Original text:", text_normalize)
print(normalize(text_normalize))  # Output: "មិនឱ្យ"
```

## Phone Numbers

    Process phone numbers in the text by chunking digits with a specified chunk size.

    Args:
        text (str): The text containing phone numbers.
        chunk_size (int): The size of each digit chunk.

    Returns:
        str: The processed text with phone numbers chunked.

```python
from pykhmernlp.tha import process_phone_numbers
text_phone_numbers = "010123123"

print("Original text:", text_phone_numbers)
print(process_phone_numbers(text_phone_numbers, chunk_size=2))  # Output: "0▁10▁12▁31▁23"
```

## URLs and emails

    Process URLs and emails in the text by replacing them with tokens.

    Args:
        text (str): The text containing URLs and emails.

    Returns:
        str: The processed text with URLs and emails replaced.

```python
from pykhmernlp.tha import process_urls
text_urls = "https://google.com"

print("Original text:", text_urls)
print(process_urls(text_urls))  # Output: "google dot com"
```

## Time

    Process time expressions in the text by formatting them.

    Args:
        text (str): The text containing time expressions.

    Returns:
        str: The processed text with time expressions formatted.

```python
from pykhmernlp.tha import process_time
text_time = "10:23AM"

print("Original text:", text_time)
print(process_time(text_time))  # Output: "10 23▁A▁M"
```

## Date

    Process date expressions in the text by formatting them.

    Args:
        text (str): The text containing date expressions.

    Returns:
        str: The processed text with date expressions formatted.

```python
from pykhmernlp.tha import process_date
text_date = "2024-01-02"

print("Original text:", text_date)
print(process_date(text_date))  # Output: "2024 01 02"
```

## Hashtags

    Process hashtags in the text by removing them.

    Args:
        text (str): The text containing hashtags.

    Returns:
        str: The processed text with hashtags removed.

```python
from pykhmernlp.tha import process_hashtags
text_hashtags = "Hello world #this_will_remove hello"

print("Original text:", text_hashtags)
print(process_hashtags(text_hashtags))  # Output: "Hello world  hello"
```

## ASCII Lines

    Process ASCII lines in the text by removing them.

    Args:
        text (str): The text containing ASCII lines.

    Returns:
        str: The processed text with ASCII lines removed.

```python
from pykhmernlp.tha import process_ascii_lines
text_ascii_lines = "Remove --- asdasd"

print("Original text:", text_ascii_lines)
print(process_ascii_lines(text_ascii_lines))  # Output: "Remove  asdasd"
```

## Cambodia License Plate

    Process Cambodia license plate numbers in the text by formatting them.

    Args:
        text (str): The text containing Cambodia license plate numbers.

    Returns:
        str: The processed text with license plate numbers formatted.

```python
from pykhmernlp.tha import process_license_plate
text_license_plate = "1A 1234"

print("Original text:", text_license_plate)
print(process_license_plate(text_license_plate))  # Output: "1 A 12▁34"
```

## Number - Cardinals

    Process cardinal numbers in the text by converting them to Khmer words.

    Args:
        text (str): The text containing cardinal numbers.

    Returns:
        str: The processed text with cardinal numbers converted to Khmer words.

```python
from pykhmernlp.tha import process_cardinals
text_cardinals = "1234"

print("Original text:", text_cardinals)
print(process_cardinals(text_cardinals))  # Output: "មួយពាន់▁ពីររយ▁សាមសិបបួន"
```

## Number - Decimals

    Process decimal numbers in the text by converting them to Khmer words.

    Args:
        text (str): The text containing decimal numbers.

    Returns:
        str: The processed text with decimal numbers converted to Khmer words.

```python
from pykhmernlp.tha import process_decimals
text_decimals = "123.324"

print("Original text:", text_decimals)
print(process_decimals(text_decimals)) # Output: "មួយរយ▁ម្ភៃបី▁ចុច▁បីរយ▁ម្ភៃបួន"
```

## Number - Ordinals

    Process ordinal numbers in the text by converting them to Khmer words.

    Args:
        text (str): The text containing ordinal numbers.

    Returns:
        str: The processed text with ordinal numbers converted to Khmer words.

```python
from pykhmernlp.tha import process_ordinals
text_ordinals = "5th"

print("Original text:", text_ordinals)
print(process_ordinals(text_ordinals))  # Output: "ទី▁ប្រាំ"
```

## Number - Currency

    Process currency expressions in the text by converting them to Khmer words.

    Args:
        text (str): The text containing currency expressions.

    Returns:
        str: The processed text with currency expressions converted to Khmer words.

```python
from pykhmernlp.tha import process_currency
text_currency = "$100"

print("Original text:", text_currency)
print(process_currency(text_currency))  # Output: "មួយរយដុល្លារ▁មួយសេន"
```

## Parenthesis

    Process parenthesis in the text by removing them.

    Args:
        text (str): The text containing parenthesis.

    Returns:
        str: The processed text with parenthesis removed.

```python
from pykhmernlp.tha import process_parenthesis
text_parenthesis = "Hello (this will be ignored) world"

print("Original text:", text_parenthesis)
print(process_parenthesis(text_parenthesis))  # Output: "Hello world"
```

## Iteration Mark

    """
    Process repeated words or phrases in the text by replacing them with a single instance.

    Args:
        text (str): The text containing repeated words or phrases.
        tokenizer: A function used for tokenization.

    Returns:
        str: The processed text with repeated words or phrases replaced.
    """

```python
from pykhmernlp.tha import process_repeater
text_repeater = "គាត់បានទៅបន្ត

def fake_tokenizer(_):
    return ["គាត់", "បាន", "ទៅ", "បន្តិច", "ម្ដង"]

process_repeater(text_repeater, tokenizer=fake_tokenizer) # Output: "គាត់បានទៅបន្តិចម្ដង▁បន្តិចម្ដងហើយ"
```
