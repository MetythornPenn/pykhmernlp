
## Khmer words
    Load a list of Khmer words from ICU data.

    Returns:
        List[str]: A list of Khmer words.

```python
from pykhmernlp.corpus import km_words

km_words = km_words()
print(f"Length of Khmer words {len(km_words)}")
print(km_words[:100])

# Length of Khmer words 81028
# ['ក', 'កក', 'កកកុញ', 'កកកុះ', ...]
```

## English Word

    Load a list of Khmer words nltk library.

    Returns:
        List[str]: A list of Khmer words.


```python
from pykhmernlp.corpus import en_words

en_words = en_words()

print(f"Length of English words {len(en_words)}")
print(en_words[:100])

# Length of English words 235892
# ['elcaja', 'problockade', 'chalkiness',...]
```

## Khmer to Khmer Dictionary

    Search for a Khmer word in the Khmer dictionary.

    Args:
        word (str): The Khmer word to search for.

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing entries in the Khmer dictionary
                               corresponding to the provided word.
                               Each dictionary contains keys for 
                               'word' (main word), 
                               'pronounce' (pronunciation),
                               'pos' (part of speech), 
                               'definition',
                               'example'.

```python
from pykhmernlp.corpus import km2km_dict

entries = km2km_dict('កក់ក្ដៅ')
print(entries)

# Result : 
# [{
#   'word': 'កក់ក្ដៅ', 
#   'pronounce': '[កក់-ក្ដៅ]', 
#   'pos': 'កិ.', 
#   'definition': 'ក្ដៅល្មម ក្ដៅស្រួល :', 
#   'example': 'ភួយនេះកក់ក្ដៅណាស់។'
# }]

```

## English to English Dictionary 

    Search for an English word in the English dictionary.

    Args:
        word (str): The English word to search for.

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing entries in the English dictionary
                               corresponding to the provided word.
                               Each dictionary contains keys for 
                               'word', 
                               'pos' (part of speech),
                               'definition'

```python
from pykhmernlp.corpus import en2en_dict

entries = en2en_dict('BooK')
print(entries)

# Result: 
# [{
#   'word': 'book', 
#   'pos': 'n.', 
#   'definition': 'A collection of sheets of paper, or similar material....
# }]
```
