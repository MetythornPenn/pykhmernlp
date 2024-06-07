## remove_duplicate_spaces
    Remove duplicate spaces. Replace multiple spaces with one space.

    Multiple newline characters and empty lines will be replaced
    with one newline character.

    :param str text: input text
    :return: text without duplicated spaces and newlines
    :rtype: str

```python
from pykhmernlp import remove_duplicate_spaces

remove_duplicate_spaces('ក    គ    ថ')

# Result: 
# 'ក គ ថ'
```

## remove_zero_width_characters
    Remove zero-width characters.

    These non-visible characters may cause unexpected result from the
    user's point of view. Removing them can make string matching more robust.

    Characters to be removed:

        * Zero-width space (ZWSP)
        * Zero-width non-joiner (ZWJP)

    :param str text: input text
    :return: text without zero-width characters
    :rtype: str

```python
from pykhmernlp import remove_zero_width_characters

text1 = 'ក\u200bគ\u200cថ'
text2 = 'ក\u200b\u200bគ\u200c\u200cថ'
text3 = 'កគថ'

print(remove_zero_width_characters(text1))
print(remove_zero_width_characters(text2))
print(remove_zero_width_characters(text3))

# Result
# 'កគថ'
# 'កគថ'
# 'កគថ'
```
