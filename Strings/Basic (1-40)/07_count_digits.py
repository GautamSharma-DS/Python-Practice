# =========================================================================================
#                              QUESTION 07: COUNT DIGITS
# =========================================================================================


# i). USING FOR LOOP

s = "abc123def45"
count = 0

for ch in s:
    if ch.isdigit():
        count += 1

print("For loop:", count)


# ii). USING WHILE LOOP

s = "Room No 404"
count = 0
i = 0

while i < len(s):
    if s[i].isdigit():
        count += 1
    i += 1

print("While loop:", count)


# iii). USING sum()

s = "a1b2c3d4"
count = sum(1 for ch in s if ch.isdigit())

print("sum():", count)


# iv). USING LIST COMPREHENSION

s = "Year 2026"
digits = [ch for ch in s if ch.isdigit()]

print("List comprehension:", len(digits))


# v). USING filter()

s = "Mobile 98765"
count = len(list(filter(str.isdigit, s)))

print("filter():", count)


# vi). WITHOUT isdigit()

s = "pin 1234"
count = 0

for ch in s:
    if "0" <= ch <= "9":
        count += 1

print("Without isdigit():", count)


# vii). USING REGULAR EXPRESSION

import re

s = "ID: A102B55"
count = len(re.findall(r"\d", s))

print("Regex:", count)


# viii). USING map()

s = "A1B2C3"
count = sum(map(str.isdigit, s))

print("map():", count)


# ix). USING RECURSION

def count_digits_recursive(s):
    if not s:
        return 0

    return int(s[0].isdigit()) + count_digits_recursive(s[1:])


print("Recursion:", count_digits_recursive("Room 101"))


# x). EXTRACT DIGITS AND THEN COUNT

s = "order56id78"
digits = "".join(ch for ch in s if ch.isdigit())

print("Extract then count:", len(digits))


# xi). FIND POSITIONS OF DIGITS

s = "A1B22C333"
positions = []

for i in range(len(s)):
    if s[i].isdigit():
        positions.append(i)

print("Digit positions:", positions)


# xii). STORE DIGITS IN LIST

s = "Order 45 and 67"
digits = []

for ch in s:
    if ch.isdigit():
        digits.append(ch)

print("Digit list:", digits)
print("Digit list count:", len(digits))


# xiii). COUNT DIGITS IN EACH WORD

s = "A12 B3 C456"
word_counts = {}

for word in s.split():
    word_counts[word] = sum(1 for ch in word if ch.isdigit())

print("Each word:", word_counts)


# xiv). USING ASCII ORD VALUE

s = "pin 9087"
count = 0

for ch in s:
    if 48 <= ord(ch) <= 57:
        count += 1

print("ord():", count)


# xv). COUNT DIGITS FROM LIST OF STRINGS

items = ["a1", "b22", "333c"]
count = 0

for item in items:
    count += sum(1 for ch in item if ch.isdigit())

print("List of strings:", count)
