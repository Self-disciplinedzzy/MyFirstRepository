#学习之路 2021-10-7
#继续学习classclass
#通过方法对属性的值进行递增
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def get_chuchang_name(self):
         long_name = f"{self.model} {self.make} {self.year}"
    def update_od(self,mileage):
        self.update_od = mileage
        if mileage >= self.mileage:
            self.mileage = mileage
        else:
            print("you can not")
    def zen_zhi(self,miles):
        self.odometer += miles
