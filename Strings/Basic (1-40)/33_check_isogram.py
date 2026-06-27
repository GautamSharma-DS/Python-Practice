# =========================================================================================
#                              QUESTION 33: CHECK ISOGRAM
# =========================================================================================


# i). USING set()

s = "machine"
clean = s.replace(" ", "").lower()

print("set():", len(clean) == len(set(clean)))


# ii). USING FOR LOOP

s = "algorithm"
seen = set()
is_isogram = True

for ch in s.lower():
    if ch in seen:
        is_isogram = False
        break
    seen.add(ch)

print("For loop:", is_isogram)


# iii). USING count()

s = "python"
is_isogram = True

for ch in s:
    if s.count(ch) > 1:
        is_isogram = False
        break

print("count():", is_isogram)


# iv). IGNORE SPACES AND HYPHENS

s = "six-year-old"
clean = s.replace(" ", "").replace("-", "").lower()

print("Ignore spaces/hyphens:", len(clean) == len(set(clean)))


# v). USING FUNCTION

def is_isogram(s):
    clean = "".join(ch.lower() for ch in s if ch.isalpha())
    return len(clean) == len(set(clean))


print("Function:", is_isogram("background"))


# vi). USING DICTIONARY FREQUENCY

s = "subdermatoglyphic"
freq = {}
is_isogram_value = True

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
    if freq[ch] > 1:
        is_isogram_value = False
        break

print("Dictionary:", is_isogram_value)


# vii). USING Counter

from collections import Counter

s = "machine"
counter = Counter(s)

print("Counter:", all(value == 1 for value in counter.values()))


# viii). USING RECURSION

def is_isogram_recursive(s, seen=None):
    if seen is None:
        seen = set()

    if not s:
        return True

    if s[0] in seen:
        return False

    seen.add(s[0])
    return is_isogram_recursive(s[1:], seen)


print("Recursion:", is_isogram_recursive("python"))


# ix). FIND REPEATED LETTER IF NOT ISOGRAM

s = "programming"
seen = set()
repeated = None

for ch in s:
    if ch in seen:
        repeated = ch
        break
    seen.add(ch)

print("Repeated letter:", repeated)


# x). ISOGRAM IGNORING NON-ALPHABETS

s = "six-year old"
clean = "".join(ch.lower() for ch in s if ch.isalpha())

print("Ignore non-alphabets:", len(clean) == len(set(clean)))


# xi). CHECK LIST OF WORDS

words = ["machine", "hello", "python"]
answers = []

for word in words:
    answers.append(len(word) == len(set(word)))

print("List of words:", answers)
