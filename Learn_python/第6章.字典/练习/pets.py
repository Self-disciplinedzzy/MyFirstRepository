pet_1 = {
    'master': 'ren1',
    'name': 'dog',
    'age': 3,
}
pet_2 = {
    'master': 'ren2',
    'name': 'cat',
    'age': 1.5,
}
pet_3 = {
    'master': 'ren3',
    'name': 'pig',
    'age': 5,
}
pet_4 = {
    'master': 'ren4',
    'name': 'sheep',
    'age': 7,
}
pets = [pet_1, pet_2, pet_3, pet_4]
for pet in pets:
    print(f"主人是:{pet['master']}"
          f"宠物是:{pet['name']}"
          f"\tage: {pet['age']}.")
print('over')
