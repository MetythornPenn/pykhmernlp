# Khmer Address

```Python hl_lines="2"
from pykhmernlp.address import (
    km_villages, 
    km_commune, 
    km_districts, 
    km_provinces
)
```

## List all villages

```Python hl_lines="2"
from pykhmernlp.address import km_villages

all_villages = km_villages()

print(f"Size Villages : {len(all_villages)}")
print(f"List of villages: {all_villages}")
```

## List villages from a specific province

```Python hl_lines="2"
from pykhmernlp.address import km_villages

battambang_villages = km_villages('battambang')

print(f"Size Battambang's Villages : {len(battambang_villages)}")
print(f"List battambang's villages: {battambang_villages}")
```

## List all communes

```Python hl_lines="2"
from pykhmernlp.address import km_commune

all_communes = km_commune()

print(f"Size Communes : {len(all_communes)}")
print(f"List of communes: {all_communes}")
```

## List communes from a specific province

```Python hl_lines="2"
from pykhmernlp.address import km_commune

kampot_communes = km_commune('kampot')

print(f"Size Kampot's Communes : {len(kampot_communes)}")
print(f"List kampot's communes: {kampot_communes}")
```

## List all districts

```Python hl_lines="2"
from pykhmernlp.address import km_districts

all_districts = km_districts()

print(f"Size Districts : {len(all_districts)}")
print(f"List of districts: {all_districts}")
```

## List districts from a specific province

```Python hl_lines="2"
from pykhmernlp.address import km_districts

kandal_districts = km_districts('kandal')

print(f"Size Kandal's Districts : {len(kandal_districts)}")
print(f"List kandal's districts: {kandal_districts}")
```

## List all provinces

```Python hl_lines="2"
from pykhmernlp.address import km_provinces

provinces = km_provinces()

print(f"Size Provinces : {len(provinces)}")
print(f"List of provinces: {provinces}")
```

<hr>

# More Details about functions

::: pykhmernlp.address