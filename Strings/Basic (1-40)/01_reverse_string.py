# =========================================================================================
#                    QUESTION 01:- REVERSE A STRING (MULTIPLE APPROACHES)
# =========================================================================================


# i). SLICING (MOST COMMON)

s = "gautam"
print(s[::-1])



# ii). USING FOR LOOP

s1 = "Arvind"
rev = ""

for i in s1:
    rev = i + rev

print(rev)



# iii). INDEX LOOP

s2 = "categorization"
rev_1 = ""

for i in range(len(s2)-1, -1, -1):
    rev_1 += s2[i]

print(rev_1)



# iv). USING Reversed() FUNCTION


st = "Incomprehensibilities" 

print("".join(reversed(st)))



# v). USING Reversed() ITERATOR


s_1 = "Money"

for m in reversed(s_1):
    print(m, end = "")



# vi). USING WHILE LOOP


w = "Supercalifragilisticexpialidocious"

i = len(w) - 1
while i >= 0:
    print(w[i], end = "")

    i -= 1



# vii). ONE-LINE LAMBDA FUNCTION

reverse = lambda l: l[::-1]
print(reverse("implementation"))



# viii). RECURSION


def reverse_1(s):
    if len(s) == 0:
        return s
    return reverse_1 (s[1:]) + s[0]

print(reverse_1("Classfication"))



# ix). STACK APPROACH

 
s = "Initialization"
stack = []

for ch in s:
    stack.append(ch)

rev = ""

while stack:
    rev += stack.pop()

print(rev)



# x). USING REDUCE

r = "Micro-service"

from functools import reduce

print(reduce(lambda x, y: y + x, r))



# xi). USING INSERT METHOD

m = "Hyperparameter"

lst = []

for j in m:
    lst.insert(0, j)

print("".join(lst))



# xii). LIST COMPREHENSION

n = "gautam"

print("".join([n[i] for i in range(len(n)-1, -1, -1)] ))



# xiii). GENERATOR EXPRESSION

name = "extraordinary"
print("".join(name[i] for i in range(len(name)-1, -1, -1)))
 


