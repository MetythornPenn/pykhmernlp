
# Tha

## Load all functions from pykhmernlp.tha

```Python hl_lines="2"
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
```

## Normalize

```Python hl_lines="2"
assert normalize("មិន\u200bឲ្យ") == "មិនឱ្យ"
```

## Phone Numbers

```Python hl_lines="2"
assert process_phone_numbers("010123123", chunk_size=2) == "0▁10▁12▁31▁23"
assert process_phone_numbers("010123123", chunk_size=3) == "0▁10▁123▁123"
assert process_phone_numbers("0961231234", chunk_size=3) == "0▁96▁123▁1234"
```

## URLs and emails

```Python hl_lines="2"
assert process_urls("example@gmail.com") == "example at g▁mail dot com"
assert process_urls("https://google.com") == "google dot com"
assert process_urls("http://google.com") == "google dot com"
assert process_urls("google.com") == "google dot com"
assert process_urls("google.gov.kh") == "google dot gov dot k▁h"
assert process_urls("google.com.kh") == "google dot com dot k▁h"
```

## Time

```Python hl_lines="2"
assert process_time("10:23AM") == "10 23▁A▁M"
assert process_time("10:23PM") == "10 23▁P▁M"
assert process_time("1:23PM") == "1 23▁P▁M"
```

## Date

```Python hl_lines="2"
assert process_date("2024-01-02") == "2024 01 02"
assert process_date("01-02-2034") == "01 02 2034"
```

## Hashtags

```Python hl_lines="2"
assert process_hashtags("Hello world #this_will_remove hello") == "Hello world  hello"
assert process_hashtags("Hello world #លុប hello") == "Hello world  hello"
assert process_hashtags("Hello world #លុប1234 hello") == "Hello world  hello"
```

## ASCII Lines

```Python hl_lines="2"
assert process_ascii_lines("Remove --- asdasd") == "Remove  asdasd"
assert process_ascii_lines("Remove\n###\nasdasd") == "Remove\n\nasdasd"
```

## Cambodia License Plate

```Python hl_lines="2"
assert process_license_plate("1A 1234") == "1 A 12▁34"
assert process_license_plate("1A 4444") == "1 A ការ៉េ4"
```

## Number - Cardinals

```Python hl_lines="2"
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
```

## Number - Decimals

```Python hl_lines="2"
assert process_decimals("123.324") == "មួយរយ▁ម្ភៃបី▁ចុច▁បីរយ▁ម្ភៃបួន"
assert process_decimals("123.001") == "មួយរយ▁ម្ភៃបី▁ចុច▁សូន្យ▁សូន្យ▁មួយ"
assert process_decimals("-123.0012") == "ដក▁មួយរយ▁ម្ភៃបី▁ចុច▁សូន្យ▁សូន្យ▁ដប់ពីរ"
assert process_decimals("-123,0012") == "ដក▁មួយរយ▁ម្ភៃបី▁ក្បៀស▁សូន្យ▁សូន្យ▁ដប់ពីរ"
```

## Number - Ordinals

```Python hl_lines="2"
assert process_ordinals("5th") == "ទី▁ប្រាំ"
assert process_ordinals("3rd") == "ទី▁បី"
assert process_ordinals("1st") == "ទី▁មួយ"
assert process_ordinals("10th") == "ទី▁ដប់"
assert process_ordinals("10") == "10"
```

## Number - Currency

```Python hl_lines="2"
assert process_currency("$100.01") == "មួយរយដុល្លារ▁មួយសេន"
assert process_currency("$100") == "មួយរយ▁ដុល្លារ"
# assert process_currency("100$") == "មួយរយដុល្លារ"
# assert process_currency("100៛") == "មួយរយរៀល"
# assert process_currency("100.32៛") == "មួយរយ▁ចុច▁សាមសិបពីររៀល"
# assert process_currency("100.0032៛") == "មួយរយ▁ចុច▁សូន្យ▁សូន្យ▁សាមសិបពីររៀល"
```

## Parenthesis

```Python hl_lines="2"
assert process_parenthesis("Hello (this will be ignored) world") == "Hello world"

## Iteration Mark
def fake_tokenizer(_):
    return ["គាត់", "បាន", "ទៅ", "បន្តិច", "ម្ដង"]

assert process_repeater("គាត់បានទៅបន្តិចម្ដងៗហើយ", tokenizer=fake_tokenizer) == "គាត់បានទៅបន្តិចម្ដង▁បន្តិចម្ដងហើយ"

print("All tests passed!")

```

::: pykhmernlp.tha