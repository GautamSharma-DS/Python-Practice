# =========================================================================================
#                              QUESTION 34: STRING ROTATION
# =========================================================================================


# i). USING CONCATENATION

s1 = "abcd"
s2 = "cdab"

print("Concatenation:", len(s1) == len(s2) and s2 in s1 + s1)


# ii). LEFT ROTATION

s = "abcdef"
k = 2
result = s[k:] + s[:k]

print("Left rotation:", result)


# iii). RIGHT ROTATION

s = "abcdef"
k = 2
result = s[-k:] + s[:-k]

print("Right rotation:", result)


# iv). USING LOOP FOR LEFT ROTATION

s = "python"
k = 3
result = s

for i in range(k):
    result = result[1:] + result[0]

print("Loop left rotation:", result)


# v). USING FUNCTION

def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1


print("Function:", is_rotation("waterbottle", "erbottlewat"))


# vi). CHECK ROTATION BY TRYING ALL SPLITS

s1 = "abcd"
s2 = "dabc"
is_rotated = False

for i in range(len(s1)):
    if s1[i:] + s1[:i] == s2:
        is_rotated = True
        break

print("All splits:", is_rotated)


# vii). NORMALIZE k GREATER THAN LENGTH

s = "python"
k = 14
k = k % len(s)

print("Normalized left rotation:", s[k:] + s[:k])


# viii). FIND ROTATION COUNT

s1 = "abcdef"
s2 = "defabc"
rotation_count = -1

for i in range(len(s1)):
    if s1[i:] + s1[:i] == s2:
        rotation_count = i
        break

print("Rotation count:", rotation_count)


# ix). CHECK LEFT ROTATION BY k

s1 = "abcdef"
s2 = "cdefab"
k = 2

print("Left by k:", s1[k:] + s1[:k] == s2)


# x). CHECK RIGHT ROTATION BY k

s1 = "abcdef"
s2 = "efabcd"
k = 2

print("Right by k:", s1[-k:] + s1[:-k] == s2)
