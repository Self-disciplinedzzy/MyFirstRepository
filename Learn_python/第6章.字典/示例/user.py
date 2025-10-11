user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in user_0.keys():
    print(key.title())

for value in user_0.values():
    print(f"\n{value.title()}")
