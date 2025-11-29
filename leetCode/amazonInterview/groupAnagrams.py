# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
d = defaultdict(list)

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        all_chars = [0]*26
        for char in word:
            all_chars[ord(char) - ord('a')] += 1
        anagrams[tuple(all_chars)].append(word)
    return list(anagrams.values())    

# what is the complexity of this approach?
# Time: O(N K) where N is the number of words and K is the maximum length of a word
# Space: O(N K) in the worst case, if all words are different, we store all words in the anagrams dictionary

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))


