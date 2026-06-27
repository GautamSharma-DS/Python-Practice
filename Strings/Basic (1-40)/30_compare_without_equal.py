# =========================================================================================
#                              QUESTION 30: COMPARE WITHOUT EQUAL OPERATOR
# =========================================================================================


# i). USING compare RESULT WITH NOT LESS/GREATER

a = "hello"
b = "hello"

print("Not less/greater:", not (a < b) and not (a > b))


# ii). USING cmp STYLE FUNCTION

def compare_strings(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] < b[i] or a[i] > b[i]:
            return False

    return True


print("Function:", compare_strings("python", "python"))


# iii). USING ord()

a = "data"
b = "data"
same = True

if len(a) != len(b):
    same = False
else:
    for i in range(len(a)):
        if ord(a[i]) - ord(b[i]) != 0:
            same = False
            break

print("ord():", same)


# iv). USING zip()

a = "code"
b = "code"
same = len(a) == len(b) and all(not (x < y) and not (x > y) for x, y in zip(a, b))

print("zip():", same)


# v). CASE-INSENSITIVE COMPARE

a = "Python"
b = "python"
same = compare_strings(a.lower(), b.lower())

print("Case-insensitive:", same)


# vi). USING list COMPARISON

a = "python"
b = "python"
same = not (list(a) < list(b)) and not (list(a) > list(b))

print("List comparison:", same)


# vii). USING RECURSION WITHOUT == FOR CHARACTERS

def compare_recursive(a, b):
    if len(a) != len(b):
        return False

    if not a:
        return True

    if a[0] < b[0] or a[0] > b[0]:
        return False

    return compare_recursive(a[1:], b[1:])


print("Recursion:", compare_recursive("data", "data"))


# viii). COMPARE CASE-INSENSITIVE WITHOUT == ON ORIGINAL STRINGS

a = "Python"
b = "python"
same = compare_recursive(a.lower(), b.lower())

print("Case-insensitive recursion:", same)


# ix). COMPARE AFTER REMOVING SPACES

a = "hello world"
b = "helloworld"
same = compare_recursive(a.replace(" ", ""), b.replace(" ", ""))

print("Ignore spaces:", same)


# x). COMPARE LENGTH FIRST THEN CHARACTERS

a = "code"
b = "code"
same = True

if len(a) != len(b):
    same = False
else:
    for i in range(len(a)):
        if a[i] < b[i] or a[i] > b[i]:
            same = False
            break

print("Length then chars:", same)
