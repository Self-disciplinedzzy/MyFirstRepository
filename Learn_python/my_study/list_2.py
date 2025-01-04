motorcycles_1 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_1)

motorcycles_1[0] = 'ducati'
print(motorcycles_1)
del motorcycles_1[0]
print(motorcycles_1)

motorcycles_1.append('honda')
del motorcycles_1[0]
print(motorcycles_1)

motorcycles_2 = []
motorcycles_2.append("honda")
motorcycles_2.insert(0, "yamaha")
motorcycles_2.append("suzuki")
motorcycles_2.insert(-1, "ducati")
print(motorcycles_2)

poped_motorcycles = motorcycles_2.pop()
message = f"My last motorcycle is {
    poped_motorcycles.title()}, I want to del it now."
print(message)
print(motorcycles_2)

too_expensive = "suzuki"
motorcycles_1.remove(too_expensive)
print(motorcycles_1)
message_2 = f"{too_expensive.title()} is too expensive."
print(message_2)
