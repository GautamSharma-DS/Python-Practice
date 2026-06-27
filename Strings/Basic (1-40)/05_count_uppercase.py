# =========================================================================================
#                              QUESTION 05: COUNT UPPERCASE LETTERS
# =========================================================================================


# i). USING FOR LOOP

s = "Hello WORLD"
count = 0

for ch in s:
    if ch.isupper():
        count += 1

print("For loop:", count)


# ii). USING WHILE LOOP

s = "PyTHon PrACtice"
count = 0
i = 0

while i < len(s):
    if s[i].isupper():
        count += 1
    i += 1

print("While loop:", count)


# iii). USING sum()

s = "Data STRUCTURES"
count = sum(1 for ch in s if ch.isupper())

print("sum():", count)


# iv). USING LIST COMPREHENSION

s = "OpenAI ChatGPT"
upper_chars = [ch for ch in s if ch.isupper()]

print("List comprehension:", len(upper_chars))


# v). USING filter()

s = "Machine LEARNING"
count = len(list(filter(str.isupper, s)))

print("filter():", count)


# vi). WITHOUT isupper()

s = "ABC def GHI"
count = 0

for ch in s:
    if "A" <= ch <= "Z":
        count += 1

print("Without isupper():", count)


# vii). USING FUNCTION

def count_uppercase(s):
    return sum(1 for ch in s if ch.isupper())


print("Function:", count_uppercase("My Name Is GAUTAM"))


# viii). USING REGULAR EXPRESSION

import re

s = "PyTHON Practice"
count = len(re.findall(r"[A-Z]", s))

print("Regex:", count)


# ix). USING map()

s = "Data SCIENCE"
count = sum(map(str.isupper, s))

print("map():", count)


# x). USING RECURSION

def count_uppercase_recursive(s):
    if not s:
        return 0

    return int(s[0].isupper()) + count_uppercase_recursive(s[1:])


print("Recursion:", count_uppercase_recursive("HeLLo WORld"))


# xi). FIND POSITIONS OF UPPERCASE LETTERS

s = "PyTHon PrACtice"
positions = []

for i in range(len(s)):
    if s[i].isupper():
        positions.append(i)

print("Uppercase positions:", positions)


# xii). STORE UPPERCASE LETTERS IN LIST

s = "OpenAI ChatGPT"
uppercase_letters = []

for ch in s:
    if ch.isupper():
        uppercase_letters.append(ch)

print("Uppercase letters:", uppercase_letters)
print("Uppercase letters count:", len(uppercase_letters))


# xiii). COUNT UPPERCASE IN EACH WORD

s = "My Name Is GAUTAM"
word_counts = {}

for word in s.split():
    word_counts[word] = sum(1 for ch in word if ch.isupper())

print("Each word:", word_counts)


# xiv). USING ASCII ORD VALUE

s = "ABC def XYZ"
count = 0

for ch in s:
    if 65 <= ord(ch) <= 90:
        count += 1

print("ord():", count)


# xv). COUNT UPPERCASE FROM LIST OF STRINGS

words = ["Python", "JAVA", "CodeGPT"]
count = 0

for word in words:
    count += sum(1 for ch in word if ch.isupper())

print("List of strings:", count)
