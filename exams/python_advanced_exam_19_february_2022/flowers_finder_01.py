from collections import deque

vowels = deque(input().split())
consonants = input().split()
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
word_found = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words.keys():
        words[word] = words[word].replace(vowel, "")
        words[word] = words[word].replace(consonant, "")
        if words[word] == "":
            print(f"Word found: {word}")
            word_found = True
            break
    if word_found:
        break

if not word_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

