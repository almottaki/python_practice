# def pyramid_range(start, end):
#     num_rows = end - start + 1
#
#     for i in range(1, num_rows + 1):
#         # Print spaces before the numbers
#         print(" " * (num_rows - i), end="")
#
#         # Print numbers in ascending order
#         for j in range(start, start + i):
#             print(j, end="")
#
#         # Print numbers in descending order (exclude the first element to avoid repetition)
#         for j in range(start + i - 2, start - 1, -1):
#             print(j, end="")
#
#         # Move to the next line after each row is printed
#         print()
#
# # Example: Create a pyramid with a range of numbers from 1 to 5
# pyramid_range(1, 5)
#
#
#
#
#
#
#
#
# def pyramid_range(rows):
#     for x in range(1, rows + 1):
#         print("" * (rows - x), end="")
#         for y in range(1, x + 1):
#             print(y, end="")
#         print()
# pyramid_range(10)
# #
# #
# #
# #
# #
# #
# #
# #
# # def functiontest():
# #     a,b = 10,5
# #     x = a + b
# #     print(x)
# # functiontest()
#
# n = int(input())
# x = range(1, n+1)
# for a in x:
#     print(a, end="")
#
#
#
#
#