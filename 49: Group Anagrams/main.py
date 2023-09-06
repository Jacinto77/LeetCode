from collections import defaultdict


def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(strings))
