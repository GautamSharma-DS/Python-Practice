def count_consonants(s):
    count = 0

    for ch in s.lower():
        if ch.isalpha() and ch not in "aeiou":
            count = count + 1

    return count

print(count_consonants("Hello World"))