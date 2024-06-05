import csv
import pkg_resources
from typing import List, Dict

KHMER_WORDS_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'corpus/icu_words.txt')
ENGLISH_WORDS_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'corpus/english_words.txt')
KHMER_DICTIONARY_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'corpus/khmer_dictionary.xlsx')
KHMER_DICTIONARY_TSV_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'corpus/khmer_dictionary.tsv')
ENGLISH_DICTIONARY_PATH: str = pkg_resources.resource_filename('pykhmernlp', 'corpus/english_dictionary.tsv')

def load_english_dictionary(file_path: str) -> List[Dict[str, str]]:
    dictionary: List[Dict[str, str]] = []
    csv.field_size_limit(100000000) 
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            dictionary.append(row)
    return dictionary

def load_khmer_dictionary(file_path: str) -> List[Dict[str, str]]:
    dictionary: List[Dict[str, str]] = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            dictionary.append(row)
    return dictionary

def en2en_dict(word: str) -> List[Dict[str, str]]:
    dictionary: List[Dict[str, str]] = load_english_dictionary(ENGLISH_DICTIONARY_PATH)
    word = word.lower()
    entries: List[Dict[str, str]] = [entry for entry in dictionary if entry['word'].lower() == word]
    result: List[Dict[str, str]] = []
    for entry in entries:
        result.append({
            'word': entry['word'],
            'pos': entry['pos'],
            'definition': entry['definition']
        })
    return result

def km2km_dict(word: str) -> List[Dict[str, str]]:
    dictionary: List[Dict[str, str]] = load_khmer_dictionary(KHMER_DICTIONARY_TSV_PATH)
    entries: List[Dict[str, str]] = [entry for entry in dictionary if entry['t_main'] == word]
    result: List[Dict[str, str]] = []
    for entry in entries:
        result.append({
            'word': entry['t_main'],
            'pronounce': entry['t_pron'],
            'pos': entry['t_pos'],
            'definition': entry['t_exp'],
            'example': entry['t_exam']
        })
    return result

def km_words() -> List[str]:
    with open(KHMER_WORDS_PATH, 'r', encoding='utf-8-sig') as file:
        words: List[str] = [line.strip() for line in file if line.strip()]
    return words

def en_words() -> List[str]:
    with open(ENGLISH_WORDS_PATH, 'r', encoding='utf-8-sig') as file:
        words: List[str] = [line.strip() for line in file if line.strip()]
    return words
