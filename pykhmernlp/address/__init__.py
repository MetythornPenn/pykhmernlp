import os
import csv
from pathlib import Path
from typing import List, Dict, Union

import pkg_resources

PHUM_TSV_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'address/address_data/phum.tsv')
KHUM_TSV_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'address/address_data/khum.tsv')
SROK_TSV_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'address/address_data/srok.tsv')
PROVINCE_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'address/address_data/province.txt')


def _load_tsv_data(tsv_path: str) -> Dict[str, List[str]]:
    data: Dict[str, List[str]] = {}
    with open(tsv_path, 'r', encoding='utf-8') as tsv_file:
        reader = csv.reader(tsv_file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            file_base_name, line = row
            if file_base_name not in data:
                data[file_base_name] = []
            data[file_base_name].append(line)
    return data


PHUM_DATA: Dict[str, List[str]] = _load_tsv_data(PHUM_TSV_PATH)
KHUM_DATA: Dict[str, List[str]] = _load_tsv_data(KHUM_TSV_PATH)
SROK_DATA: Dict[str, List[str]] = _load_tsv_data(SROK_TSV_PATH)


def _list_data(data: Dict[str, List[str]], province: str = 'all') -> List[str]:
    """
    Helper function to list all data from a specified path and filter by province name.

    Args:
        data (dict): The data dictionary to list data from.
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of data.
    """
    if province == 'all':
        result: List[str] = []
        for lines in data.values():
            result.extend(lines)
        return result
    else:
        if province in data:
            return data[province]
        else:
            raise ValueError(f"No data available for the province: {province}")
        

def km_villages(province: str = 'all') -> List[str]:
    """
    List all data from the phum data and filter by province name.

    Args:
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of villages.
    """
    return _list_data(PHUM_DATA, province)


def km_commune(province: str = 'all') -> List[str]:
    """
    List all data from the khum data and filter by province name.

    Args:
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of communes.
    """
    return _list_data(KHUM_DATA, province)


def km_districts(province: str = 'all') -> List[str]:
    """
    List all data from the srok data and filter by province name.

    Args:
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of districts.
    """
    return _list_data(SROK_DATA, province)


def km_provinces() -> List[str]:
    """
    List all provinces from the province data.

    Returns:
        List[str]: A list of provinces.
    """
    with open(PROVINCE_PATH, 'r', encoding='utf-8-sig') as file:
        provinces: List[str] = [line.strip() for line in file if line.strip()]
    return provinces
