# fruits = ["apple","banana","mango"]
# x = fruits.index("banana")
# print(x)
#
#
#
#
# nestedList = [1, 2, 'a', ['b', 'c'], 1, 3]
# subList = nestedList[3]
# element = nestedList[3][0]
# print(subList)
# print(element)


def count_vowels_and_consonants(sentence):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0

    for x in sentence:
        if x in vowels:
            vowel_count += 1
        elif x in consonants:
            consonant_count += 1

    return vowel_count, consonant_count

sentence = input().strip()
vowels, consonants = count_vowels_and_consonants(sentence)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)