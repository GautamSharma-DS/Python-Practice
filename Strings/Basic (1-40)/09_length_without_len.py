# =========================================================================================
#                              QUESTION 09: LENGTH WITHOUT len()
# =========================================================================================


# i). USING FOR LOOP

s = "Python"
count = 0

for ch in s:
    count += 1

print("For loop:", count)


# ii). USING WHILE LOOP

s = "Practice"
count = 0

while s[count:count + 1]:
    count += 1

print("While loop:", count)


# iii). USING enumerate()

s = "Gautam"
count = 0

for count, ch in enumerate(s, start=1):
    pass

print("enumerate():", count)


# iv). USING sum()

s = "Programming"
count = sum(1 for ch in s)

print("sum():", count)


# v). USING RECURSION

def string_length(s):
    if s == "":
        return 0

    return 1 + string_length(s[1:])


print("Recursion:", string_length("Hello"))


# vi). USING FUNCTION

def length_without_len(s):
    count = 0

    for ch in s:
        count += 1

    return count


print("Function:", length_without_len("Data"))


# vii). USING LIST CONVERSION WITHOUT len()

s = "Practice"
lst = list(s)
count = 0

for ch in lst:
    count += 1

print("List conversion:", count)


# viii). LENGTH OF EACH WORD WITHOUT len()

s = "Python is easy"
word_lengths = {}

for word in s.split():
    count = 0
    for ch in word:
        count += 1
    word_lengths[word] = count

print("Each word:", word_lengths)


# ix). LENGTH OF LIST OF STRINGS WITHOUT len()

words = ["Python", "Java", "C"]
lengths = []

for word in words:
    count = 0
    for ch in word:
        count += 1
    lengths.append(count)

print("List of strings:", lengths)
