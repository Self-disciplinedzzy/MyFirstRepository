user_names = ['governor', 'president', 'driver', 'coach', 'admin']
user_names = []
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin, would you like to see status reprot?")
        else:
            print(f"Hello {user_name.title()}, thank you for logging in again.")
else:
    print("We need some users!")