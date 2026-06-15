# =========================================================================================
#                              QUESTIONS 03:- COUNT VOWELS                                    
# =========================================================================================



# i). USING FOR LOOP

l = "International"

vowel = 0

for ch in l:
    if ch.lower() in "aeiou":
        vowel += 1

print(vowel)



# ii). sum() + generator expression (short)

# 1.
s = "Hello World"

count = sum(1 for ch in s if ch.lower() in "aeiou")

print(count)

# 2. list comprehension

s1 = "internatioonal"

c = sum([1 for ch in s1 if ch.lower() in "aeiou"])
print(c)



# iii). LIST COMPTREHENSION

s2 = "coding"

count_1 = len([i for i in s2 if i.lower() in "aeiou"])

print(count_1)



# iv). COUNT FREQUENCY OF EACH VOWELS USING DICTIONARY

s3 = "cooperation aeronautical"

vowels = {}

for i in s3:
    if i.lower() in "aeiou":
        vowels[i] = vowels.get(i, 0) + 1


print(vowels)



# v). RECURSIVE WAY

def count_vowels(s):
    if not s:
        return 0
    
    return (s[0].lower() in "aeiou") + count_vowels(s[1:])


print(count_vowels("frequency"))

