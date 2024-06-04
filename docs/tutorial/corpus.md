
### Corpus

#### Khmer words

```python
from pykhmernlp.corpus import km_words

km_words = km_words()
print(f"Length of Khmer words {len(km_words)}")
print(km_words[:100])

# Length of Khmer words 81028
# ['ក', 'កក', 'កកកុញ', 'កកកុះ', ...]
```

#### English Word

```python
from pykhmernlp.corpus import en_words

en_words = en_words()

print(f"Length of English words {len(en_words)}")
print(en_words[:100])

# Length of English words 235892
# ['elcaja', 'problockade', 'chalkiness',...]
```


#### Khmer to Khmer Dictionary 

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

#### English to English Dictionary 

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
