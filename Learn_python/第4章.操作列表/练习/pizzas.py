pizzas = ['fanqie', 'lajiao', 'hujiao', 'yuanwei']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza.title()} pizza.\n")

print("I really love pizza.")

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append("zhishi")
friend_pizzas.append("yuanyang")
print("\nMy pizzas are:")
for pizza in pizzas:
    print(pizza)
print(pizzas)
print("\nMy friend_pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
print(friend_pizzas)
