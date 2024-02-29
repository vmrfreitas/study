import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

def findSignature(word):
    return ''.join(sorted(word))

words = sorted({word.strip().lower() for word in open("br-latin1.txt", "r", encoding="latin1")})
wordsByPalindrome = collections.defaultdict(set)

for word in words:
    reversedWord = word[::-1]
    if reversedWord in wordsByPalindrome:
        wordsByPalindrome[reversedWord].add(word)
    else:
        wordsByPalindrome[word].add(word)

# removes all the words that are not palindromes of other words
onlyPalindromes = {word: palindromeSet for word, palindromeSet in wordsByPalindrome.items() if len(palindromeSet) > 1}

# adds the true palindrome words
for word in words: 
    reversedWord = word[::-1]
    if reversedWord == word:
        onlyPalindromes[word] = set()
        onlyPalindromes[word].add(word)

print(onlyPalindromes)