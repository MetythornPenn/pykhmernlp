[Khmer Pronounce](https://github.com/seanghay/khmerpronounce) A Khmer pronounciation toolkit trained on KhmerDictionary 2022 by Royal Academy of Cambodia (RAC) with Phonetisaurus from Seanghay.

```Python
from pykhmernlp.pronounce import pronounce

result1 = pronounce("សម្ដេចបវរធិបតី")
print(result1)
# => ['សំ', 'ដាច់', 'ប', 'វ៉', 'ធិ', 'ប៉ៈ', 'ដី']

result2 = pronounce("មករា")
print(result2)
# => ['មៈ', 'កៈ', 'រ៉ា']

```

<!-- ::: pykhmernlp.pronounce -->