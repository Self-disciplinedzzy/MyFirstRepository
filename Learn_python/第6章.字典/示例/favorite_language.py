favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'java',
    'phill': 'javascrip',
    'killy': 'rust'
}
language = favorite_language['jen']
print(f"Jen's favorite language is {language.title()}.")

for name, language in favorite_language.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

friends = ['phill', 'sarah']
for name in favorite_language.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

if 'erin' not in favorite_language.keys():
    print("\nErin, please take our poll.")


for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print('\nThe following languages have been mentioned.')
for language in set(favorite_language.values()):
    print(language.title())
