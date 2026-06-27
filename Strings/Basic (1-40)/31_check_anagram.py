# =========================================================================================
#                              QUESTION 31: CHECK ANAGRAM
# =========================================================================================


# i). USING sorted()

s1 = "listen"
s2 = "silent"

print("sorted():", sorted(s1) == sorted(s2))


# ii). USING DICTIONARY

s1 = "triangle"
s2 = "integral"
freq = {}

for ch in s1:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s2:
    freq[ch] = freq.get(ch, 0) - 1

print("Dictionary:", all(value == 0 for value in freq.values()))


# iii). USING Counter

from collections import Counter

s1 = "evil"
s2 = "vile"

print("Counter:", Counter(s1) == Counter(s2))


# iv). IGNORE CASE AND SPACES

s1 = "Dormitory"
s2 = "Dirty room"

a = s1.replace(" ", "").lower()
b = s2.replace(" ", "").lower()

print("Ignore case/spaces:", sorted(a) == sorted(b))


# v). USING FUNCTION

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


print("Function:", is_anagram("heart", "earth"))


# vi). USING CHARACTER COUNT ARRAY

s1 = "listen"
s2 = "silent"
count = [0] * 26

for ch in s1:
    count[ord(ch) - ord("a")] += 1

for ch in s2:
    count[ord(ch) - ord("a")] -= 1

print("Count array:", all(value == 0 for value in count))


# vii). ANAGRAM AFTER REMOVING PUNCTUATION

import re

s1 = "conversation!"
s2 = "voices rant on"

a = "".join(re.findall(r"[A-Za-z]", s1.lower()))
b = "".join(re.findall(r"[A-Za-z]", s2.lower()))

print("Ignore punctuation:", sorted(a) == sorted(b))


# viii). GROUP ANAGRAM WORDS

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)

print("Anagram groups:", list(groups.values()))


# ix). CHECK ANAGRAM WITHOUT SORTING USING DELETION

s1 = "heart"
s2 = "earth"
temp = list(s2)
is_anagram_value = True

for ch in s1:
    if ch in temp:
        temp.remove(ch)
    else:
        is_anagram_value = False
        break

print("Deletion method:", is_anagram_value and not temp)
