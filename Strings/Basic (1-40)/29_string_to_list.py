# =========================================================================================
#                              QUESTION 29: STRING TO LIST
# =========================================================================================


# i). USING list()

s = "python"
print("list():", list(s))


# ii). USING split() FOR WORDS

s = "Python is easy"
print("split():", s.split())


# iii). USING FOR LOOP

s = "hello"
lst = []

for ch in s:
    lst.append(ch)

print("For loop:", lst)


# iv). USING LIST COMPREHENSION

s = "gautam"
lst = [ch for ch in s]

print("List comprehension:", lst)


# v). COMMA SEPARATED STRING TO LIST

s = "red,green,blue"
lst = s.split(",")

print("Comma split:", lst)


# vi). USING map()

s = "12345"
lst = list(map(int, s))

print("map():", lst)


# vii). USING unpacking

s = "hello"
lst = [*s]

print("Unpacking:", lst)


# viii). WORDS USING REGEX

import re

s = "red, green; blue"
lst = re.findall(r"[A-Za-z]+", s)

print("Regex words:", lst)


# ix). USING ast.literal_eval FOR LIST-LIKE STRING

import ast

s = "['python', 'java', 'c']"
lst = ast.literal_eval(s)

print("literal_eval():", lst)


# x). STRING TO LIST OF WORD LENGTHS

s = "Python is easy"
lst = [len(word) for word in s.split()]

print("Word lengths:", lst)


# xi). STRING TO LIST OF ASCII VALUES

s = "ABC"
lst = [ord(ch) for ch in s]

print("ASCII values:", lst)


# xii). STRING TO NESTED LIST OF WORD CHARACTERS

s = "hi ok"
lst = [list(word) for word in s.split()]

print("Nested list:", lst)
