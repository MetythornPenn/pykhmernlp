<!-- ::: pykhmernlp.tokenizer -->
[Khmercut](https://github.com/seanghay/khmercut) : A (fast) Khmer word segmentation toolkit.


## Khmercut
    Tokenize Khmer text using the khmercut library from Seanghay.

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

```python
from pykhmernlp.tokenizer import khmercut

khmercut("ឃាត់ខ្លួនជនសង្ស័យ០៤នាក់ ករណីលួចខ្សែភ្លើង នៅស្រុកព្រៃនប់")

# => ['ឃាត់ខ្លួន', 'ជនសង្ស័យ', '០៤', 'នាក់', ' ', 'ករណី', 'លួច', 'ខ្សែភ្លើង', ' ', 'នៅ', 'ស្រុក', 'ព្រៃនប់']
```
