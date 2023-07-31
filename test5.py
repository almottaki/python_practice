# name = ["Mottaki", "Abdullah", "Mamun", "Tanjil", "Rana", "Kamal"]
# name.sort()
# print(name)
# name.sort(key = len)
# name.reverse()
# print(name)
#
#
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# if 4 in list:
#     print("Yes")
# else :
#     print("No")
#
#
#
# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     if y == 0:
#         raise ValueError("Cannot divide by zero.")
#     z = x // y
#     return z
#
#
# print("Welcome to the Python Calculator!")
# print("Select operation:")
# print("1. add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
#
# try:
#     choice = int(input("Enter choice (1/2/3/4): "))
#
#     if choice not in [1, 2, 3, 4]:
#         print("Invalid choice.")
#     else:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == 1:
#             print("Result:", add(num1, num2))
#         elif choice == 2:
#             print("Result:", subtract(num1, num2))
#         elif choice == 3:
#             print("Result:", multiply(num1, num2))
#         elif choice == 4:
#             print("Result:", divide(num1, num2))
#
# except ValueError:
#     print("Invalid input. Please enter numbers only.")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)