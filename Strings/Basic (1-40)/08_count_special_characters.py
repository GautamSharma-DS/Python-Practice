# =========================================================================================
#                              QUESTION 08: COUNT SPECIAL CHARACTERS
# =========================================================================================


# i). USING FOR LOOP

s = "Hello@123#World!"
count = 0

for ch in s:
    if not ch.isalnum() and not ch.isspace():
        count += 1

print("For loop:", count)


# ii). USING WHILE LOOP

s = "Python$ Practice%"
count = 0
i = 0

while i < len(s):
    if not s[i].isalnum() and not s[i].isspace():
        count += 1
    i += 1

print("While loop:", count)


# iii). USING sum()

s = "a+b=c?"
count = sum(1 for ch in s if not ch.isalnum() and not ch.isspace())

print("sum():", count)


# iv). USING LIST COMPREHENSION

s = "mail@example.com"
special = [ch for ch in s if not ch.isalnum() and not ch.isspace()]

print("List comprehension:", len(special))


# v). USING string.punctuation

import string

s = "Price: $50!"
count = sum(1 for ch in s if ch in string.punctuation)

print("string.punctuation:", count)


# vi). USING REGULAR EXPRESSION

import re

s = "A#B@C123"
count = len(re.findall(r"[^A-Za-z0-9\s]", s))

print("Regex:", count)


# vii). USING FUNCTION

def count_special_characters(s):
    return sum(1 for ch in s if not ch.isalnum() and not ch.isspace())


print("Function:", count_special_characters("Hi! How are you?"))


# viii). USING map()

s = "A@B#C$"
count = sum(map(lambda ch: not ch.isalnum() and not ch.isspace(), s))

print("map():", count)


# ix). USING RECURSION

def count_special_recursive(s):
    if not s:
        return 0

    first = int(not s[0].isalnum() and not s[0].isspace())
    return first + count_special_recursive(s[1:])


print("Recursion:", count_special_recursive("Hi@2026!"))


# x). COUNT WITH CUSTOM SPECIAL SET

s = "a+b=c*d"
special_set = "+=*"
count = sum(1 for ch in s if ch in special_set)

print("Custom set:", count)


# xi). FIND POSITIONS OF SPECIAL CHARACTERS

s = "A@B#C$D"
positions = []

for i in range(len(s)):
    if not s[i].isalnum() and not s[i].isspace():
        positions.append(i)

print("Special positions:", positions)


# xii). STORE SPECIAL CHARACTERS IN LIST

s = "mail@example.com!"
special_chars = []

for ch in s:
    if not ch.isalnum() and not ch.isspace():
        special_chars.append(ch)

print("Special list:", special_chars)
print("Special list count:", len(special_chars))


# xiii). COUNT SPECIAL CHARACTERS IN EACH WORD

s = "hi! mail@example.com price$50"
word_counts = {}

for word in s.split():
    word_counts[word] = sum(1 for ch in word if not ch.isalnum())

print("Each word:", word_counts)


# xiv). COUNT ONLY SYMBOLS, NOT SPACES

s = "A + B = C"
count = 0

for ch in s:
    if not ch.isalnum() and ch != " ":
        count += 1

print("Symbols only:", count)


# xv). COUNT SPECIAL CHARACTERS FROM LIST OF STRINGS

items = ["a@b", "c#d$", "hello"]
count = 0

for item in items:
    count += sum(1 for ch in item if not ch.isalnum() and not ch.isspace())

print("List of strings:", count)
