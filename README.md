## PyKhmerNLP

Collections of Khmer Language Toolkit.

## Install

### Install from Source

```shell
git clone https://github.com/MetythornPenn/pykhmernlp.git
cd pykhmernlp
pip install -e .
```

### Install from PYPI

```shell
# pip install pykhmernlp
# *Noted: There's some errors with pip install & I'm fixing it.
```

## Usage 

### 1. Corpus

#### 1.1 Khmer words

```python
from pykhmernlp.corpus import km_words

km_words = km_words()
print(f"Length of Khmer words {len(km_words)}")
print(km_words[:100])

# Length of Khmer words 81028
# ['ក', 'កក', 'កកកុញ', 'កកកុះ', ...]
```

#### 1.2 English Word

```python
from pykhmernlp.corpus import en_words

en_words = en_words()

print(f"Length of English words {len(en_words)}")
print(en_words[:100])

# Length of English words 235892
# ['elcaja', 'problockade', 'chalkiness',...]
```


#### 1.3 Khmer to Khmer Dictionary 

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

#### 1.4 English to English Dictionary 

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

### 2. Tokenizer

```python
from pykhmernlp.tokenizer import khmercut

khmercut("ឃាត់ខ្លួនជនសង្ស័យ០៤នាក់ ករណីលួចខ្សែភ្លើង នៅស្រុកព្រៃនប់")

# Result: 
# => ['ឃាត់ខ្លួន', 'ជនសង្ស័យ', '០៤', 'នាក់', ' ', 'ករណី', 'លួច', 'ខ្សែភ្លើង', ' ', 'នៅ', 'ស្រុក', 'ព្រៃនប់']

```

### 3. Pronounce 

```python
from pykhmernlp.pronounce import pronounce

result1 = pronounce("សម្ដេចបវរធិបតី")
print(result1)
# => ['សំ', 'ដាច់', 'ប', 'វ៉', 'ធិ', 'ប៉ៈ', 'ដី']

result2 = pronounce("មករា")
print(result2)
# => ['មៈ', 'កៈ', 'រ៉ា']

```

### 4. Tha

