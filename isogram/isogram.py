def is_isogram(string):
    if "-" in string:
        string = string.replace("-", "")
    if " " in string:
        string = string.replace(" ", "")
    return len(set(string.lower())) == len(string.lower())
