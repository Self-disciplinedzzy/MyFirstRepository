#学习之路 2021-10-7
#学习class类car
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_chuchang_name(self):
        long_name = f"{self.model} {self.make} {self.year}"
        return long_name.title()
my_Car = Car("aodi","r8",2021)
print(my_Car.get_chuchang_name())
