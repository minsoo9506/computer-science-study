# https://leetcode.com/problems/group-anagrams

anagrams = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

from collections import defaultdict

anagrams_dict = defaultdict(list) # defaultdict에 인자는 이런식으로 넣어야함

for anagram in anagrams:
    anagram_key = sorted(anagram)
    anagrams_dict[''.join(sorted(anagram))].append(anagram)
    
print(anagrams_dict.values())