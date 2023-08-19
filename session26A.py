#Function as input
#i.e. passing the function by reference

def show(func):
    print("show executed:")
    func()

def hello():
    print("this is hello")
    print("hello function finished...")

def bye():
    print("this is bye")
    print("bye function executed...")

show(hello)
print(",,,,,,,,,,")

show(bye)

