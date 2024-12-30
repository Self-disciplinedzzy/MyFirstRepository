# Created on 张振宇的iPad.
class Car:
    def __init__(self,name,make,year):
        self.name = name
        self.year = year
        self.make = make
    def move_kil(self):
        self.kil = 100
    def moveing(self):
        print(f"zhe ge che zup le {self.kil}")
    def jian_yan(self):
        print("jian yan ji cheng ")
class Vcar(Car):
    def __init__(self,name,make,year):
        super().__init__(name,make,year)
        self.wide = 100
    def describe(self):
        print(f"dian chi yong liang: {self.wide}")
    
my_va = Vcar("zzy","aodi",2021)


my_va.describe()
print(my_va.wide)

  
#my_va = Vcar("zzy","aodi",2020)
print("my vcar di car name:")
print("*"*100)
print(my_va.name)
print("*" *100)
print(my_va.make)
print("*" *100)
print(my_va.year)

