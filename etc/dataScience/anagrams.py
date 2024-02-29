import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

def findSignature(word):
    return ''.join(sorted(word))

words = sorted({word.strip().lower() for word in open("br-latin1.txt", "r", encoding="latin1")})
wordsBySignature = collections.defaultdict(set)

for word in words:
    wordsBySignature[findSignature(word)].add(word)

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
