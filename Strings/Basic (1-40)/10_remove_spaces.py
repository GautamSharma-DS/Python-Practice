# =========================================================================================
#                              QUESTION 10: REMOVE SPACES
# =========================================================================================


# i). USING replace()

s = "Python is easy"
print("replace():", s.replace(" ", ""))


# ii). USING FOR LOOP

s = "Hello World"
result = ""

for ch in s:
    if ch != " ":
        result += ch

print("For loop:", result)


# iii). USING WHILE LOOP

s = "Data Science"
result = ""
i = 0

while i < len(s):
    if s[i] != " ":
        result += s[i]
    i += 1

print("While loop:", result)


# iv). USING join() + split()

s = "Machine Learning"
result = "".join(s.split())

print("join() + split():", result)


# v). USING LIST COMPREHENSION

s = "Open AI Chat GPT"
result = "".join([ch for ch in s if ch != " "])

print("List comprehension:", result)


# vi). REMOVE ALL WHITESPACE USING isspace()

s = "A B\tC\nD"
result = "".join(ch for ch in s if not ch.isspace())

print("isspace():", result)


# vii). USING REGULAR EXPRESSION

import re

s = "Remove all spaces"
result = re.sub(r"\s+", "", s)

print("Regex:", result)


# viii). USING filter()

s = "Filter Method Example"
result = "".join(filter(lambda ch: ch != " ", s))

print("filter():", result)


# ix). USING translate()

s = "Remove Spaces Fast"
result = s.translate(str.maketrans("", "", " "))

print("translate():", result)


# x). USING RECURSION

def remove_spaces_recursive(s):
    if not s:
        return ""

    if s[0] == " ":
        return remove_spaces_recursive(s[1:])

    return s[0] + remove_spaces_recursive(s[1:])


print("Recursion:", remove_spaces_recursive("A B C D"))


# xi). REMOVE ONLY LEADING AND TRAILING SPACES

s = "   Python Practice   "
result = s.strip()

print("strip():", result)


# xii). REMOVE TABS AND NEWLINES ALSO

s = "A B\tC\nD"
result = ""

for ch in s:
    if not ch.isspace():
        result += ch

print("All whitespace:", result)


# xiii). REMOVE SPACES FROM EACH WORD IN LIST

items = ["A B", "C D", "E F"]
result = []

for item in items:
    result.append(item.replace(" ", ""))

print("List of strings:", result)
