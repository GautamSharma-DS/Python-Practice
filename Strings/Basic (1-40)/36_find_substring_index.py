# =========================================================================================
#                              QUESTION 36: FIND SUBSTRING INDEX
# =========================================================================================


# i). USING find()

s = "Python programming"
sub = "gram"

print("find():", s.find(sub))


# ii). USING index()

s = "Hello World"
sub = "World"

print("index():", s.index(sub))


# iii). USING FOR LOOP

s = "programming"
sub = "gram"
index = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        index = i
        break

print("For loop:", index)


# iv). CASE-INSENSITIVE INDEX

s = "Python Practice"
sub = "practice"
index = s.lower().find(sub.lower())

print("Case-insensitive:", index)


# v). USING FUNCTION

def find_substring_index(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            return i

    return -1


print("Function:", find_substring_index("Data Science", "Science"))


# vi). USING REGULAR EXPRESSION

import re

s = "Python programming"
sub = "gram"
match = re.search(re.escape(sub), s)
index = match.start() if match else -1

print("Regex:", index)


# vii). USING startswith()

s = "hello world"
sub = "world"
index = -1

for i in range(len(s)):
    if s.startswith(sub, i):
        index = i
        break

print("startswith():", index)


# viii). FIND LAST INDEX USING rfind()

s = "abababab"
sub = "ab"

print("rfind():", s.rfind(sub))


# ix). FIND ALL FIRST INDEXES FOR MULTIPLE SUBSTRINGS

s = "Python programming"
subs = ["Py", "gram", "java"]
indexes = {}

for sub in subs:
    indexes[sub] = s.find(sub)

print("Multiple substrings:", indexes)


# x). FIND WORD INDEX

s = "Python programming language"
sub = "programming"
words = s.split()
index = words.index(sub) if sub in words else -1

print("Word index:", index)


# xi). FIND INDEX CASE-INSENSITIVE MANUALLY

s = "Data Science"
sub = "science"
index = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)].lower() == sub.lower():
        index = i
        break

print("Manual case-insensitive:", index)
