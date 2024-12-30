class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
    def des_restaurant(self):
        print(f"This is {self.type} de {self.name} restaurant.")
    def num_ed(self):
        print(f"The restaurant is get {self.number_served}")
    def set_ed(self,setber_ed):
        self.num_ed = setber_ed
    def incment_num_ed(self,setber):
        self.number_served += setber
    def open_restaurant(self):
        print("The restaurant opened 9:00")
r1 = Restaurant("opo","hou")

r1.number_served = 1000
print(r1.number_served)
r1.incment_num_ed(20)
print(r1.number_served)
