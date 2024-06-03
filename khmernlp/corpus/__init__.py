import re
import pandas as pd

KHMER_WORDS_PATH = 'khmernlp/corpus/icu_words.txt'
ENGLISH_WORDS_PATH = 'khmernlp/corpus/english_words.txt'
KHMER_DICTIONARY_PATH = 'khmernlp/corpus/khmer_dictionary.xlsx'



def load_khmer_dictionary(file_path):
    df = pd.read_excel(file_path)
    return df


def km2km_dict(word):
    dictionary_df = load_khmer_dictionary(KHMER_DICTIONARY_PATH)
    entries = dictionary_df[dictionary_df['t_main'] == word]
    result = []
    for _, row in entries.iterrows():
        entry = {
            'word': row['t_main'],
            'pronounce': row['t_pron'],
            'pos': row['t_pos'],
            'definition': row['t_exp'],
            'example': row['t_exam']
        }
        result.append(entry)
    return result



def km_words():
    with open(KHMER_WORDS_PATH, 'r', encoding='utf-8-sig') as file:
        words = [line.strip() for line in file if line.strip()]
    return words


def en_words():
    with open(ENGLISH_WORDS_PATH, 'r', encoding='utf-8-sig') as file:
        words = [line.strip() for line in file if line.strip()]
    return words
