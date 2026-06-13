## ========================= PYTHON PRACTICE | QUETIONS WITH SOLUTIONS  ========================= #

## Python String:- 20 Questions

## Question 01: Reverse a String (All Methods)

## i). Slicing (Most Common)

s = "gautam"
print(s[::-1])

## ii). Using For Loop

s1 = "Arvind"
rev = ""

for i in s1:
    rev = i + rev

print(rev)

## iii). Index Loop

s2 = "categorization"
rev_1 = ""

for i in range(len(s2)-1, -1, -1):
    rev_1 += s2[i]

print(rev_1)


## iv). Using Reversed() Function

st = "Incomprehensibilities" 

print("".join(reversed(st)))

## v). Using Reversed() Iterator

s_1 = "Money"

for m in reversed(s_1):
    print(m, end = "")


## vi). Using While Loop

w = "Supercalifragilisticexpialidocious"

i = len(w) - 1
while i >= 0:
    print(w[i], end = "")

    i -= 1

## vii). One-Line Lambda Function

reverse = lambda l: l[::-1]
print(reverse("implementation"))

## viii). Recursion

def reverse_1(s):
    if len(s) == 0:
        return s
    return reverse_1 (s[1:]) + s[0]

print(reverse_1("Classfication"))

## ix). Stack Approach
 
s = "Initialization"
stack = []

for ch in s:
    stack.append(ch)

rev = ""

while stack:
    rev += stack.pop()

print(rev)

## x). Using Reduce

r = "Micro-service"

from functools import reduce

print(reduce(lambda x, y: y + x, r))


## xi). Using Insert Method

m = "Hyperparameter"

lst = []

for j in m:
    lst.insert(0, j)

print("".join(lst))

## xii). List Comprehension

n = "gautam"

print("".join([n[i] for i in range(len(n)-1, -1, -1)] ))


## xiii). Generator Expression

name = "sumit mishra"
print("".join(name[i] for i in range(len(name)-1, -1, -1)))
 