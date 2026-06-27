# =========================================================================================
#                              QUESTION 24: SHORTEST WORD
# =========================================================================================


# i). USING min()

s = "Python programming language"
word = min(s.split(), key=len)

print("min():", word)


# ii). USING FOR LOOP

s = "Data science and machine learning"
words = s.split()
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("For loop:", shortest)


# iii). USING SORT

s = "I love problem solving"
words = s.split()
words.sort(key=len)

print("sort():", words[0])


# iv). USING FUNCTION

def shortest_word(s):
    words = s.split()
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    return shortest


print("Function:", shortest_word("Consistency builds confidence"))


# v). USING REGULAR EXPRESSION

import re

s = "Python, AI and ML!"
words = re.findall(r"[A-Za-z]+", s)
word = min(words, key=len)

print("Regex:", word)


# vi). USING RECURSION

def shortest_word_recursive(words):
    if len(words) == 1:
        return words[0]

    shortest = shortest_word_recursive(words[1:])
    return words[0] if len(words[0]) <= len(shortest) else shortest


print("Recursion:", shortest_word_recursive("learn python daily".split()))


# vii). RETURN ALL SHORTEST WORDS

s = "red blue ox go"
words = s.split()
min_len = min(len(word) for word in words)
shortest_words = [word for word in words if len(word) == min_len]

print("All shortest:", shortest_words)


# viii). SHORTEST WORD IGNORING PUNCTUATION

s = "Python, AI! ML."
words = re.findall(r"[A-Za-z]+", s)

print("Ignore punctuation:", min(words, key=len))


# ix). SHORTEST WORD IN EACH LINE

text = """Python is easy
Practice programming daily"""

answers = []

for line in text.splitlines():
    answers.append(min(line.split(), key=len))

print("Each line:", answers)


# x). SHORTEST WORD LENGTH

s = "Consistency builds confidence"
word = min(s.split(), key=len)

print("Shortest length:", len(word))
