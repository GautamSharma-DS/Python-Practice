# =========================================================================================
#                              QUESTION 40: SMALLEST OCCURRING CHARACTER
# =========================================================================================


# i). CHARACTER WITH MIN FREQUENCY USING DICTIONARY

s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

smallest = min(freq, key=freq.get)
print("Dictionary:", smallest, freq[smallest])


# ii). USING Counter

from collections import Counter

s = "mississippi"
counter = Counter(s)
smallest = min(counter, key=counter.get)

print("Counter:", smallest, counter[smallest])


# iii). USING count()

s = "banana"
smallest = ""
min_count = len(s)

for ch in set(s):
    count = s.count(ch)
    if count < min_count:
        min_count = count
        smallest = ch

print("count():", smallest, min_count)


# iv). LEXICOGRAPHICALLY SMALLEST CHARACTER

s = "python"
smallest = min(s)

print("Lexicographically smallest:", smallest)


# v). USING FUNCTION

def smallest_occurring_character(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return min(freq, key=freq.get)


print("Function:", smallest_occurring_character("success"))


# vi). SMALLEST FREQUENCY WITH TIE BY LEXICOGRAPHIC ORDER

s = "aabbccd"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

smallest = min(freq, key=lambda ch: (freq[ch], ch))

print("Frequency + lexicographic tie:", smallest, freq[smallest])


# vii). USING SORTED FREQUENCY ITEMS

s = "mississippi"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

items = sorted(freq.items(), key=lambda item: item[1])

print("Sorted items:", items[0])


# viii). IGNORE SPACES

s = "hello world"
clean = s.replace(" ", "")
freq = {}

for ch in clean:
    freq[ch] = freq.get(ch, 0) + 1

smallest = min(freq, key=freq.get)

print("Ignore spaces:", smallest, freq[smallest])


# ix). ALL CHARACTERS WITH MIN FREQUENCY

s = "aabbccdde"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

min_count = min(freq.values())
chars = [ch for ch, count in freq.items() if count == min_count]

print("All min frequency:", chars, min_count)


# x). SMALLEST OCCURRING ALPHABET ONLY

s = "a1b22bbb!!!"
freq = {}

for ch in s:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

smallest = min(freq, key=freq.get)

print("Alphabet only:", smallest, freq[smallest])


# xi). SMALLEST OCCURRING IN EACH WORD

s = "hello banana"
answers = {}

for word in s.split():
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    smallest = min(freq, key=freq.get)
    answers[word] = (smallest, freq[smallest])

print("Each word:", answers)
