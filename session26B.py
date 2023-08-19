#NESTED/LOCAL FUNCTION
# create function inside another function

def outer():
    print("this is outer function")
    def inner():#nested/local function
        print("this is inner function")

    # inner()
    return inner

result = outer()
result()
