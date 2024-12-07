from fastapi import FastAPI, HTTPException, Query, APIRouter
from typing import Optional
from pykhmernlp.address import km_villages, km_provinces

router = APIRouter()

list_province = [
    "banteaymeanchey",
    "battambang",
    "kampongcham",
    "kampongchhnang",
    "kampongspeu",
    "kampongthom",
    "kampot",
    "kandal",
    "keb",
    "kohkong",
    "kratie",
    "mundulkiri",
    "ordomeanchey",
    "pailin",
    "phnompenh",
    "preahsihanouk",
    "preahvihear",
    "preyveng",
    "pursat",
    "ratanakiri",
    "siemreap",
    "stungtraeng",
    "svayrieng",
    "takeo"
]

@router.get("/provinces")
def list_provinces():
    return {
        "size": len(km_provinces()),
        "provinces_kh": km_provinces(),
        "provinces_en": list_province
    }


@router.get("/villages")
def get_villages(
    province: Optional[str] = Query(None, description="Name of the province, e.g. 'battambang'")
):
    try:
        if province is None:
            villages = km_villages()
            
        province = province.lower()

        if province not in list_province and province != None:
            raise HTTPException(status_code=404, detail=f"Province '{province}' not found.")
        else: 
            villages = km_villages(province)
    except Exception as e:
        raise HTTPException(
            status_code=404, 
            detail=f"Province '{province}' not found or an error occurred: {str(e)}"
        )

    return {
        "province": province,
        "size": len(villages),
        "villages": villages
    }
