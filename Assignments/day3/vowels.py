def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def vowel_consonant_ratio(v, c):
    if c == 0:
        return "Infinity (No consonants in string)"
    return v / c

data = input("Enter any string: ")
v = count_vowels(data)
c = count_consonants(data)

ratio = vowel_consonant_ratio(v, c)
print("Number of vowels:", v)
print("Number of consonants:", c)
print("Vowel : Consonant Ratio =", ratio)