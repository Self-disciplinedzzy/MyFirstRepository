cubic_numbers = [number**3 for number in range(1, 11)]
for cubic_number in cubic_numbers:
    print(cubic_number)

print(cubic_numbers)

print("\nThe first three items in the list are:")
print(cubic_numbers[:3])

print("\nThree items from the middle of the list are:")
print(cubic_numbers[3:6])

print("\nThe last three items in the list are:")
print(cubic_numbers[-3:])
