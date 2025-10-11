motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

motorcycles[0] = "dukadi"
# print(motorcycles)

motorcycles.append("honda")
# print(motorcycles)

motorcycles.insert(4, "KTM")
print(motorcycles)

# del motorcycles[4]
# print(motorcycles)

popped_motorcycle = motorcycles.pop(0)
print(f"My last motorcycle is {popped_motorcycle.title()}.")
print(motorcycles)

motorcycles.insert(0, "ducati")
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
message = f"This motorcycle is too expensive , so I give up the {too_expensive.title()}."
print(message)
print(motorcycles)