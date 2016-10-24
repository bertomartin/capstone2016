"""
This module contains code to do the following:
    1. Text tokenization
    2. Text normalization
    3. n-grams
    4. POS Tagging
    5. language detection
"""
import nltk
from nltk.tokenize import LineTokenizer
from nltk.tokenize import TreebankWordTokenizer


# =================== Tokenization ===================
def sl_tokenizer(corpus):
    lines = sentence_tokenizer(corpus)
    return [word_tokenizer(sent) for sent in lines]


# 1 sentence segmentation
def sentence_tokenizer(corpus):
    line_tokenizer = LineTokenizer()
    song_lines = line_tokenizer.tokenize(corpus)
    return song_lines


# 2 tokenizer
def word_tokenizer(sent):
    sl_word_tokenizer = TreebankWordTokenizer()
    line_tokens = sl_word_tokenizer.tokenize(sent)
    return line_tokens

# ------------------ /Tokenization --------------------


# =================== Normalization ===================
def sl_normalization():
    # 1. remove punctuations
    # 2. lower-case
    # 3. stop-word removal (optional)
    # 4. lemmatization
    # 5. stemming
    # 6. text expansion/abbreviation expansion (don't ==> do not)
    # 7. synonyms
    # 8. convert numbers to words
    pass

# ----------------- Normalization ---------------------


# ================= Vectorization =====================

def vectorize_corpus(corpus, kind='BoW'):
    pass
# ----------------- Vectorization ---------------------


def sl_ngrams(n_gram = 2):
    # return the n-grams
    pass


def sl_tags(text):
    # return pos tags for each word
    pass


def sl_language(text):
    # detect language
    pass