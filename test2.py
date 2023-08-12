w = 14
x = 1.00
y = +-12j
z = -87e7100

print(type(w))
print(type(x))
print(type(y))
print(type(z))

a = 10  # int
b = -1.2  # float
c = 5j  # complex

# convert from int to float:
x = float(a)

# convert from float to int:
y = int(b)

# convert from float to complex:
z = complex(c)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

import random

print(random.randrange(11, 12))

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = str("4.5")   # w will be 4.5

print(x)
print(y)
print(z)
print(w)

print(type(x))
print(type(y))
print(type(z))
print(type(w))

a = "PYTHON!"
print(a[6])

a = "PYTHON!"
print(a[-4:-1])

for name in "MOTTAKI":
    print(name)


a = "MOTTAKI"
print(len(a))

a = ""
print(len(a))

txt = "Man is immortal!"
print("mortal" not in txt)

a = "Hello, World!"
print(a.upper())

x = "My Name is MOTTAKI!"
print(x.lower())

a = "It's PYTHON!"
print(a.replace("t's", "ts"))

a = "        Hello, World!         "
print(a.strip())

a = "Hello, World!"
print(a.split())

fruits = ["apple","banana","mango"]
x = fruits.index("banana")
print(x)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

name = "MOTTAKI"
age = 20
Intro = "My name is {}, I am {} years old."
print(Intro.format(name, age))

quantity = 3
item = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, item, price))

x = 10
y = 20
if (x + y) > 25:
    print("true")


b = "Hello, World!"
print(b[:-2])