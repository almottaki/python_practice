# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list1.extend(list2)
# print(list1)


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for data in list1:
    if data == "":
        list1.remove(data)

print(list1)

# list1 = [1, 1, 1, 0, 0, 0, 2, -2, -2]
# x = max(list1)
# print(x)
#
# list1 = [1, 1, 1, 0, 0, 0, 2, -2, -2]
# x = min(list1)
# print(x)
#
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
