# =========================================================================================
#                              QUESTION 28: CONTAINS ONLY DIGITS
# =========================================================================================


# i). USING isdigit()

s = "12345"
print("isdigit():", s.isdigit())


# ii). USING isnumeric()

s = "98765"
print("isnumeric():", s.isnumeric())


# iii). USING FOR LOOP

s = "123a45"
only_digits = True

for ch in s:
    if not ch.isdigit():
        only_digits = False
        break

print("For loop:", only_digits)


# iv). WITHOUT isdigit()

s = "12345"
only_digits = True

for ch in s:
    if not ("0" <= ch <= "9"):
        only_digits = False
        break

print("Without isdigit():", only_digits)


# v). USING all()

s = "2026"
print("all():", all(ch.isdigit() for ch in s))


# vi). USING REGULAR EXPRESSION

import re

s = "456789"
print("Regex:", bool(re.fullmatch(r"\d+", s)))


# vii). USING try-except int()

s = "12345"

try:
    int(s)
    only_digits = True
except ValueError:
    only_digits = False

print("try-except:", only_digits)


# viii). USING set()

s = "908172"
digits = set("0123456789")

print("set():", set(s).issubset(digits) and s != "")


# ix). USING RECURSION

def only_digits_recursive(s):
    if not s:
        return True

    return s[0].isdigit() and only_digits_recursive(s[1:])


print("Recursion:", only_digits_recursive("2026"))


# x). CHECK DIGITS AFTER REMOVING SPACES

s = "123 456"
clean = s.replace(" ", "")

print("Ignore spaces:", clean.isdigit())


# xi). CHECK DIGITS WITH OPTIONAL SIGN

s = "-12345"
clean = s[1:] if s.startswith(("+", "-")) else s

print("Optional sign:", clean.isdigit())


# xii). CHECK LIST OF STRINGS

items = ["123", "45a", "678"]
answers = []

for item in items:
    answers.append(item.isdigit())

print("List of strings:", answers)
