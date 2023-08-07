def simplefunction():
    print("say hello to function")
    a,b = 5,10
    x = a * b
    print(x)

simplefunction()

def sum(num1, num2):
    sum = num1 + num2
    print(sum)

sum(10,20)
sum(50,40)

def function(num1, num2):
    print(num1, "-", num2)

function(10,5)

def function(num1, num2=10):
    print(num1, "-", num2)

function(5)
function(5,20)

def func(name, old):
    print("My name is", name, "and i am", old, "years old")

func("Mottaki", 20)

var = "Hello "

def variable():
    print(var + "World")

variable()

x = "Hello "

def y():
    global x
    x = x + "World"
    print(x)

y()

x = "Hello "

def y():
    local = x
    local = local + "World"
    print(local)

y()

