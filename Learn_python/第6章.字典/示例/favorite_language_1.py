favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c', 'c++'],
    'edward': ['rust', 'go'],
    'phill': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite_language are:")
    for language in languages:
        print(f"\t{language.title()}")
