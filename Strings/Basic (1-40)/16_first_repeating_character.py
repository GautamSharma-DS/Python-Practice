# =========================================================================================
#                              QUESTION 16: FIRST REPEATING CHARACTER
# =========================================================================================


# i). USING SET

s = "programming"
seen = set()

for ch in s:
    if ch in seen:
        print("Set:", ch)
        break
    seen.add(ch)


# ii). USING DICTIONARY FREQUENCY

s = "swiss"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] > 1:
        print("Dictionary:", ch)
        break


# iii). USING count()

s = "banana"

for ch in s:
    if s.count(ch) > 1:
        print("count():", ch)
        break


# iv). USING NESTED LOOP

s = "abcdefda"
found = None

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            found = s[i]
            break
    if found:
        break

print("Nested loop:", found)


# v). USING FUNCTION

def first_repeating_character(s):
    seen = set()

    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)

    return None


print("Function:", first_repeating_character("hello"))


# vi). USING INDEX AND rfind()

s = "abca"
answer = None

for ch in s:
    if s.find(ch) != s.rfind(ch):
        answer = ch
        break

print("find() + rfind():", answer)


# vii). CASE-INSENSITIVE FIRST REPEATING

s = "Abca"
seen = set()
answer = None

for ch in s:
    key = ch.lower()
    if key in seen:
        answer = ch
        break
    seen.add(key)

print("Case-insensitive:", answer)


# viii). FIRST REPEATING CHARACTER WITH INDEX

s = "programming"
seen = {}
answer = None

for i in range(len(s)):
    if s[i] in seen:
        answer = (s[i], i)
        break
    seen[s[i]] = i

print("Character with index:", answer)


# ix). FIRST CHARACTER WHOSE TOTAL FREQUENCY IS MORE THAN 1

s = "abcda"
answer = None

for ch in s:
    if s.count(ch) > 1:
        answer = ch
        break

print("Total frequency check:", answer)


# x). FIRST REPEATING IN EACH WORD

s = "hello apple code"
answers = {}

for word in s.split():
    answers[word] = first_repeating_character(word)

print("Each word:", answers)
