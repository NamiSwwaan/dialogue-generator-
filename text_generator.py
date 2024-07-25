import string
import random

def clean(word):
    checkers = ['\n']
    return ''.join([char for char in word if char not in string.punctuation and char not in checkers])

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def create_wordlist(data):
    wordlist = []
    for line in data:
        words = [clean(word.lower()) for word in line.split(" ")]
        for word in words:
            if word and word not in wordlist:
                wordlist.append(word)
    return wordlist

def create_trigrams(data):
    trigrams = []
    for line in data:
        words = [clean(word.lower()) for word in line.split(" ")]
        trigram = []
        for word in words:
            if word:
                if len(trigram) < 3:
                    trigram.append(word)
                else:
                    trigram.pop(0)
                    trigram.append(word)
                if len(trigram) == 3:
                    trigrams.append(trigram.copy())
    return trigrams

def create_vocab(trigrams):
    vocab = dict()
    for g in trigrams:
        if (g[0], g[1]) in vocab:
            vocab[(g[0], g[1])].append(g[2])
        else:
            vocab[(g[0], g[1])] = [g[2]]
    return vocab

def generate(text, n, vocab, wordlist):
    words = text.split(" ")
    if len(words) < 2:
        return "Input text should contain at least two words."
    n1 = words[-2]
    n2 = words[-1]
    generated_text = ""
    while n != 0:
        if vocab.get((n1, n2), False):
            generated_word = random.choice(vocab[(n1, n2)])
        else:
            generated_word = random.choice(wordlist)
        generated_text += " " + generated_word
        n1 = n2
        n2 = generated_word
        n -= 1
    return generated_text
