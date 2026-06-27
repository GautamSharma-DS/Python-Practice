# =========================================================================================
#                              QUESTION 21: TOGGLE CASE
# =========================================================================================


# i). USING swapcase()

s = "Hello World"
print("swapcase():", s.swapcase())


# ii). USING FOR LOOP

s = "PyTHon"
result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print("For loop:", result)


# iii). USING LIST COMPREHENSION

s = "OpenAI 123"
result = "".join([ch.lower() if ch.isupper() else ch.upper() if ch.islower() else ch for ch in s])

print("List comprehension:", result)


# iv). WITHOUT swapcase()

s = "aBcD"
result = ""

for ch in s:
    if "A" <= ch <= "Z":
        result += chr(ord(ch) + 32)
    elif "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
    else:
        result += ch

print("ASCII:", result)


# v). USING FUNCTION

def toggle_case(s):
    return "".join(ch.lower() if ch.isupper() else ch.upper() if ch.islower() else ch for ch in s)


print("Function:", toggle_case("GauTam"))


# vi). USING map()

s = "Map Method"
result = "".join(map(lambda ch: ch.lower() if ch.isupper() else ch.upper() if ch.islower() else ch, s))

print("map():", result)


# vii). USING translate()

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
table = str.maketrans(lower + upper, upper + lower)

s = "Translate Case 123"
print("translate():", s.translate(table))


# viii). USING RECURSION

def toggle_case_recursive(s):
    if not s:
        return ""

    ch = s[0]
    if ch.isupper():
        ch = ch.lower()
    elif ch.islower():
        ch = ch.upper()

    return ch + toggle_case_recursive(s[1:])


print("Recursion:", toggle_case_recursive("ReCurSion"))


# ix). TOGGLE ONLY ALPHABETS

s = "PyTHon 123!"
result = ""

for ch in s:
    if ch.isalpha():
        result += ch.lower() if ch.isupper() else ch.upper()
    else:
        result += ch

print("Only alphabets:", result)


# x). TOGGLE EACH WORD

s = "Hello World"
result_words = []

for word in s.split():
    result_words.append(word.swapcase())

print("Each word:", " ".join(result_words))


# xi). TOGGLE ALTERNATE CHARACTERS

s = "programming"
result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i].upper()
    else:
        result += s[i].lower()

print("Alternate characters:", result)
