# x = open('/home/mottaki/Documents/file-handling.txt', 'r')
#
# print(x.readline())
# print(x.read())
# print(x.read(20))
#
# for a in x:
#     print(a)
#
# x = open('/home/mottaki/Documents/file-handling.txt', 'w')
#
# x.write('Python is a Language')
# print("Operation Done!")
#
#
# x = open('/home/mottaki/Documents/file-handling.txt', 'a')
#
# x.write('Python is a Language')
# print("Operation Done!")


products = [
    {"name": "iPhone 13", "category": "smartphone", "price": 999},
    {"name": "Samsung Galaxy S21", "category": "smartphone", "price": 899},
    {"name": "iPad Pro", "category": "tablet", "price": 799},
    {"name": "Sony Xperia", "category": "smartphone", "price": 799},
    {"name": "MacBook Air", "category": "laptop", "price": 999},
]

for product in products:
    if "category" in product and product["category"] == "smartphone":
        print(product)
