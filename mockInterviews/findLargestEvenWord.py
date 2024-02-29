# given a sentence, find the first largest even word on it
#
# example: "I am a sentence lol JACQUARD"
# result = sentence
# even though JACQUARD also has 8 letters, sentence came first

sentence = "I am a sentenc lol JACQUARD" # for testing

words = sentence.split()
maxWord = ''
for word in words:
    if len(word)%2 == 0: #it is even
        if len(word) > len(maxWord):
            maxWord = word

print(maxWord)

# this oneis pretty simple, and it is O(n), I don't believe there's any faster way...