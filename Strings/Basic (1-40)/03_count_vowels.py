# =========================================================================================
#                              QUESTION 03: COUNT VOWELS
# =========================================================================================


VOWELS = "aeiou"


# i). USING FOR LOOP

s = "International"
count = 0

for ch in s:
    if ch.lower() in VOWELS:
        count += 1

print("For loop:", count)


# ii). USING WHILE LOOP

s = "Hello World"
count = 0
i = 0

while i < len(s):
    if s[i].lower() in VOWELS:
        count += 1
    i += 1

print("While loop:", count)


# iii). USING sum() + GENERATOR EXPRESSION

s = "Programming"
count = sum(1 for ch in s if ch.lower() in VOWELS)

print("sum() + generator:", count)


# iv). USING LIST COMPREHENSION

s = "coding"
count = len([ch for ch in s if ch.lower() in VOWELS])

print("List comprehension:", count)


# v). USING filter()

s = "Education"
count = len(list(filter(lambda ch: ch.lower() in VOWELS, s)))

print("filter():", count)


# vi). USING str.count()

s = "cooperation"
count = 0

for vowel in VOWELS:
    count += s.lower().count(vowel)

print("str.count():", count)


# vii). COUNT FREQUENCY OF EACH VOWEL USING DICTIONARY

s = "cooperation aeronautical"
vowel_count = {}

for ch in s:
    ch = ch.lower()
    if ch in VOWELS:
        vowel_count[ch] = vowel_count.get(ch, 0) + 1

print("Dictionary frequency:", vowel_count)


# viii). COUNT FREQUENCY USING collections.Counter

from collections import Counter

s = "beautiful education"
counter = Counter(ch for ch in s.lower() if ch in VOWELS)

print("Counter frequency:", counter)


# ix). USING REGULAR EXPRESSION

import re

s = "International"
count = len(re.findall(r"[aeiou]", s, re.IGNORECASE))

print("Regex:", count)


# x). USING RECURSION

def count_vowels_recursive(s):
    if not s:
        return 0

    return int(s[0].lower() in VOWELS) + count_vowels_recursive(s[1:])


print("Recursion:", count_vowels_recursive("frequency"))


# xi). USING A REUSABLE FUNCTION

def count_vowels(s):
    count = 0

    for ch in s:
        if ch.lower() in VOWELS:
            count += 1

    return count


print("Function:", count_vowels("Python Practice"))


# xii). COUNT VOWELS AND CONSONANTS TOGETHER

s = "International"
vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in VOWELS:
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# xiii). FIND POSITIONS OF VOWELS

s = "Education"
positions = []

for i in range(len(s)):
    if s[i].lower() in VOWELS:
        positions.append(i)

print("Vowel positions:", positions)


# xiv). STORE ALL VOWELS IN A LIST

s = "Data Science"
vowel_list = []

for ch in s:
    if ch.lower() in VOWELS:
        vowel_list.append(ch)

print("Vowel list:", vowel_list)
print("Vowel list count:", len(vowel_list))


# xv). COUNT VOWELS IN EACH WORD

s = "Python data science"
word_counts = {}

for word in s.split():
    word_counts[word] = sum(1 for ch in word if ch.lower() in VOWELS)

print("Each word:", word_counts)


# xvi). COUNT VOWELS FROM A LIST OF STRINGS

words = ["python", "pandas", "numpy"]
total = 0

for word in words:
    total += sum(1 for ch in word if ch.lower() in VOWELS)

print("List of strings total:", total)
