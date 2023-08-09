x = open('/home/mottaki/Documents/file-handling.txt', 'r')

print(x.readline())
print(x.read())
print(x.read(20))

for a in x:
    print(a)

x = open('/home/mottaki/Documents/file-handling.txt', 'w')

x.write('Python is a Language')
print("Operation Done!")


x = open('/home/mottaki/Documents/file-handling.txt', 'a')

x.write('Python is a Language')
print("Operation Done!")