from session10 import ScreenInterface, Stack

def main ():
    interface1 = ScreenInterface(title="App Home Page")
    interface2 = ScreenInterface(title="Product 1 page")
    interface3 = ScreenInterface(title="Product 2 Page")

    stack = Stack()
    stack.push(interface1)
    stack.push(interface2)
    stack.push(interface3)

    # stack.pop()
    # stack.pop()

    stack.iterate()

    print("Stack:", vars(stack))


if __name__ == "__main__":
    main()
