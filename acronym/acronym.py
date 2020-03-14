def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ").upper().split()
    acronym = ""
    for word in words:
        print(word)
        acronym += word[0]
    return acronym
        
    