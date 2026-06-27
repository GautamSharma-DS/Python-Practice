# =========================================================================================
#                              QUESTION 06: COUNT LOWERCASE LETTERS
# =========================================================================================


# i). USING FOR LOOP

s = "Hello WORLD"
count = 0

for ch in s:
    if ch.islower():
        count += 1

print("For loop:", count)


# ii). USING WHILE LOOP

s = "PyTHon PrACtice"
count = 0
i = 0

while i < len(s):
    if s[i].islower():
        count += 1
    i += 1

print("While loop:", count)


# iii). USING sum()

s = "Data STRUCTURES"
count = sum(1 for ch in s if ch.islower())

print("sum():", count)


# iv). USING LIST COMPREHENSION

s = "OpenAI ChatGPT"
lower_chars = [ch for ch in s if ch.islower()]

print("List comprehension:", len(lower_chars))


# v). USING filter()

s = "Machine LEARNING"
count = len(list(filter(str.islower, s)))

print("filter():", count)


# vi). WITHOUT islower()

s = "abc DEF ghi"
count = 0

for ch in s:
    if "a" <= ch <= "z":
        count += 1

print("Without islower():", count)


# vii). USING FUNCTION

def count_lowercase(s):
    return sum(1 for ch in s if ch.islower())


print("Function:", count_lowercase("My Name Is GAUTAM"))


# viii). USING REGULAR EXPRESSION

import re

s = "PyTHON Practice"
count = len(re.findall(r"[a-z]", s))

print("Regex:", count)


# ix). USING map()

s = "Data SCIENCE"
count = sum(map(str.islower, s))

print("map():", count)


# x). USING RECURSION

def count_lowercase_recursive(s):
    if not s:
        return 0

    return int(s[0].islower()) + count_lowercase_recursive(s[1:])


print("Recursion:", count_lowercase_recursive("HeLLo WORld"))


# xi). FIND POSITIONS OF LOWERCASE LETTERS

s = "PyTHon PrACtice"
positions = []

for i in range(len(s)):
    if s[i].islower():
        positions.append(i)

print("Lowercase positions:", positions)


# xii). STORE LOWERCASE LETTERS IN LIST

s = "OpenAI ChatGPT"
lowercase_letters = []

for ch in s:
    if ch.islower():
        lowercase_letters.append(ch)

print("Lowercase letters:", lowercase_letters)
print("Lowercase letters count:", len(lowercase_letters))


# xiii). COUNT LOWERCASE IN EACH WORD

s = "My Name Is GAUTAM"
word_counts = {}

for word in s.split():
    word_counts[word] = sum(1 for ch in word if ch.islower())

print("Each word:", word_counts)


# xiv). USING ASCII ORD VALUE

s = "abc DEF xyz"
count = 0

for ch in s:
    if 97 <= ord(ch) <= 122:
        count += 1

print("ord():", count)


# xv). COUNT LOWERCASE FROM LIST OF STRINGS

words = ["Python", "JAVA", "CodeGPT"]
count = 0

for word in words:
    count += sum(1 for ch in word if ch.islower())

print("List of strings:", count)