```python
from pykhmernlp.tha import (
    normalize,
    process_phone_numbers,
    process_urls,
    process_time,
    process_date,
    process_hashtags,
    process_ascii_lines,
    process_license_plate,
    process_cardinals,
    process_decimals,
    process_ordinals,
    process_currency,
    process_parenthesis,
    process_repeater
)

# Normalize
assert normalize("មិន\u200bឲ្យ") == "មិនឱ្យ"

# Phone Numbers
assert process_phone_numbers("010123123", chunk_size=2) == "0▁10▁12▁31▁23"
assert process_phone_numbers("010123123", chunk_size=3) == "0▁10▁123▁123"
assert process_phone_numbers("0961231234", chunk_size=3) == "0▁96▁123▁1234"

# URLs and emails
assert process_urls("example@gmail.com") == "example at g▁mail dot com"
assert process_urls("https://google.com") == "google dot com"
assert process_urls("http://google.com") == "google dot com"
assert process_urls("google.com") == "google dot com"
assert process_urls("google.gov.kh") == "google dot gov dot k▁h"
assert process_urls("google.com.kh") == "google dot com dot k▁h"

# Time
assert process_time("10:23AM") == "10 23▁A▁M"
assert process_time("10:23PM") == "10 23▁P▁M"
assert process_time("1:23PM") == "1 23▁P▁M"

# Date
assert process_date("2024-01-02") == "2024 01 02"
assert process_date("01-02-2034") == "01 02 2034"

# Hashtags
assert process_hashtags("Hello world #this_will_remove hello") == "Hello world  hello"
assert process_hashtags("Hello world #លុប hello") == "Hello world  hello"
assert process_hashtags("Hello world #លុប1234 hello") == "Hello world  hello"

# ASCII Lines
assert process_ascii_lines("Remove --- asdasd") == "Remove  asdasd"
assert process_ascii_lines("Remove\n###\nasdasd") == "Remove\n\nasdasd"

# Cambodia License Plate
assert process_license_plate("1A 1234") == "1 A 12▁34"
assert process_license_plate("1A 4444") == "1 A ការ៉េ4"

# Number - Cardinals
assert process_cardinals("1234") == "មួយពាន់▁ពីររយ▁សាមសិបបួន"
assert process_cardinals("1") == "មួយ"
assert process_cardinals("1▁2") == "មួយ▁ពីរ"
assert process_cardinals("-1") == "ដក▁មួយ"
assert process_cardinals("10") == "ដប់"
assert process_cardinals("15") == "ដប់ប្រាំ"
assert process_cardinals("100") == "មួយរយ"
assert process_cardinals("10000") == "មួយម៉ឺន"
assert process_cardinals("10000.234") == "មួយម៉ឺន.ពីររយ▁សាមសិបបួន"
assert process_cardinals("-10000.234") == "ដក▁មួយម៉ឺន.ពីររយ▁សាមសិបបួន"
assert process_cardinals("-10000,234") == "ដក▁មួយម៉ឺន,ពីររយ▁សាមសិបបួន"

# Number - Decimals
assert process_decimals("123.324") == "មួយរយ▁ម្ភៃបី▁ចុច▁បីរយ▁ម្ភៃបួន"
assert process_decimals("123.001") == "មួយរយ▁ម្ភៃបី▁ចុច▁សូន្យ▁សូន្យ▁មួយ"
assert process_decimals("-123.0012") == "ដក▁មួយរយ▁ម្ភៃបី▁ចុច▁សូន្យ▁សូន្យ▁ដប់ពីរ"
assert process_decimals("-123,0012") == "ដក▁មួយរយ▁ម្ភៃបី▁ក្បៀស▁សូន្យ▁សូន្យ▁ដប់ពីរ"

# Number - Ordinals
assert process_ordinals("5th") == "ទី▁ប្រាំ"
assert process_ordinals("3rd") == "ទី▁បី"
assert process_ordinals("1st") == "ទី▁មួយ"
assert process_ordinals("10th") == "ទី▁ដប់"
assert process_ordinals("10") == "10"

# Number - Currency
assert process_currency("$100.01") == "មួយរយដុល្លារ▁មួយសេន"
assert process_currency("$100") == "មួយរយ▁ដុល្លារ"
# assert process_currency("100$") == "មួយរយដុល្លារ"
# assert process_currency("100៛") == "មួយរយរៀល"
# assert process_currency("100.32៛") == "មួយរយ▁ចុច▁សាមសិបពីររៀល"
# assert process_currency("100.0032៛") == "មួយរយ▁ចុច▁សូន្យ▁សូន្យ▁សាមសិបពីររៀល"

# Parenthesis
assert process_parenthesis("Hello (this will be ignored) world") == "Hello world"

# Iteration Mark
def fake_tokenizer(_):
    return ["គាត់", "បាន", "ទៅ", "បន្តិច", "ម្ដង"]

assert process_repeater("គាត់បានទៅបន្តិចម្ដងៗហើយ", tokenizer=fake_tokenizer) == "គាត់បានទៅបន្តិចម្ដង▁បន្តិចម្ដងហើយ"

print("All tests passed!")

```



### 5. Khmer Address

```python
from pykhmernlp.address import (
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

This library was inspired by [PyThaiNLP](https://pythainlp.github.io/) and I think our python community should have one, that's why i build this library.

This library wraps around other awesome Khmer libraries. Without these other libraries, this library wouldn't exist.

- [khmercut](https://github.com/seanghay/tha): from seanghay
- [khmerpronounce](https://github.com/seanghay/khmerpronounce): from seanghay
- [tha](https://github.com/seanghay/tha): from seanghay
