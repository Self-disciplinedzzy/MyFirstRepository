favorite_place = {
    'xiaohong': ['wuchang', 'donghu', 'huanggang'],
    'xiaobai': ['xiaotao', 'tianmen', 'qianjiang'],
    'lihua': ['beijing', 'xianan', 'huanghelou'],
}

for name in favorite_place.keys():
    if name == 'xiaohong':
        for places in favorite_place[name]:
            print(f"{name.title()} like to go to {places.title()}.")
    elif name == 'xiaobai':
        for places in favorite_place[name]:
            print(f"{name.title()} like to go to {places.title()}.")
    elif name == 'lihua':
        for places in favorite_place[name]:
            print(f"{name.title()} like to go to {places.title()}.")
