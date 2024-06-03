## khmernlp 

Khmer Language Toolkit.


## Install

### Install from PYPI

```shell
pip install khmernlp
```

### Install from Source

```shell
pip install -e .
```


## Usage 

### 1. Corpus

#### 1.1 Khmer words

```python
from khmernlp.corpus import km_words

km_words = km_words()
print(f"Length of Khmer words {len(km_words)}")
print(km_words[:100])

# Length of Khmer words 81028
# ['ក', 'កក', 'កកកុញ', 'កកកុះ', ...]
```

#### 1.2 English Word

```python
from khmernlp.corpus import en_words

en_words = en_words()

print(f"Length of English words {len(en_words)}")
print(en_words[:100])

# Length of English words 235892
# ['elcaja', 'problockade', 'chalkiness',...]
```


#### 1.3 Khmer to Khmer Dictionary 

```python
from khmernlp.corpus import km2km_dict

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

#### 1.4 English to English Dictionary 

```python
from khmernlp.corpus import en2en_dict

entries = en2en_dict('BooK')
print(entries)

# Result: 
# [{
#   'word': 'book', 
#   'pos': 'n.', 
#   'definition': 'A collection of sheets of paper, or similar material....
# }]
```

### 2. Tokenizer

```python
from khmernlp.tokenizer import khmercut

khmercut("ឃាត់ខ្លួនជនសង្ស័យ០៤នាក់ ករណីលួចខ្សែភ្លើង នៅស្រុកព្រៃនប់")

# Result: 
# => ['ឃាត់ខ្លួន', 'ជនសង្ស័យ', '០៤', 'នាក់', ' ', 'ករណី', 'លួច', 'ខ្សែភ្លើង', ' ', 'នៅ', 'ស្រុក', 'ព្រៃនប់']

```

### 3. Pronounce 

```python
from khmernlp.pronounce import pronounce

result1 = pronounce("សម្ដេចបវរធិបតី")
print(result1)
# => ['សំ', 'ដាច់', 'ប', 'វ៉', 'ធិ', 'ប៉ៈ', 'ដី']

result2 = pronounce("មករា")
print(result2)
# => ['មៈ', 'កៈ', 'រ៉ា']

```


### 4. Khmer Address

```python
from khmernlp.address import (
    km_villages, 
    km_commune, 
    km_districts, 
    km_provinces
)

# List all villages
all_villages = km_villages()
print(f"Size Villages : {len(all_villages)}")
print(f"List of villages: {all_villages}")

print("\n")
# List villages from a specific province
battambang_villages = km_villages('battambang')
print(f"Size Battambang's Villages : {len(battambang_villages)}")
print(f"List battambang's villages: {battambang_villages}")

print("\n")
# List all communes
all_communes = km_commune()
print(f"Size Communes : {len(all_communes)}")
print(f"List of communes: {all_communes}")

print("\n")
# List communes from a specific province
kampot_communes = km_commune('kampot')
print(f"Size Kampot's Communes : {len(kampot_communes)}")
print(f"List kampot's communes: {kampot_communes}")

print("\n")
# List all districts
all_districts = km_districts()
print(f"Size Districts : {len(all_districts)}")
print(f"List of districts: {all_districts}")

print("\n")
# List districts from a specific province
kandal_districts = km_districts('kandal')
print(f"Size Kandal's Districts : {len(kandal_districts)}")
print(f"List kandal's districts: {kandal_districts}")


# List all provinces
provinces = km_provinces()
print(f"Size Provinces : {len(provinces)}")
print(f"List of provinces: {provinces}")

```


## Reference 

This library wraps around other awesome Khmer libraries. Without these other libraries, this library wouldn't exist.

- [khmercut from seanghay](https://github.com/seanghay/tha)
- [khmerpronounce from seanghay](https://github.com/seanghay/khmerpronounce)
- [tha from seanghay](https://github.com/seanghay/tha)
