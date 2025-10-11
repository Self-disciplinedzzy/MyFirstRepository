cites = {
    'beijing': {
        'contry': 'china',
        'population': '21M',
        'fact': 'political center',
    },
    'new yourk': {
        'contry': 'america',
        'population': '8M',
        'fact': 'economic center',
    },
    'london': {
        'contry': 'britain',
        'population': '10M',
        'fact': 'arts center',
    },
}
for city, data in cites.items():
    print(f"The {city.title()} belong {data['contry'].title()} have "
          f"{data['population']} population, is the {data['fact'].title()}.")
