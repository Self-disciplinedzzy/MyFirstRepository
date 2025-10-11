requseted_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requseted_topping in requseted_toppings:
    if requseted_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requseted_topping.title()}. ")
print("\nFinished making your pizza.")

requseted_toppings = []
if requseted_toppings:
    for requseted_topping in requseted_toppings:
        print(f"Adding {requseted_topping.title()}")
    print("Finished making your pizza.")
else:
    print("\nAre you sure you want a plain pizza?")
