#Decorator
#1. create a function, which takes function as input
#2. Create an inner function, which should have same signature for the target function
#3.execute the passed function from the inner function
#4.return inner function from outer function
#5. to decorate any function use @function
def compute_taxes(func):

    def inner(amount, taxes):
        if amount > 0 and amount <= 10000:
            taxes = 0.18
        elif amount > 10000 and amount <=100000:
            taxes = 0.25
        else:
            print("Invalid amount")

        return func(amount, taxes)
    return inner

@compute_taxes
def pay(amount, taxes):
    return amount + (amount*taxes)

amount_to_pay = pay(50000, 0)
print("amount to pay: ", amount_to_pay)