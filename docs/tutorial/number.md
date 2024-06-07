## to_latin_num

    Convert a string of Khmer numbers to Latin numbers.

    Args:
        khmer_number (str): A string containing Khmer numbers.

    Returns:
        str: A string with Khmer numbers converted to Latin numbers.

```python
from pykhmernlp.number import to_latin_num
text = "abc ១២៣៤៥៦៧៨៩០8space៨៩"

print("Original :", text)
print("Normalize :"to_latin_num(text_normalize))  # Output: ""
```


## to_khmer_num

    Convert a string of Latin numbers to Khmer numbers.

    Args:
        latin_number (str): A string containing Latin numbers.

    Returns:
        str: A string with Latin numbers converted to Khmer numbers.

```python
from pykhmernlp.number import to_latin_num
text = "abc ១២៣៤៥៦៧៨៩០8space៨៩"

print("Original :", text)
print("Normalize :"to_latin_num(text_normalize))  # Output: "ម"
```