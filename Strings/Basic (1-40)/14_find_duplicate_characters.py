# =========================================================================================
#                              QUESTION 14: FIND DUPLICATE CHARACTERS
# =========================================================================================


# i). USING DICTIONARY

s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

duplicates = [ch for ch, count in freq.items() if count > 1]
print("Dictionary:", duplicates)


# ii). USING set() AND count()

s = "banana"
duplicates = []

for ch in set(s):
    if s.count(ch) > 1:
        duplicates.append(ch)

print("set() + count():", duplicates)


# iii). USING TWO SETS

s = "mississippi"
seen = set()
duplicates = set()

for ch in s:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)

print("Two sets:", duplicates)


# iv). USING Counter

from collections import Counter

s = "committee"
counter = Counter(s)
duplicates = [ch for ch, count in counter.items() if count > 1]

print("Counter:", duplicates)


# v). USING FUNCTION

def find_duplicates(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return [ch for ch in freq if freq[ch] > 1]


print("Function:", find_duplicates("success"))


# vi). PRESERVE DUPLICATE ORDER

s = "programming"
seen = set()
duplicates = []

for ch in s:
    if ch in seen and ch not in duplicates:
        duplicates.append(ch)
    else:
        seen.add(ch)

print("Preserve order:", duplicates)


# vii). USING LIST COMPREHENSION

s = "banana"
duplicates = [ch for ch in dict.fromkeys(s) if s.count(ch) > 1]

print("List comprehension:", duplicates)


# viii). CASE-INSENSITIVE DUPLICATES

s = "Application"
clean = s.lower()
duplicates = [ch for ch in dict.fromkeys(clean) if clean.count(ch) > 1]

print("Case-insensitive:", duplicates)


# ix). DUPLICATES WITH FREQUENCY

s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

duplicates = {ch: count for ch, count in freq.items() if count > 1}

print("Duplicates with frequency:", duplicates)


# x). DUPLICATE POSITIONS

s = "banana"
positions = {}

for i in range(len(s)):
    if s.count(s[i]) > 1:
        positions.setdefault(s[i], []).append(i)

print("Duplicate positions:", positions)


# xi). DUPLICATES IGNORING SPACES

s = "hello world"
clean = s.replace(" ", "")
duplicates = [ch for ch in dict.fromkeys(clean) if clean.count(ch) > 1]

print("Ignore spaces:", duplicates)
