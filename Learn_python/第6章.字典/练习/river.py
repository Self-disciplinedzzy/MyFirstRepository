river_through = {
    'nile': 'sudan',
    'amazon': 'brazil',
    'danube': 'germany',
    'mekong': 'china',
    'rhine': 'france'
}
for river, countries in river_through.items():
    print(f"\nThe {river.title()} runs through {countries.title()}.")

for river in river_through.keys():
    print(river.title())
print('==================')
for countries in river_through.values():
    print(countries.title())


through_countries = ['china', 'france']
for river, countries in river_through.items():
    if countries in through_countries:
        print(f"The {river.title()} through {countries.title()}.")
    else:
        print(f"The {river.title()} not through {countries.title()}.")
