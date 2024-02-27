# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
# 49. Group Anagrams
# Since sorting a word can be boiled down to O(1) in this scenario, and appending and searching a HashTable is O(1), this is O(n), which is good :)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsDict = {}
        
        for i, word in enumerate(strs): 
            sortedWord = ''.join(sorted(word))
            if sortedWord not in wordsDict:
                wordsDict[sortedWord] = [strs[i]]
            else:
                wordsDict[sortedWord].append(strs[i])
        
        return list(wordsDict.values())
