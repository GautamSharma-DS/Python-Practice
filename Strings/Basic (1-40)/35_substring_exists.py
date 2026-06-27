# =========================================================================================
#                              QUESTION 35: SUBSTRING EXISTS
# =========================================================================================


# i). USING in OPERATOR

s = "Python programming"
sub = "gram"

print("in operator:", sub in s)


# ii). USING find()

s = "Hello World"
sub = "World"

print("find():", s.find(sub) != -1)


# iii). USING index() WITH try-except

s = "Data Science"
sub = "Science"

try:
    s.index(sub)
    exists = True
except ValueError:
    exists = False

print("index():", exists)


# iv). MANUAL CHECK

s = "programming"
sub = "gram"
exists = False

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        exists = True
        break

print("Manual:", exists)


# v). USING FUNCTION

def substring_exists(s, sub):
    return sub in s


print("Function:", substring_exists("Python Practice", "Practice"))


# vi). USING REGULAR EXPRESSION

import re

s = "Python programming"
sub = "gram"

print("Regex:", re.search(re.escape(sub), s) is not None)


# vii). CASE-INSENSITIVE CHECK

s = "Data Science"
sub = "science"

print("Case-insensitive:", sub.lower() in s.lower())


# viii). USING startswith() ON SLICES

s = "hello world"
sub = "world"
exists = False

for i in range(len(s)):
    if s.startswith(sub, i):
        exists = True
        break

print("startswith():", exists)


# ix). CHECK MULTIPLE SUBSTRINGS

s = "Python programming"
subs = ["Py", "gram", "java"]
answers = {}

for sub in subs:
    answers[sub] = sub in s

print("Multiple substrings:", answers)


# x). CHECK WHOLE WORD SUBSTRING

s = "Python programming language"
sub = "programming"
words = s.split()

print("Whole word:", sub in words)


# xi). CHECK PREFIX OR SUFFIX

s = "programming"
sub = "pro"

print("Prefix:", s.startswith(sub))
print("Suffix:", s.endswith("ing"))
