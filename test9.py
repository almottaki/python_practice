fruits = ["apple","banana","mango"]
x = fruits.index("banana")
print(x)




nestedList = [1, 2, 'a', ['b', 'c'], 1, 3]
subList = nestedList[3]
element = nestedList[3][0]



def count_vowels_and_consonants(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for x in sentence:
        if x in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count
if __name__ == '__main__':
    sentence = "python is a language"
    vowels, consonants = count_vowels_and_consonants(sentence)
    print("Number of vowels:", vowels)
    print("Number of consonants:", consonants)


def math(a, b, c, d):
    x = a ** b
    y = c ** d
    return x + y

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = math(a, b, c, d)
print(result)

nestedlist = ['a', [1, 2, 'b'], [4, 5, 6], [7, 8, 'c', 9]]
for list in nestedlist:
  for number in list:
    print(number, end=' ')

x = [item for sublist in nestedlist for item in sublist]

print(x)

