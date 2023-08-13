def simplefunction():
    print("say hello to function")
    a,b = 5,10
    x = a * b
    print(x)

simplefunction()

def sum(num1, num2):
    sum = num1 + num2
    print(sum)

sum(10,20)
sum(50,40)

def function(num1, num2):
    print(num1, "-", num2)

function(10,5)

def function(num1, num2=10):
    print(num1, "-", num2)

function(5)
function(5,20)

def func(name, old):
    print("My name is", name, "and i am", old, "years old")

func("Mottaki", 20)

var = "Hello "

def variable():
    print(var + "World")

variable()

x = "Hello "

def y():
    global x
    x = x + "World"
    print(x)

y()

x = "Hello "

def y():
    local = x
    local = local + "World"
    print(local)

y()



# def split_and_join(line):
#     x = line.split(' ')
#     y = '-'.join(x)
#     return y
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
#
#
# def print_full_name(first, last):
#     full_name = f"{first} {last}"
#     print(f"Hello {full_name}! You just delved into Python.")
#
# if __name__ == '__main__':
#     n = int(input("Enter the number of names you want to input: "))
#
#     for i in range(n):
#         first_name = input("Enter the first name: ")
#         last_name = input("Enter the last name: ")
#         print_full_name(first_name, last_name)
#
# def print_full_name(first, last):
#     full_name = f"{first} {last}"
#     print(f"Hello {full_name}! You just delved into python.")
#
# if __name__ == '__main__':
#     first_name = input("")
#     last_name = input("")
#     print_full_name(first_name, last_name)
#
#
# def count_substring(string, sub_string):
#     count = 0
#     sub_len = len(sub_string)
#     str_len = len(string)
#
#     for i in range(str_len - sub_len + 1):
#         if string[i:i + sub_len] == sub_string:
#             count += 1
#
#     return count
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)


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

sentence = input().strip()
vowels, consonants = count_vowels_and_consonants(sentence)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)



# def pyramid_range(rows):
#     for x in range(1, rows + 1):
#         print("" * (rows - x), end="")
#         for y in range(1, x + 1):
#             print(y, end="")
#         print()
# pyramid_range(10)
#
#
# def functiontest():
#     a,b = 10,5
#     x = a + b
#     print(x)
# functiontest()
#
# n = int(input())
# x = range(1, n+1)
# for a in x:
#     print(a, end="")



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    z = x // y
    return z


print("Welcome to the Python Calculator!")
print("Select operation:")
print("1. add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = int(input("Enter choice (1/2/3/4): "))

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice.")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))

except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")