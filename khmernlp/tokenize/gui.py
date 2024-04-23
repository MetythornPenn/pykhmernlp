import streamlit as st
import random
from multicut import Tokenizer, dict_trie, khmer_words
import re

def load_custom_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        custom_words = file.read().splitlines()
    return custom_words

def save_custom_words(file_path, custom_words):
    with open(file_path, 'w', encoding='utf-8') as file:
        unique_words = set(custom_words)
        cleaned_words = [word.strip() for word in unique_words if word.strip()]
        file.write('\n'.join(cleaned_words))

def segment_text(text, custom_words):
    ignore_words = [' ', '  ', '\u200b', '\t', '\r']

    correct_words = {
        "ពិេ សស": "ពិេសស",
        "ពីេសស": "ពិេសស",
        "ខ្បាល": "ក្បាល",
        "កម្ពុ": "កម្ពុជា",
    }

    # Convert custom_words to a set for faster lookup
    custom_words_set = set(custom_words)

    # Initialize the tokenizer
    trie = dict_trie(dict_source=khmer_words() | custom_words_set)
    custom_tokenizer = Tokenizer(custom_dict=trie, engine="multi_cut")

    # Segment sentences
    lines = text.split('\n')

    segmented_text = []
    for line in lines:
        if not line.strip():  # Skip empty lines
            segmented_text.append('')
            continue

        # Tokenize words in the line
        words = custom_tokenizer.word_tokenize(line)

        # Process each word
        segmented_words = []
        for word in words:
            if word not in ignore_words:
                corrected_word = correct_words.get(word, word)  # Get corrected word or use original word
                segmented_words.append(corrected_word)

        # Join segmented words back into line
        segmented_text.append(' '.join(segmented_words))

    return '\n'.join(segmented_text)

def main():

    # Input form for text
    with st.sidebar:
        st.title("Khmer Text Segmenter")
        st.subheader("Input Text")
        input_text = st.text_area("Enter Khmer text here", key=hash("input_text"), height=400)

    # Button to segment text
    if st.sidebar.button("Segment Text"):
        if input_text.strip():
            custom_words = load_custom_words("custom_words.txt")
            segmented_text = segment_text(input_text, custom_words)
            st.subheader("Segmented Text")
            # Use HTML formatting to insert a special Unicode character for space and apply CSS to it
            html_segmented_text = segmented_text.replace(' ', f'<span style="color: {random.choice(["blue", "red", "green", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"])}">&#x25a0;</span>')
            st.markdown(html_segmented_text, unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to segment.")

    # Form to input new words to custom_words.txt
    st.sidebar.subheader("Add New Words")
    new_words = st.sidebar.text_area("Enter new words (one per line)", key=hash("new_words"), height=50)
    if new_words:
        new_words_list = new_words.split('\n')
        custom_words = load_custom_words("custom_words.txt")
        custom_words.extend(new_words_list)
        save_custom_words("custom_words.txt", custom_words)
        st.success("New words added to custom_words.txt")

    # Button to save new words to custom_words.txt
    st.sidebar.subheader("Save New Words")
    if st.sidebar.button("Save New Words", key=hash("save_new_words")):
        new_words = st.sidebar.text_area("Enter new words (one per line)", key=hash("new_words_save"), height=200)
        if new_words:
            new_words_list = new_words.split('\n')
            custom_words = load_custom_words("custom_words.txt")
            custom_words.extend(new_words_list)
            save_custom_words("custom_words.txt", custom_words)
            st.success("New words saved to custom_words.txt")

if __name__ == "__main__":
    main()
