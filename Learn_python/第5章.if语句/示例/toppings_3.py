available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pinepple', 'extra cheese']
request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in request_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}.")
    else:
        print(f"Sorry, we don't have {requested_topping.title()}")

print("\nFinished making your pizza.")