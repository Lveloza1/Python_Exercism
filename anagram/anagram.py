def find_anagrams(word, candidates):
    ans = []
    word = word.lower()
    for candidate in candidates:
        if sorted(word) == sorted(candidate.lower()) and candidate.lower() != word:
            ans.append(candidate)
    return ans
