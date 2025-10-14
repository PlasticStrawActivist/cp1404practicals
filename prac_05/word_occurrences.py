"""
Word Occurrences
Estimate: 8 minutes
Actual:   6 minutes, 28 seconds
"""

text = input("Text: ")
word_occurrences = {}

for word in text.lower().split(" "):
    if word in word_occurrences:
        word_occurrences[word] += 1
    else:
        word_occurrences[word] = 1

word_occurrences = dict(sorted(word_occurrences.items()))

width = max([len(word) for word in word_occurrences.keys()])

for word, number_of_occurrences in word_occurrences.items():
    print(f"{word:{width}} : {number_of_occurrences}")
