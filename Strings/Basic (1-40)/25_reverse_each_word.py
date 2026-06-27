# =========================================================================================
#                              QUESTION 25: REVERSE EACH WORD
# =========================================================================================


# i). USING split() AND SLICING

s = "Python is easy"
result = " ".join(word[::-1] for word in s.split())

print("Slicing:", result)


# ii). USING FOR LOOP

s = "Hello World"
result_words = []

for word in s.split():
    result_words.append(word[::-1])

print("For loop:", " ".join(result_words))


# iii). USING reversed()

s = "Data Science"
result = " ".join("".join(reversed(word)) for word in s.split())

print("reversed():", result)


# iv). USING NESTED LOOP

s = "Good Morning"
result_words = []

for word in s.split():
    rev = ""
    for ch in word:
        rev = ch + rev
    result_words.append(rev)

print("Nested loop:", " ".join(result_words))


# v). USING FUNCTION

def reverse_each_word(s):
    return " ".join(word[::-1] for word in s.split())


print("Function:", reverse_each_word("Python Practice"))


# vi). USING map()

s = "Map can reverse"
result = " ".join(map(lambda word: word[::-1], s.split()))

print("map():", result)


# vii). PRESERVE ORIGINAL SPACING USING REGEX

import re

s = "Hello   World"
parts = re.split(r"(\s+)", s)
result = "".join(part[::-1] if not part.isspace() else part for part in parts)

print("Preserve spacing:", result)


# viii). USING STACK FOR EACH WORD

s = "Stack Logic"
result_words = []

for word in s.split():
    stack = list(word)
    rev = ""
    while stack:
        rev += stack.pop()
    result_words.append(rev)

print("Stack:", " ".join(result_words))


# ix). REVERSE EACH WORD BUT KEEP WORD ORDER AND PUNCTUATION ATTACHED

s = "Hello, world!"
result = " ".join(word[::-1] for word in s.split())

print("With punctuation:", result)


# x). REVERSE EACH WORD IN LIST OF STRINGS

sentences = ["Hello World", "Python Code"]
answers = []

for sentence in sentences:
    answers.append(" ".join(word[::-1] for word in sentence.split()))

print("List of sentences:", answers)


# xi). REVERSE ONLY WORDS LONGER THAN 3

s = "I love Python code"
result_words = []

for word in s.split():
    if len(word) > 3:
        result_words.append(word[::-1])
    else:
        result_words.append(word)

print("Long words only:", " ".join(result_words))
