# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 == 1:
#         print("Weird")
#     elif 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print("Weird")
#     elif n > 20:
#         print("Not Weird")






if __name__ == '__main__':
    N = int(input())
    list = []
    list.insert(N, "e")
    print(list)
    list.pop(0)
    list.append(N)
    list.sort()
    list.pop()
    list.reverse()

