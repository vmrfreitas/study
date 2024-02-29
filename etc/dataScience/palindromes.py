import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

def findSignature(word):
    return ''.join(sorted(word))

words = sorted({word.strip().lower() for word in open("br-latin1.txt", "r", encoding="latin1")}) # import all words, turn to smallcase and sort them
wordsByPalindrome = collections.defaultdict(set) # defaultdict will create an empty set as value when the key is not present, before adding the actual value

for word in words:
    reversedWord = word[::-1] # word[::-1] will go through the entire word backwards
    if reversedWord in wordsByPalindrome:
        wordsByPalindrome[reversedWord].add(word) # if the reversed word is already there, add it together with it
                                                  # words that are palindromes of one another will be added to the same set
    else:
        wordsByPalindrome[word].add(word) # if the reversed word is not there yet, just add the word 

# removes all the words that are not palindromes of other words, words that are added by themselves
onlyPalindromes = {word: palindromeSet for word, palindromeSet in wordsByPalindrome.items() if len(palindromeSet) > 1}

# adds the true palindrome words, words that are equal when reversed
for word in words: 
    reversedWord = word[::-1]
    if reversedWord == word:
        onlyPalindromes[word] = set()
        onlyPalindromes[word].add(word)

print(onlyPalindromes)