### Pronounce 

```Python hl_lines="2"
from pykhmernlp.pronounce import pronounce

result1 = pronounce("សម្ដេចបវរធិបតី")
print(result1)
# => ['សំ', 'ដាច់', 'ប', 'វ៉', 'ធិ', 'ប៉ៈ', 'ដី']

result2 = pronounce("មករា")
print(result2)
# => ['មៈ', 'កៈ', 'រ៉ា']

```

::: pykhmernlp.pronounce