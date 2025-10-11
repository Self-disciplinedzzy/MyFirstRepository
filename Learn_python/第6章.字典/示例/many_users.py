users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    'tnewton': {
        'first': 'isaac',
        'last': 'newton',
        'location': 'cambridge',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull_name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
