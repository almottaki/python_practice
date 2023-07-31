Roll = [1, 2, 3, 5, 6, 8, 9]
for x in Roll:
    print(x)

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