class User:
    def __init__(self,login_attempts,list_name,frist_name,mod_name = "",hou_name = ""):
        self.list_name = list_name
        self.frist_name = frist_name
        self.mod_name = mod_name
        self.hou_name = hou_name
        self.login_attempts = login_attempts
    def des_user(self):
        print(f"the people is {self.list_name} {self.frist_name} {self.mod_name} {self.hou_name}")
    def greet_user(self):
        print(f"THe is id id {self.frist_name} {self.list_name} {self.mod_name} {self.hou_name}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempte(self):
        self.login_attempts = 0
u1 = User(10,"ooo","ppp","zzz")
print(u1.login_attempts)
u1.increment_login_attempts()
print(u1.login_attempts)
u1.reset_login_attempte()
print(u1.login_attempts)

u1.increment_login_attempts()
print(u1.login_attempts)
u1.increment_login_attempts()

print(u1.login_attempts)

