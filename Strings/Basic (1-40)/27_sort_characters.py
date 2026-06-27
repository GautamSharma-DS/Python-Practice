# =========================================================================================
#                              QUESTION 27: SORT CHARACTERS
# =========================================================================================


# i). USING sorted()

s = "python"
result = "".join(sorted(s))

print("sorted():", result)


# ii). REVERSE SORT

s = "python"
result = "".join(sorted(s, reverse=True))

print("Reverse sort:", result)


# iii). CASE-INSENSITIVE SORT

s = "bAcD"
result = "".join(sorted(s, key=str.lower))

print("Case-insensitive:", result)


# iv). USING LIST sort()

s = "program"
lst = list(s)
lst.sort()

print("list.sort():", "".join(lst))


# v). WITHOUT sorted() USING BUBBLE SORT

s = "code"
lst = list(s)

for i in range(len(lst)):
    for j in range(0, len(lst) - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Bubble sort:", "".join(lst))


# vi). SORT ONLY LETTERS CASE-INSENSITIVE

s = "BcaA"
result = "".join(sorted(s, key=lambda ch: ch.lower()))

print("lambda key:", result)


# vii). SORT USING ASCII VALUE

s = "dbca"
result = "".join(sorted(s, key=ord))

print("ord():", result)


# viii). COUNTING SORT FOR LOWERCASE LETTERS

s = "banana"
count = [0] * 26

for ch in s:
    count[ord(ch) - ord("a")] += 1

result = ""

for i in range(26):
    result += chr(i + ord("a")) * count[i]

print("Counting sort:", result)


# ix). SORT ONLY ALPHABETS AND KEEP DIGITS SEPARATE

s = "b2a1c3"
letters = sorted(ch for ch in s if ch.isalpha())
digits = sorted(ch for ch in s if ch.isdigit())

print("Letters then digits:", "".join(letters + digits))


# x). SORT CHARACTERS IGNORING SPACES

s = "b a c"
result = "".join(sorted(ch for ch in s if ch != " "))

print("Ignore spaces:", result)


# xi). SORT EACH WORD

s = "python code"
result = " ".join("".join(sorted(word)) for word in s.split())

print("Each word:", result)
