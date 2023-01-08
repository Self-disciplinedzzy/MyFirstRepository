'''类和实例 作业-1
2021-10-9
建一个Restaurant类，1.用__init__方法，2.restaurant.name和cuisine.type属性
创建describe_restaurant(）和open_restaurant()方法
方法一打印这两项信息，方法二打印一条消息，指餐馆正在营业
'''
class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def des_restaurant(self):
        print(f"This is {self.type} de {self.name} restaurant.")

    def open_restaurant(self):
        print("The restaurant opened 9:00")

r1 = Restaurant("renjian","malalang")
print(r1.name)
print(r1.type)
r1.open_restaurant()
r1.des_restaurant()
r2 = Restaurant("yuy","zhaji")
r2.des_restaurant()
r3 = Restaurant("pop","lili")
r3.des_restaurant()

#用户
class User:
    def __init__(self,list_name,frist_name,mod_name = "",hou_name = ""):
        self.list_name = list_name
        self.frist_name = frist_name
        self.mod_name = mod_name
        self.hou_name = hou_name
    def des_user(self):
        print(f"the people is {self.list_name} {self.frist_name} {self.mod_name} {self.hou_name}")
    def greet_user(self):
        print(f"THe is id id {self.frist_name} {self.list_name} {self.mod_name} {self.hou_name}")
        
        
u1 = User("zzy","zzu","zzi")
u2 = User("oop","ppo","wwq","wee")
u1.greet_user()
u2.greet_user()

