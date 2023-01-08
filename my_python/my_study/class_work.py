#学习之路 2021-10-7
#学习练习
class Restaurant:
    def __init__(self,name,type,year):
        self.name = name
        self.type = type
        self.year = year
        self.number = 10   
    def describe_restaurant(self):
        print(f"You's restaurant name call {self.name}.")
        print(f"You's restuarant type id {self.type}.")
    def open_restaurant(self):
        print("The restaurant open 6 o'colok")
    def number_restaurant(self):
        print(f"have {self.number} people can eat out there.")
res_1 = Restaurant("lili","huo",10)
res_1.describe_restaurant()
res_1.open_restaurant()
res_1.number = 20
res_1.number_restaurant()
