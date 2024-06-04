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

::: pykhmernlp.address