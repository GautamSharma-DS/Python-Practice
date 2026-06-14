# ===========================================================================================
#                          QUESTIONS 02:- CHECK PALINDROME STRING
# ===========================================================================================

# i). USING SHORTCUT

s = "level"
print(s == s[::-1])    # Output:- True



# ii). USING SLICING

s1 = "madam"

if s1 == s1[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")



# iii). USING Reversed() FUNCTION

s2 = "civic"

rev = "".join(reversed(s2))

print(s2 == rev)         # Output:- True



# iv). FOR LOOP

s3 = "refer"

rev = ""

for i in s3:
    rev = i + rev

print(s3 == rev)



# v). TWO POINTER (DSA STYLE - IMPORTANT)

s4 = "rotator"

left = 0
right = len(s4) - 1

while left < right:
    if s4[left] != s4[right]:
        print(False)
        
        break

    left  += 1
    right -= 1

else:
    print("True")

# Time:

# O(n)
# Space: O(1)



# vi). RECURSION

def palindrome(s5):
    
    if len(s5) <= 1:
        return True
    
    if s5[0] != s5[-1]:
        return False
    
    return palindrome(s5[1:-1])

print(palindrome("madam"))



# vii). STACK APPROACH

s6 = "radar"

stack = list(s6)

rev = ""

while stack:
    rev += stack.pop()

print(s6 == rev)



# viii). USING ALL() FUNCTION + INDEX COMPARISON 

n = "12321"

ans = all(
    n[i] == n[-i-1]
    for i in range(len(n)//2)

)
print(ans)



# ix). USING FUNCTION

def is_palindrome(c):
    return c == c[::-1]

print(is_palindrome("racecar"))



# x). CASE-INSENSITIVE PALINDROME

movie = "tenet"

print(movie.lower() == movie.lower()[::-1])



# xi). IGNORE SPACES

i = "nurese run"

i = i.replace(" ", "").lower()

print(i == i[::-1])



# xii) 1. IGNORE SPECIAL CHARACTERS

c = "A man, a plan, a canal: Panama"

clean = ""

for ch in c:
    if c.isalpha():
        clean += ch.lower()

print(clean == clean[::-1])



# Xiii) 2. IGNORE SPECIAL CHARACTERS

var = "A1b22b1A"

clean_1 = ""

for a in var:
    if a.isalnum():
        clean_1 += a.lower()

print(clean_1 == clean_1[::-1])



