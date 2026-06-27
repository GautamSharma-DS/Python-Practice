# =========================================================================================
#                              QUESTION 11: REMOVE EXTRA SPACES
# =========================================================================================


# i). USING split() + join()

s = "Python    is     easy"
result = " ".join(s.split())

print("split() + join():", result)


# ii). USING FOR LOOP

s = "Hello     World   Python"
result = ""
previous_space = False

for ch in s.strip():
    if ch == " ":
        if not previous_space:
            result += ch
        previous_space = True
    else:
        result += ch
        previous_space = False

print("For loop:", result)


# iii). USING WHILE LOOP

s = "Data     Science     Course"
result = ""
i = 0

while i < len(s.strip()):
    ch = s.strip()[i]
    if ch != " " or (result and result[-1] != " "):
        result += ch
    i += 1

print("While loop:", result)


# iv). USING REGULAR EXPRESSION

import re

s = "Machine      Learning      Basics"
result = re.sub(r"\s+", " ", s).strip()

print("Regex:", result)


# v). USING FUNCTION

def remove_extra_spaces(s):
    return " ".join(s.split())


print("Function:", remove_extra_spaces("  Good     Morning   India  "))


# vi). USING filter() AFTER split()

s = "  Python     basic      strings  "
words = list(filter(None, s.split(" ")))
result = " ".join(words)

print("filter() + split:", result)


# vii). USING MANUAL WORD COLLECTION

s = "  Learn     Python    Daily  "
words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    elif word:
        words.append(word)
        word = ""

if word:
    words.append(word)

print("Manual words:", " ".join(words))


# viii). USING RECURSION ON WORDS

def join_words(words):
    if not words:
        return ""

    if len(words) == 1:
        return words[0]

    return words[0] + " " + join_words(words[1:])


s = "  Clean    extra      spaces "
print("Recursion:", join_words(s.split()))


# ix). KEEP SINGLE SPACE BUT PRESERVE WORD ORDER

s = "Python        basics       are     important"
words = []
current = ""

for ch in s:
    if ch != " ":
        current += ch
    elif current:
        words.append(current)
        current = ""

if current:
    words.append(current)

print("Manual clean:", " ".join(words))


# x). REMOVE EXTRA SPACES FROM EACH STRING IN LIST

sentences = ["  hello    world  ", "Python     is easy"]
cleaned = []

for sentence in sentences:
    cleaned.append(" ".join(sentence.split()))

print("List of strings:", cleaned)


# xi). HANDLE TABS AND NEWLINES

s = "Python\t\tis\n\nsimple"
result = " ".join(s.split())

print("Tabs and newlines:", result)
