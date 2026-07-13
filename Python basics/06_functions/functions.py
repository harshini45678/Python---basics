#function without parameters
def greetings():
    print("Happy new year!")

greetings()

#function with parameters
def hello(name):
    print("Hi " + name + "!. How are you? ")

hello("preethi")
hello("charan")
hello("tharun")

#default paarmeters
def num(a = 2, b = 5):
    print(a+b)

num()
num(10, 20)

