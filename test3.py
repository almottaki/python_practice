for name in "MOTTAKI":
    print(name)

quantity = 3
item = 567
price = 49.95
print(f"I want {quantity} pieces of item {item} for {price} dollars")

a = "It is \"too difficult to\" understand!"
print(a)

print(bool("0"))
print(bool(0))

x = "MOTTAKI"
print(len(x))

x = 10
y = 20
print(x//y)

x = ["apple", "banana", "cherry"]
print(len(x))

a = ["apple", "banana", "cherry"]
b = [1, 5, 7, 9, 3]
c = [True, False, False]
print(a[:-2])
print(c)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

a = ["apple", "banana", "cherry"]
print(a)

b = list(("apple", 50, 100, 200, "cherry"))
print(b[-3])
print(b[-5:-3])
if "apple" in b :
    print("yes, 'apple' is in the list.")

x = [1, 2, 5, 7, 9]
x[1] = 3
print(x)

x = [1, 2, 5, 8, 9]
x[1:3] = [3, 6, 7]
print(x)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

a = ["apple", "banana", "cherry"]
a.insert(0, "watermelon")
print(a)

a = [1, 3, 5, 7]
a.append(9)
print(a)

x = ["apple", "banana", "cherry"]
y = ["mango", "pineapple", "papaya"]
z = []
for data in x:
    z.append(data)
    if data == "banana":
        print("Yes")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

x = [x for x in fruits if "a" in x]

print(x)

a = [1, 3, 7, 9]
b = [0]
b.remove(0)
b.extend(a)
print(b)