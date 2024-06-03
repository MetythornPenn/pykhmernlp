import re
import pandas as pd

KHMER_WORDS_PATH = 'pykhmernlp/corpus/icu_words.txt'
ENGLISH_WORDS_PATH = 'pykhmernlp/corpus/english_words.txt'
KHMER_DICTIONARY_PATH = 'pykhmernlp/corpus/khmer_dictionary.xlsx'
ENGLISH_DICTIONARY_PATH = 'pykhmernlp/corpus/english_dictionary.tsv'




def load_khmer_dictionary(file_path):
    df = pd.read_excel(file_path)
    return df

def load_english_dictionary(file_path):
    df = pd.read_csv(file_path, delimiter='\t')
    return df


def en2en_dict(word):
    dictionary_df = load_english_dictionary(ENGLISH_DICTIONARY_PATH)
    word = word.lower()
    dictionary_df['word'] = dictionary_df['word'].str.lower()
    
    entries = dictionary_df[dictionary_df['word'] == word]
    result = []
    for _, row in entries.iterrows():
        entry = {
            'word': row['word'],
            'pos': row['pos'],
            'definition': row['definition'],
        }
        result.append(entry)
    return result



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
