import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

def findSignature(word):
    return ''.join(sorted(word)) # this will sort the letters on the word
           # sorted(word) will return a list of characters
           # ''.join(wordList) will join the list into a string using '' as a separator, so no separator 

words = sorted({word.strip().lower() for word in open("br-latin1.txt", "r", encoding="latin1")}) # import all words, turn to smallcase and sort them
wordsBySignature = collections.defaultdict(set) # defaultdict will create an empty set as value when the key is not present, before adding the actual value

for word in words:
    wordsBySignature[findSignature(word)].add(word) # make a dictionary of words by their signature (sorted characters in it)
                                                    # this way the anagrams will fall on the same set

#onlyAnagrams = {signature: wordSet for signature, wordSet in wordsBySignature.items() if len(wordSet) > 1}
#longestAnagrams = [onlyAnagrams[signature] for signature in sorted(onlyAnagrams.keys(), key=len, reverse=True)]

word = input("Escreva uma palavra para achar anagramas: ")
try:
    wordsSet = wordsBySignature[findSignature(word)]
    if(len(wordsSet) == 0):
        print("Nenhum anagrama encontrado.")
    else:
        print(wordsBySignature[findSignature(word)])
except:
    print("Nenhum anagrama encontrado.")
