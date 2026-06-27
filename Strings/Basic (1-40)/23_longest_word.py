# =========================================================================================
#                              QUESTION 23: LONGEST WORD
# =========================================================================================


# i). USING max()

s = "Python programming language"
word = max(s.split(), key=len)

print("max():", word)


# ii). USING FOR LOOP

s = "Data science and machine learning"
longest = ""

for word in s.split():
    if len(word) > len(longest):
        longest = word

print("For loop:", longest)


# iii). USING SORT

s = "I love problem solving"
words = s.split()
words.sort(key=len, reverse=True)

print("sort():", words[0])


# iv). USING FUNCTION

def longest_word(s):
    longest = ""

    for word in s.split():
        if len(word) > len(longest):
            longest = word

    return longest


print("Function:", longest_word("Consistency builds confidence"))


# v). USING REGULAR EXPRESSION

import re

s = "Python, programming and debugging!"
words = re.findall(r"[A-Za-z]+", s)
word = max(words, key=len)

print("Regex:", word)


# vi). USING RECURSION

def longest_word_recursive(words):
    if len(words) == 1:
        return words[0]

    longest = longest_word_recursive(words[1:])
    return words[0] if len(words[0]) >= len(longest) else longest


print("Recursion:", longest_word_recursive("learn python consistently".split()))


# vii). RETURN ALL LONGEST WORDS

s = "red blue green white"
words = s.split()
max_len = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_len]

print("All longest:", longest_words)


# viii). LONGEST WORD IGNORING PUNCTUATION

s = "Python, programming! debug."
words = re.findall(r"[A-Za-z]+", s)

print("Ignore punctuation:", max(words, key=len))


# ix). LONGEST WORD IN EACH LINE

text = """Python is easy
Practice programming daily"""

answers = []

for line in text.splitlines():
    answers.append(max(line.split(), key=len))

print("Each line:", answers)


# x). LONGEST WORD LENGTH

s = "Consistency builds confidence"
word = max(s.split(), key=len)

print("Longest length:", len(word))
