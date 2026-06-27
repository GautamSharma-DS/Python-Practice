# =========================================================================================
#                              QUESTION 26: REVERSE WORD ORDER
# =========================================================================================


# i). USING split() AND SLICING

s = "Python is easy"
result = " ".join(s.split()[::-1])

print("Slicing:", result)


# ii). USING reversed()

s = "Hello World Python"
result = " ".join(reversed(s.split()))

print("reversed():", result)


# iii). USING STACK

s = "Data Science Course"
stack = s.split()
result = []

while stack:
    result.append(stack.pop())

print("Stack:", " ".join(result))


# iv). USING FOR LOOP

s = "Good Morning India"
words = s.split()
result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i] + " "

print("For loop:", result.strip())


# v). USING FUNCTION

def reverse_word_order(s):
    return " ".join(s.split()[::-1])


print("Function:", reverse_word_order("Python Practice Folder"))


# vi). USING insert()

s = "Insert method example"
result = []

for word in s.split():
    result.insert(0, word)

print("insert():", " ".join(result))


# vii). USING RECURSION

def reverse_words_recursive(words):
    if not words:
        return []

    return reverse_words_recursive(words[1:]) + [words[0]]


s = "reverse with recursion"
print("Recursion:", " ".join(reverse_words_recursive(s.split())))


# viii). PRESERVE CLEAN SINGLE SPACES

s = "  Python    basic   strings "
result = " ".join(s.split()[::-1])

print("Clean spaces:", result)


# ix). REVERSE WORD ORDER WITH PUNCTUATION

s = "Hello, world! Python."
result = " ".join(s.split()[::-1])

print("With punctuation:", result)


# x). REVERSE WORD ORDER IN EACH LINE

text = """Python is easy
Practice daily"""

answers = []

for line in text.splitlines():
    answers.append(" ".join(line.split()[::-1]))

print("Each line:", answers)


# xi). REVERSE WORD ORDER FROM LIST OF SENTENCES

sentences = ["Hello World", "Python Code"]
answers = []

for sentence in sentences:
    answers.append(" ".join(sentence.split()[::-1]))

print("List of sentences:", answers)
