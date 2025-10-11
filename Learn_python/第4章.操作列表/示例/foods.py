my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My friend favorite food is:")
print(friend_foods)
print("\nMy favorite food is:")
print(my_foods)
for my_food in my_foods:
    print(my_food.title())

for friend_food in friend_foods:
    print(friend_food.title())
