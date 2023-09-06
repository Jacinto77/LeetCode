def is_anagram(s, t):
    letters = {}
    for letter in s:
        if letter not in letters.keys():
            letters[letter] = 1
        else:
            letters[letter] += 1

    letters2 = {}
    for letter in t:
        if letter not in letters2.keys():
            letters2[letter] = 1
        else:
            letters2[letter] += 1

    return letters == letters2


string_s = "anagram"
string_t = "nagaram"

print(is_anagram(string_s, string_t))  # expected output: True
