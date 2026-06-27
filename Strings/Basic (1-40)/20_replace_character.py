# =========================================================================================
#                              QUESTION 20: REPLACE CHARACTER
# =========================================================================================


# i). USING replace()

s = "banana"
result = s.replace("a", "o")

print("replace():", result)


# ii). USING FOR LOOP

s = "hello"
old = "l"
new = "x"
result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("For loop:", result)


# iii). USING LIST CONVERSION

s = "python"
lst = list(s)
lst[0] = "P"
result = "".join(lst)

print("List conversion:", result)


# iv). REPLACE FIRST OCCURRENCE ONLY

s = "banana"
result = s.replace("a", "o", 1)

print("First occurrence:", result)


# v). USING translate()

s = "hello"
table = str.maketrans({"h": "H", "o": "0"})

print("translate():", s.translate(table))


# vi). USING FUNCTION

def replace_character(s, old, new):
    result = ""

    for ch in s:
        result += new if ch == old else ch

    return result


print("Function:", replace_character("mississippi", "s", "$"))


# vii). USING REGULAR EXPRESSION

import re

s = "banana"
result = re.sub("a", "o", s)

print("Regex:", result)


# viii). REPLACE USING INDEX POSITION

s = "python"
index = 2
new = "X"
result = s[:index] + new + s[index + 1:]

print("Index replace:", result)


# ix). REPLACE MULTIPLE CHARACTERS USING DICTIONARY

s = "hello world"
replace_map = {"h": "H", "o": "0", "l": "1"}
result = ""

for ch in s:
    result += replace_map.get(ch, ch)

print("Dictionary replace:", result)


# x). REPLACE ONLY LAST OCCURRENCE

s = "banana"
old = "a"
new = "o"
index = s.rfind(old)

if index != -1:
    result = s[:index] + new + s[index + 1:]
else:
    result = s

print("Last occurrence:", result)


# xi). REPLACE CHARACTER AT MULTIPLE INDEXES

s = "python"
indexes = [1, 3]
new = "*"
result = ""

for i in range(len(s)):
    if i in indexes:
        result += new
    else:
        result += s[i]

print("Multiple indexes:", result)


# xii). CASE-INSENSITIVE REPLACE

s = "Application"
old = "a"
new = "@"
result = ""

for ch in s:
    if ch.lower() == old.lower():
        result += new
    else:
        result += ch

print("Case-insensitive:", result)
