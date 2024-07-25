import streamlit as st
from text_generator import load_data, create_wordlist, create_trigrams, create_vocab, generate

st.set_page_config(page_title="Text Generator", page_icon="📝")

st.title("📝 Text Generator")

@st.cache_resource
def load_model():
    data = load_data('sherlock.txt')
    wordlist = create_wordlist(data)
    trigrams = create_trigrams(data)
    vocab = create_vocab(trigrams)
    return wordlist, vocab

wordlist, vocab = load_model()

st.write("This app generates text based on the input you provide, using a trigram model trained on Sherlock Holmes stories.")

input_text = st.text_input("Enter your starting text (at least two words):", "They are in the")
num_words = st.slider("Number of words to generate:", 1, 200, 50)

if st.button("Generate Text"):
    if len(input_text.split()) < 2:
        st.error("Please enter at least two words.")
    else:
        generated_text = generate(input_text, num_words, vocab, wordlist)
        st.write("Generated text:")
        st.write(input_text + generated_text)
