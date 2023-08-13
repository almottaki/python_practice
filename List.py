Roll = [1, 2, 3, 5, 6, 8, 9]
for x in Roll:
    print(x)


list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if 4 in list:
    print("Yes")
else :
    print("No")


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


name = ["Mottaki", "Abdullah", "Mamun", "Tanjil", "Rana", "Kamal"]
name.sort()
print(name)
name.sort(key = len)
name.reverse()
print(name)



a = ["apple", "banana", "cherry", "kiwi", "mango"]
b = []

for x in a:
   if "e" in x:
      b.append(x)

print(b)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ["hello" for x in fruits]
print(newlist)

newlist = [x if x != "cherry" else "orange" for x in fruits]
print(newlist)

thislist = ["3", "7", "0", "2", "5"]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

a = ["a", "b", "c"]
b = [1, 2, 3]
c = a + b
print(c)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

a = ["a", "b", "c"]
b = [1, 2, 3]
a.extend(b)
print(a)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list1.extend(list2)
print(list1)


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for data in list1:
    if data == "":
        list1.remove(data)

print(list1)

list1 = [1, 1, 1, 0, 0, 0, 2, -2, -2]
x = max(list1)
print(x)

list1 = [1, 1, 1, 0, 0, 0, 2, -2, -2]
x = min(list1)
print(x)

nestedList = [1, 2, 'a', ['b', 'c'], 1, 3]
subList = nestedList[3]
element = nestedList[3][0]

nestedlist = ['a', [1, 2, 'b'], [4, 5, 6], [7, 8, 'c', 9]]
for list in nestedlist:
  for number in list:
    print(number, end=' ')

x = [item for sublist in nestedlist for item in sublist]

print(x)