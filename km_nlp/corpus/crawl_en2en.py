from bs4 import BeautifulSoup
import requests
import logging
import os
import csv

logger = logging.getLogger(__name__)

"""
Ref : https://github.com/benjihillard/English-Dictionary-Database/blob/main/dictionaryScript.py
"""

def crawl(alph):
    for letter in alph:
        # this can run a long time, it's helpful to know which letter it's on
        logger.info(f"Processing letter {letter}...")
        url = "http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_" + letter + ".html" # there is a page for each letter
        req = requests.get(url) # grab page
        soup = BeautifulSoup(req.text, "html.parser") # get parser
        dictionary = soup.find_all('p') # find all the dictionary entries
        for entries in dictionary:
            word = entries.find('b').getText() # get the word itself
            pos = entries.find('i').getText() # get the part of speech
            cut = len(word) + len(pos) + 4 # calculate how much word and pos take up
            definition = entries.getText()[cut:] # cut that from the total string to get definition
            yield word, pos, definition

if __name__ == '__main__':
    alph = "abcdefghijklmnopqrstuvwxyz"
    if os.environ.get('DEV'):
        alph = "x"
    
    # Open a TSV file for writing
    with open('english_dictionary.tsv', 'w', newline='', encoding='utf-8') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        # Write the header row
        writer.writerow(["word", "pos", "definition"])
        
        # Write the dictionary entries
        for word, pos, definition in crawl(alph):
            writer.writerow([word, pos, definition])
