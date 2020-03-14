import re
from collections import Counter

def count_words(sentence):
    word = re.findall("[a-zA-Z\d]+(?:\'t)?", sentence.lower())
    return Counter(word)