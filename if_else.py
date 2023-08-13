input = int(input("Your Number: "))
a = input
if (a >= 80):
    print("You got A+")
elif (a >= 70):
    print("You got A")
elif (a >= 60):
    print("You got A-")
elif (a >= 50):
    print("You got B")
elif (a >= 40):
    print("You got C")
elif (a == 33):
    print("You are passed")
elif (a < 33):
    print("You are Fail")



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")