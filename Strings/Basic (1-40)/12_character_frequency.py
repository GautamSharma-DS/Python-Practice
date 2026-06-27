# =========================================================================================
#                              QUESTION 12: CHARACTER FREQUENCY
# =========================================================================================


# i). FREQUENCY OF ONE CHARACTER USING count()

s = "banana"
ch = "a"

print("count():", s.count(ch))


# ii). FREQUENCY OF ONE CHARACTER USING FOR LOOP

s = "mississippi"
target = "s"
count = 0

for ch in s:
    if ch == target:
        count += 1

print("For loop:", count)


# iii). CASE-INSENSITIVE FREQUENCY

s = "Application"
target = "a"
count = s.lower().count(target.lower())

print("Case-insensitive:", count)


# iv). USING sum()

s = "programming"
target = "m"
count = sum(1 for ch in s if ch == target)

print("sum():", count)


# v). USING FUNCTION

def character_frequency(s, target):
    count = 0

    for ch in s:
        if ch == target:
            count += 1

    return count


print("Function:", character_frequency("committee", "t"))


# vi). USING filter()

s = "mississippi"
target = "i"
count = len(list(filter(lambda ch: ch == target, s)))

print("filter():", count)


# vii). USING Counter

from collections import Counter

s = "banana"
target = "n"
counter = Counter(s)

print("Counter:", counter[target])


# viii). USING RECURSION

def char_frequency_recursive(s, target):
    if not s:
        return 0

    return int(s[0] == target) + char_frequency_recursive(s[1:], target)


print("Recursion:", char_frequency_recursive("success", "s"))


# ix). FIND ALL POSITIONS OF TARGET CHARACTER

s = "mississippi"
target = "s"
positions = []

for i in range(len(s)):
    if s[i] == target:
        positions.append(i)

print("Target positions:", positions)


# x). CASE-INSENSITIVE POSITIONS

s = "Application"
target = "a"
positions = []

for i in range(len(s)):
    if s[i].lower() == target.lower():
        positions.append(i)

print("Case-insensitive positions:", positions)


# xi). FREQUENCY IN EACH WORD

s = "banana bandana"
target = "a"
word_counts = {}

for word in s.split():
    word_counts[word] = word.count(target)

print("Each word:", word_counts)
