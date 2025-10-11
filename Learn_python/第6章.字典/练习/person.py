person_1 = {
    'age': 27,
    'first_name': 'xiao',
    'last_name': 'yan',
    'city': 'zhongzhou',
}
for key, value in person_1.items():
    print(f"{key.title()}:{value}")
person_2 = {
    'age': 28,
    'first_name': 'xiao',
    'last_name': 'li',
    'city': 'xuanhuang',
}
person_3 = {
    'age': 28,
    'first_name': 'xiao',
    'last_name': 'ding',
    'city': 'xuanhuang',
}
people = [person_1, person_2, person_3]
for persons in people:
    print("\n----------------------")
    print(f"{persons['first_name']} {persons['last_name']}")
    for key, value in persons.items():
        print(f"{key}:{value}")
