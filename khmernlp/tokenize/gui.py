import streamlit as st
from multicut import Tokenizer, dict_trie, khmer_words
import re

def load_custom_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        custom_words = file.read().splitlines()
    return custom_words

def save_custom_words(file_path, custom_words):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in custom_words:
            file.write(word + '\n')

def segment_text(text, custom_words):
    ignore_words = ['\n', ' ', '  ', '\u200b', '\t', '\r']

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
    st.title("Khmer Text Segmenter")

    # Input form for text
    with st.sidebar:
        st.subheader("Input Text")
        input_text = st.text_area("Enter Khmer text here", height=200)

    # Button to segment text
    if st.sidebar.button("Segment Text"):
        if input_text.strip():
            custom_words = load_custom_words("custom_words.txt")
            segmented_text = segment_text(input_text, custom_words)
            st.subheader("Segmented Text")
            st.text_area("Segmented Khmer text", segmented_text, height=200)
        else:
            st.warning("Please enter some text to segment.")

    # Form to input new words to custom_words.txt
    st.sidebar.subheader("Add New Words")
    new_words = st.sidebar.text_area("Enter new words (one per line)")
    if new_words:
        new_words_list = new_words.split('\n')
        custom_words = load_custom_words("custom_words.txt")
        custom_words.extend(new_words_list)
        save_custom_words("custom_words.txt", custom_words)
        st.success("New words added to custom_words.txt")

    # Display current custom words
    st.sidebar.subheader("Current Custom Words")
    current_custom_words = load_custom_words("custom_words.txt")
    st.sidebar.text_area("Custom Words", '\n'.join(current_custom_words), height=200)

if __name__ == "__main__":
    main()
