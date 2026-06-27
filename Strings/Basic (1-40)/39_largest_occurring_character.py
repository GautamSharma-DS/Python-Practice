# =========================================================================================
#                              QUESTION 39: LARGEST OCCURRING CHARACTER
# =========================================================================================


# i). CHARACTER WITH MAX FREQUENCY USING DICTIONARY

s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

largest = max(freq, key=freq.get)
print("Dictionary:", largest, freq[largest])


# ii). USING Counter

from collections import Counter

s = "mississippi"
counter = Counter(s)
largest = counter.most_common(1)[0]

print("Counter:", largest)


# iii). USING count()

s = "banana"
largest = ""
max_count = 0

for ch in set(s):
    count = s.count(ch)
    if count > max_count:
        max_count = count
        largest = ch

print("count():", largest, max_count)


# iv). LEXICOGRAPHICALLY LARGEST CHARACTER

s = "python"
largest = max(s)

print("Lexicographically largest:", largest)


# v). USING FUNCTION

def largest_occurring_character(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return max(freq, key=freq.get)


print("Function:", largest_occurring_character("success"))


# vi). LARGEST FREQUENCY WITH TIE BY LEXICOGRAPHIC ORDER

s = "aabbccdde"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

largest = max(freq, key=lambda ch: (freq[ch], ch))

print("Frequency + lexicographic tie:", largest, freq[largest])


# vii). USING SORTED FREQUENCY ITEMS

s = "mississippi"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

print("Sorted items:", items[0])


# viii). IGNORE SPACES

s = "hello world"
clean = s.replace(" ", "")
freq = {}

for ch in clean:
    freq[ch] = freq.get(ch, 0) + 1

largest = max(freq, key=freq.get)

print("Ignore spaces:", largest, freq[largest])


# ix). ALL CHARACTERS WITH MAX FREQUENCY

s = "aabbccdde"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

max_count = max(freq.values())
chars = [ch for ch, count in freq.items() if count == max_count]

print("All max frequency:", chars, max_count)


# x). LARGEST OCCURRING ALPHABET ONLY

s = "a1b22bbb!!!"
freq = {}

for ch in s:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

largest = max(freq, key=freq.get)

print("Alphabet only:", largest, freq[largest])


# xi). LARGEST OCCURRING IN EACH WORD

s = "hello banana"
answers = {}

for word in s.split():
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    largest = max(freq, key=freq.get)
    answers[word] = (largest, freq[largest])

print("Each word:", answers)
