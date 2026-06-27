# =========================================================================================
#                              QUESTION 18: LAST REPEATING CHARACTER
# =========================================================================================


# i). USING DICTIONARY

s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in reversed(s):
    if freq[ch] > 1:
        print("Dictionary:", ch)
        break


# ii). USING count()

s = "banana"

for ch in reversed(s):
    if s.count(ch) > 1:
        print("count():", ch)
        break


# iii). USING SET

s = "mississippi"
seen = set()
last = None

for ch in s:
    if ch in seen:
        last = ch
    else:
        seen.add(ch)

print("Set:", last)


# iv). USING Counter

from collections import Counter

s = "committee"
counter = Counter(s)

for ch in reversed(s):
    if counter[ch] > 1:
        print("Counter:", ch)
        break


# v). USING FUNCTION

def last_repeating_character(s):
    for ch in reversed(s):
        if s.count(ch) > 1:
            return ch

    return None


print("Function:", last_repeating_character("success"))


# vi). USING INDEX LOOP FROM RIGHT

s = "programming"
answer = None

for i in range(len(s) - 1, -1, -1):
    if s.count(s[i]) > 1:
        answer = s[i]
        break

print("Right index loop:", answer)


# vii). CASE-INSENSITIVE LAST REPEATING

s = "AbcaD"
clean = s.lower()
answer = None

for i in range(len(s) - 1, -1, -1):
    if clean.count(clean[i]) > 1:
        answer = s[i]
        break

print("Case-insensitive:", answer)


# viii). LAST REPEATING CHARACTER WITH INDEX

s = "programming"
answer = None

for i in range(len(s) - 1, -1, -1):
    if s.count(s[i]) > 1:
        answer = (s[i], i)
        break

print("Character with index:", answer)


# ix). ALL REPEATING CHARACTERS IN REVERSE ORDER

s = "mississippi"
chars = []

for ch in reversed(s):
    if s.count(ch) > 1 and ch not in chars:
        chars.append(ch)

print("Reverse repeating list:", chars)


# x). LAST REPEATING IN EACH WORD

s = "hello apple code"
answers = {}

for word in s.split():
    answers[word] = last_repeating_character(word)

print("Each word:", answers)
