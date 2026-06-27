# =========================================================================================
#                              QUESTION 19: LAST NON-REPEATING CHARACTER
# =========================================================================================


# i). USING DICTIONARY

s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in reversed(s):
    if freq[ch] == 1:
        print("Dictionary:", ch)
        break


# ii). USING count()

s = "swiss"

for ch in reversed(s):
    if s.count(ch) == 1:
        print("count():", ch)
        break


# iii). USING Counter

from collections import Counter

s = "aabbcddee"
counter = Counter(s)

for ch in reversed(s):
    if counter[ch] == 1:
        print("Counter:", ch)
        break


# iv). USING INDEX LOOP

s = "leetcode"

for i in range(len(s) - 1, -1, -1):
    if s.count(s[i]) == 1:
        print("Index loop:", s[i])
        break


# v). USING FUNCTION

def last_non_repeating_character(s):
    for ch in reversed(s):
        if s.count(ch) == 1:
            return ch

    return None


print("Function:", last_non_repeating_character("success"))


# vi). USING find() AND rfind()

s = "programming"
answer = None

for ch in reversed(s):
    if s.find(ch) == s.rfind(ch):
        answer = ch
        break

print("find() + rfind():", answer)


# vii). CASE-INSENSITIVE LAST NON-REPEATING

s = "aAbBcD"
clean = s.lower()
answer = None

for i in range(len(s) - 1, -1, -1):
    if clean.count(clean[i]) == 1:
        answer = s[i]
        break

print("Case-insensitive:", answer)


# viii). LAST NON-REPEATING CHARACTER WITH INDEX

s = "programming"
answer = None

for i in range(len(s) - 1, -1, -1):
    if s.count(s[i]) == 1:
        answer = (s[i], i)
        break

print("Character with index:", answer)


# ix). ALL NON-REPEATING CHARACTERS IN REVERSE ORDER

s = "programming"
chars = []

for ch in reversed(s):
    if s.count(ch) == 1:
        chars.append(ch)

print("Reverse non-repeating list:", chars)


# x). LAST NON-REPEATING IN EACH WORD

s = "hello apple code"
answers = {}

for word in s.split():
    answers[word] = last_non_repeating_character(word)

print("Each word:", answers)
