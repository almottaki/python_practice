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

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry", "mango")
#
# (green, yellow, *red) = fruits
#
# print(green)
# print(yellow)
# print(red)
#
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red) = fruits
#
# print(green)
# print(tropic)
# print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for x in range(len(thistuple)):
  print(thistuple[x])

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)