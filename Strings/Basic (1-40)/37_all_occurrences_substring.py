# =========================================================================================
#                              QUESTION 37: ALL OCCURRENCES OF SUBSTRING
# =========================================================================================


# i). USING find() IN LOOP

s = "abababab"
sub = "ab"
positions = []
start = 0

while True:
    index = s.find(sub, start)
    if index == -1:
        break
    positions.append(index)
    start = index + 1

print("find() loop:", positions)


# ii). USING FOR LOOP

s = "mississippi"
sub = "issi"
positions = []

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        positions.append(i)

print("For loop:", positions)


# iii). USING REGULAR EXPRESSION

import re

s = "aaaa"
sub = "aa"
positions = [m.start() for m in re.finditer(f"(?={re.escape(sub)})", s)]

print("Regex:", positions)


# iv). NON-OVERLAPPING OCCURRENCES

s = "aaaa"
sub = "aa"
positions = []
start = 0

while True:
    index = s.find(sub, start)
    if index == -1:
        break
    positions.append(index)
    start = index + len(sub)

print("Non-overlapping:", positions)


# v). USING FUNCTION

def all_occurrences(s, sub):
    positions = []

    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            positions.append(i)

    return positions


print("Function:", all_occurrences("banana", "an"))


# vi). USING startswith()

s = "abababa"
sub = "aba"
positions = []

for i in range(len(s)):
    if s.startswith(sub, i):
        positions.append(i)

print("startswith():", positions)


# vii). CASE-INSENSITIVE OCCURRENCES

s = "PyPYpy"
sub = "py"
positions = []
lower_s = s.lower()
lower_sub = sub.lower()

for i in range(len(lower_s) - len(lower_sub) + 1):
    if lower_s[i:i + len(lower_sub)] == lower_sub:
        positions.append(i)

print("Case-insensitive:", positions)


# viii). USING RECURSION

def occurrences_recursive(s, sub, index=0):
    if index > len(s) - len(sub):
        return []

    if s[index:index + len(sub)] == sub:
        return [index] + occurrences_recursive(s, sub, index + 1)

    return occurrences_recursive(s, sub, index + 1)


print("Recursion:", occurrences_recursive("aaaa", "aa"))


# ix). COUNT OCCURRENCES ONLY

s = "abababab"
sub = "ab"
count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        count += 1

print("Occurrence count:", count)


# x). FIND OCCURRENCES FOR MULTIPLE SUBSTRINGS

s = "banana"
subs = ["an", "na", "ba"]
answers = {}

for sub in subs:
    answers[sub] = []
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            answers[sub].append(i)

print("Multiple substrings:", answers)


# xi). WORD OCCURRENCES

s = "python is easy and python is popular"
word = "python"
positions = []
words = s.split()

for i in range(len(words)):
    if words[i] == word:
        positions.append(i)

print("Word occurrences:", positions)
