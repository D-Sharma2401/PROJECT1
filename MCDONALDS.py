def upgrade_to_meal(func):

    def inner(amount, taxes, meal_plan):
        if meal_plan == 1:
            print("upgrading to medium meal..")
            print("ADDED COKE")
            print("+ADDED FRIES")
            amount += 100
            taxes = 0.18
        elif meal_plan == 2:
            print("upgrading to large meal..")
            print("+ADDED LARGE COKE")
            print("+ADDED LARGE FRIES")
            print("+ADDED Ice Cream")
            amount += 200
            taxes = 0.20
        else:
            print("Thank you for the purchase")

        return func(amount, taxes, meal_plan)
    return inner


@upgrade_to_meal
def buy_burger(amount,taxes, meal_plan=0):
    return amount + (amount*taxes)

amount_to_pay = buy_burger(100,0.10, 2)
print("Mc Donald's Final Price: ", amount_to_pay)