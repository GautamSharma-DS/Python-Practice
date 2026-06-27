# =========================================================================================
#                              QUESTION 38: PRINT ALL SUBSTRINGS
# =========================================================================================


# i). USING NESTED LOOP

s = "abc"

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print("Nested loop:", s[i:j])


# ii). STORE IN LIST

s = "abcd"
substrings = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[i:j])

print("List:", substrings)


# iii). USING LIST COMPREHENSION

s = "abc"
substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

print("List comprehension:", substrings)


# iv). SUBSTRINGS OF FIXED LENGTH

s = "python"
k = 3
substrings = []

for i in range(len(s) - k + 1):
    substrings.append(s[i:i + k])

print("Fixed length:", substrings)


# v). USING FUNCTION

def all_substrings(s):
    result = []

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            result.append(s[i:j])

    return result


print("Function:", all_substrings("ab"))


# vi). USING WHILE LOOPS

s = "abc"
i = 0
substrings = []

while i < len(s):
    j = i + 1
    while j <= len(s):
        substrings.append(s[i:j])
        j += 1
    i += 1

print("While loops:", substrings)


# vii). UNIQUE SUBSTRINGS

s = "aba"
substrings = set()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.add(s[i:j])

print("Unique:", substrings)


# viii). USING RECURSION

def substrings_from_index(s, start=0):
    if start == len(s):
        return []

    current = [s[start:end] for end in range(start + 1, len(s) + 1)]
    return current + substrings_from_index(s, start + 1)


print("Recursion:", substrings_from_index("abc"))


# ix). COUNT TOTAL SUBSTRINGS

s = "abcd"
total = len(s) * (len(s) + 1) // 2

print("Total substrings:", total)


# x). SUBSTRINGS GROUPED BY LENGTH

s = "abcd"
groups = {}

for length in range(1, len(s) + 1):
    groups[length] = []
    for i in range(len(s) - length + 1):
        groups[length].append(s[i:i + length])

print("Grouped by length:", groups)


# xi). PALINDROMIC SUBSTRINGS

s = "ababa"
palindromes = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if sub == sub[::-1]:
            palindromes.append(sub)

print("Palindromic substrings:", palindromes)
