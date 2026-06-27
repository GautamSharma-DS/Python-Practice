# =========================================================================================
#                              QUESTION 04: COUNT CONSONANTS
# =========================================================================================


VOWELS = "aeiou"


# i). USING FOR LOOP

s = "Hello World"
count = 0

for ch in s:
    if ch.isalpha() and ch.lower() not in VOWELS:
        count += 1

print("For loop:", count)


# ii). USING WHILE LOOP

s = "International"
count = 0
i = 0

while i < len(s):
    if s[i].isalpha() and s[i].lower() not in VOWELS:
        count += 1
    i += 1

print("While loop:", count)


# iii). USING sum() + GENERATOR EXPRESSION

s = "Python Practice"
count = sum(1 for ch in s if ch.isalpha() and ch.lower() not in VOWELS)

print("sum() + generator:", count)


# iv). USING LIST COMPREHENSION

s = "Programming"
count = len([ch for ch in s if ch.isalpha() and ch.lower() not in VOWELS])

print("List comprehension:", count)


# v). USING filter()

s = "Education"
count = len(list(filter(lambda ch: ch.isalpha() and ch.lower() not in VOWELS, s)))

print("filter():", count)


# vi). USING map()

s = "Data Structures"
count = sum(map(lambda ch: ch.isalpha() and ch.lower() not in VOWELS, s))

print("map():", count)


# vii). USING REGULAR EXPRESSION

import re

s = "Python Practice 123"
consonants = re.findall(r"[bcdfghjklmnpqrstvwxyz]", s, re.IGNORECASE)

print("Regex:", len(consonants))


# viii). USING DICTIONARY FREQUENCY

s = "Better programming"
freq = {}

for ch in s.lower():
    if ch.isalpha() and ch not in VOWELS:
        freq[ch] = freq.get(ch, 0) + 1

print("Dictionary frequency:", freq)


# ix). USING collections.Counter

from collections import Counter

s = "Communication"
counter = Counter(ch for ch in s.lower() if ch.isalpha() and ch not in VOWELS)

print("Counter:", counter)
print("Counter total:", sum(counter.values()))


# x). USING set()

s = "Python Programming"
consonant_set = set("bcdfghjklmnpqrstvwxyz")
count = 0

for ch in s.lower():
    if ch in consonant_set:
        count += 1

print("set():", count)


# xi). COUNT ONLY UNIQUE CONSONANTS

s = "Communication"
unique_consonants = set()

for ch in s.lower():
    if ch.isalpha() and ch not in VOWELS:
        unique_consonants.add(ch)

print("Unique consonants:", len(unique_consonants), unique_consonants)


# xii). USING translate()

import string

s = "Hello World 123!"
remove_chars = VOWELS + VOWELS.upper() + string.digits + string.punctuation + " "
only_consonants = s.translate(str.maketrans("", "", remove_chars))

print("translate():", len(only_consonants))


# xiii). COUNT CONSONANTS IN EACH WORD

s = "Python is very easy"
word_counts = {}

for word in s.split():
    word_counts[word] = sum(1 for ch in word if ch.isalpha() and ch.lower() not in VOWELS)

print("Each word:", word_counts)


# xiv). USING RECURSION

def count_consonants_recursive(s):
    if not s:
        return 0

    first = int(s[0].isalpha() and s[0].lower() not in VOWELS)
    return first + count_consonants_recursive(s[1:])


print("Recursion:", count_consonants_recursive("Hello World"))


# xv). USING FUNCTION

def count_consonants(s):
    count = 0

    for ch in s.lower():
        if ch.isalpha() and ch not in VOWELS:
            count += 1

    return count


print("Function:", count_consonants("Hello World"))


# xvi). TOTAL ALPHABETS - TOTAL VOWELS

s = "International"
alphabet_count = 0
vowel_count = 0

for ch in s:
    if ch.isalpha():
        alphabet_count += 1
        if ch.lower() in VOWELS:
            vowel_count += 1

consonant_count = alphabet_count - vowel_count

print("Alphabets - vowels:", consonant_count)


# xvii). WITHOUT isalpha() USING ASCII RANGE

s = "Hello World 123"
count = 0

for ch in s:
    lower_ch = ch.lower()
    if "a" <= lower_ch <= "z" and lower_ch not in VOWELS:
        count += 1

print("ASCII range:", count)


# xviii). COUNT UPPERCASE AND LOWERCASE CONSONANTS SEPARATELY

s = "PyTHON Practice"
uppercase_consonants = 0
lowercase_consonants = 0

for ch in s:
    if ch.isalpha() and ch.lower() not in VOWELS:
        if ch.isupper():
            uppercase_consonants += 1
        else:
            lowercase_consonants += 1

print("Uppercase consonants:", uppercase_consonants)
print("Lowercase consonants:", lowercase_consonants)


# xix). FIND POSITIONS OF CONSONANTS

s = "Education"
positions = []

for i in range(len(s)):
    if s[i].isalpha() and s[i].lower() not in VOWELS:
        positions.append(i)

print("Consonant positions:", positions)


# xx). STORE ALL CONSONANTS IN A LIST

s = "String Practice"
consonants = []

for ch in s:
    if ch.isalpha() and ch.lower() not in VOWELS:
        consonants.append(ch)

print("Consonant list:", consonants)
print("Consonant list count:", len(consonants))


# xxi). COUNT CONSONANTS FROM A LIST OF STRINGS

words = ["Python", "Java", "Code"]
total = 0

for word in words:
    for ch in word:
        if ch.isalpha() and ch.lower() not in VOWELS:
            total += 1

print("List of strings total:", total)


# xxii). COUNT CONSONANTS IN EACH LINE

text = """Python is easy
Practice daily
Learn strings"""

line_counts = []

for line in text.splitlines():
    count = 0
    for ch in line:
        if ch.isalpha() and ch.lower() not in VOWELS:
            count += 1
    line_counts.append(count)

print("Each line:", line_counts)
