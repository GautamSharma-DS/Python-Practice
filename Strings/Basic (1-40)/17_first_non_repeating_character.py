# =========================================================================================
#                              QUESTION 17: FIRST NON-REPEATING CHARACTER
# =========================================================================================


# i). USING DICTIONARY

s = "swiss"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print("Dictionary:", ch)
        break


# ii). USING count()

s = "programming"

for ch in s:
    if s.count(ch) == 1:
        print("count():", ch)
        break


# iii). USING Counter

from collections import Counter

s = "aabbcddee"
counter = Counter(s)

for ch in s:
    if counter[ch] == 1:
        print("Counter:", ch)
        break


# iv). USING NESTED LOOP

s = "leetcode"

for i in range(len(s)):
    repeating = False
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            repeating = True
            break
    if not repeating:
        print("Nested loop:", s[i])
        break


# v). USING FUNCTION

def first_non_repeating_character(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch

    return None


print("Function:", first_non_repeating_character("success"))


# vi). USING INDEX AND rfind()

s = "swiss"
answer = None

for ch in s:
    if s.find(ch) == s.rfind(ch):
        answer = ch
        break

print("find() + rfind():", answer)


# vii). CASE-INSENSITIVE FIRST NON-REPEATING

s = "aAbBc"
clean = s.lower()
answer = None

for i in range(len(s)):
    if clean.count(clean[i]) == 1:
        answer = s[i]
        break

print("Case-insensitive:", answer)


# viii). FIRST NON-REPEATING CHARACTER WITH INDEX

s = "swiss"
answer = None

for i in range(len(s)):
    if s.count(s[i]) == 1:
        answer = (s[i], i)
        break

print("Character with index:", answer)


# ix). ALL NON-REPEATING CHARACTERS

s = "programming"
chars = []

for ch in s:
    if s.count(ch) == 1:
        chars.append(ch)

print("All non-repeating:", chars)


# x). FIRST NON-REPEATING IN EACH WORD

s = "hello apple code"
answers = {}

for word in s.split():
    answers[word] = first_non_repeating_character(word)

print("Each word:", answers)
