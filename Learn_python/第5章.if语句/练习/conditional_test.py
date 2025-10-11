name = 'zzy'
print("Is name = 'zzy'? I predict True.")
print(name == 'zzy')
print("\nIs name = 'ccy'? I predict False.")
print(name == 'ccy')

protection_object = 'TreE'
print(protection_object.title())
print(protection_object.title() == "Tree")
print(protection_object.lower() == "tree")

age = 18
print(age == 18)
print(age == 17)
print(age != 18)
print(age > 14)
print(age < 19)
print(age >= 19)
print(age <= 18)

guests = ['xiaoming', 'xiaozhang', 'xiaohong', 'lihua']
if 'lihua' in guests:
    print("lihua in guests")
else:
    print("lihua not in guests")

if 'libai' not in guests:
    print("libai not in guests")
else:
    print("libai in guests")
