import re
def is_pangram(sentence):
    letters = r"[a-z]"
    letters = re.findall(letters,sentence.lower())
    return len(set(letters)) == 26
