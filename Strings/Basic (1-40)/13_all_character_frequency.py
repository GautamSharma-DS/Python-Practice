# =========================================================================================
#                              QUESTION 13: ALL CHARACTER FREQUENCY
# =========================================================================================


# i). USING DICTIONARY

s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Dictionary:", freq)


# ii). USING collections.Counter

from collections import Counter

s = "mississippi"
freq = Counter(s)

print("Counter:", freq)


# iii). WITHOUT get()

s = "programming"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Without get():", freq)


# iv). CASE-INSENSITIVE FREQUENCY

s = "Application"
freq = {}

for ch in s.lower():
    freq[ch] = freq.get(ch, 0) + 1

print("Case-insensitive:", freq)


# v). USING FUNCTION

def all_character_frequency(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq


print("Function:", all_character_frequency("hello"))


# vi). USING set() AND count()

s = "banana"
freq = {}

for ch in set(s):
    freq[ch] = s.count(ch)

print("set() + count():", freq)


# vii). USING defaultdict

from collections import defaultdict

s = "committee"
freq = defaultdict(int)

for ch in s:
    freq[ch] += 1

print("defaultdict:", dict(freq))


# viii). USING RECURSION

def frequency_recursive(s, freq=None):
    if freq is None:
        freq = {}

    if not s:
        return freq

    freq[s[0]] = freq.get(s[0], 0) + 1
    return frequency_recursive(s[1:], freq)


print("Recursion:", frequency_recursive("hello"))


# ix). IGNORE SPACES WHILE COUNTING

s = "hello world"
freq = {}

for ch in s:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

print("Ignore spaces:", freq)


# x). FREQUENCY OF ONLY ALPHABETS

s = "abc123abc!"
freq = {}

for ch in s:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

print("Only alphabets:", freq)


# xi). SORT FREQUENCY BY CHARACTER

s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Sorted by character:", dict(sorted(freq.items())))


# xii). SORT FREQUENCY BY COUNT

s = "mississippi"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Sorted by count:", dict(sorted(freq.items(), key=lambda item: item[1], reverse=True)))
