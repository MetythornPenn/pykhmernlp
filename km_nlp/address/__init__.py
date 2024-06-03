import os

PHUM_PATH = 'km_nlp/address/address_data/phum/'
KHUM_PATH = 'km_nlp/address/address_data/khum/'
SROK_PATH = 'km_nlp/address/address_data/srok/'
PROVINCE_PATH = 'km_nlp/address/address_data/province/'

def _list_data(path, province='all'):
    """
    Helper function to list all data from a specified path and filter by province name.

    Args:
        path (str): The directory path to list data from.
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of data.
    """
    data = []
    if province == 'all':
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                with open(os.path.join(path, filename), 'r', encoding='utf-8-sig') as file:
                    data.extend([line.strip() for line in file if line.strip()])
    else:
        province_file = f"{province}.txt"
        province_path = os.path.join(path, province_file)
        if os.path.isfile(province_path):
            with open(province_path, 'r', encoding='utf-8-sig') as file:
                data = [line.strip() for line in file if line.strip()]
        else:
            raise ValueError(f"No data available for the province: {province}")

    return data

def km_villages(province='all'):
    """
    List all data from the phum folder and filter by province name.

    Args:
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of villages.
    """
    return _list_data(PHUM_PATH, province)

def km_commune(province='all'):
    """
    List all data from the khum folder and filter by province name.

    Args:
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of communes.
    """
    return _list_data(KHUM_PATH, province)

def km_districts(province='all'):
    """
    List all data from the srok folder and filter by province name.

    Args:
        province (str): The province name to filter by. If 'all', list all data.

    Returns:
        List[str]: A list of districts.
    """
    return _list_data(SROK_PATH, province)

def km_provinces():
    """
    List all provinces from the province folder.

    Returns:
        List[str]: A list of provinces.
    """
    with open(os.path.join(PROVINCE_PATH, 'province.txt'), 'r', encoding='utf-8-sig') as file:
        provinces = [line.strip() for line in file if line.strip()]
    return provinces
