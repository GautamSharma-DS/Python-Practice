# =========================================================================================
#                              QUESTION 15: REMOVE DUPLICATE CHARACTERS
# =========================================================================================


# i). PRESERVE ORDER USING set()

s = "programming"
seen = set()
result = ""

for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)

print("Preserve order:", result)


# ii). USING DICTIONARY KEYS

s = "banana"
result = "".join(dict.fromkeys(s))

print("dict.fromkeys():", result)


# iii). USING FOR LOOP AND in

s = "mississippi"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("For loop:", result)


# iv). SORTED UNIQUE CHARACTERS

s = "programming"
result = "".join(sorted(set(s)))

print("Sorted unique:", result)


# v). USING FUNCTION

def remove_duplicates(s):
    result = ""

    for ch in s:
        if ch not in result:
            result += ch

    return result


print("Function:", remove_duplicates("success"))


# vi). CASE-INSENSITIVE REMOVE DUPLICATES

s = "AppLe"
seen = set()
result = ""

for ch in s:
    key = ch.lower()
    if key not in seen:
        result += ch
        seen.add(key)

print("Case-insensitive:", result)


# vii). USING OrderedDict

from collections import OrderedDict

s = "character"
result = "".join(OrderedDict.fromkeys(s))

print("OrderedDict:", result)


# viii). USING RECURSION

def remove_duplicates_recursive(s, result=""):
    if not s:
        return result

    if s[0] not in result:
        result += s[0]

    return remove_duplicates_recursive(s[1:], result)


print("Recursion:", remove_duplicates_recursive("banana"))


# ix). REMOVE DUPLICATES IGNORING SPACES

s = "hello world"
result = ""

for ch in s:
    if ch == " " or ch not in result:
        result += ch

print("Keep spaces:", result)


# x). KEEP ONLY CHARACTERS THAT APPEAR ONCE

s = "programming"
result = ""

for ch in s:
    if s.count(ch) == 1:
        result += ch

print("Only non-duplicates:", result)


# xi). REMOVE DUPLICATES FROM EACH WORD

s = "hello programming"
result_words = []

for word in s.split():
    result_words.append("".join(dict.fromkeys(word)))

print("Each word:", " ".join(result_words))
