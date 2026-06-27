# =========================================================================================
#                              QUESTION 22: COUNT WORDS
# =========================================================================================


# i). USING split()

s = "Python is easy"
print("split():", len(s.split()))


# ii). USING FOR LOOP

s = "Hello world from Python"
count = 0
in_word = False

for ch in s:
    if ch.isspace():
        in_word = False
    elif not in_word:
        count += 1
        in_word = True

print("For loop:", count)


# iii). USING WHILE LOOP

s = "Data science is powerful"
count = 0
i = 0

while i < len(s):
    while i < len(s) and s[i].isspace():
        i += 1
    if i < len(s):
        count += 1
    while i < len(s) and not s[i].isspace():
        i += 1

print("While loop:", count)


# iv). USING REGULAR EXPRESSION

import re

s = "One, two and three"
words = re.findall(r"\b\w+\b", s)

print("Regex:", len(words))


# v). USING FUNCTION

def count_words(s):
    return len(s.split())


print("Function:", count_words("Good morning India"))


# vi). USING filter()

s = "  Python   is   simple  "
words = list(filter(None, s.split(" ")))

print("filter():", len(words))


# vii). USING REGULAR EXPRESSION FOR ALPHABET WORDS

s = "Python 3 is fun"
words = re.findall(r"[A-Za-z]+", s)

print("Regex alphabet words:", len(words))


# viii). USING RECURSION ON WORD LIST

def count_words_recursive(words):
    if not words:
        return 0

    return 1 + count_words_recursive(words[1:])


s = "Recursion counts words"
print("Recursion:", count_words_recursive(s.split()))


# ix). COUNT WORDS IGNORING PUNCTUATION

s = "Hello, world! Python."
words = re.findall(r"[A-Za-z]+", s)

print("Ignore punctuation:", len(words))


# x). COUNT WORDS IN EACH LINE

text = """Python is easy
Practice daily
Keep coding"""

line_counts = []

for line in text.splitlines():
    line_counts.append(len(line.split()))

print("Each line:", line_counts)


# xi). COUNT WORDS FROM LIST OF SENTENCES

sentences = ["Python is easy", "Strings are important"]
counts = []

for sentence in sentences:
    counts.append(len(sentence.split()))

print("List of sentences:", counts)
