# 9-5 Login attempts
class Users:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name
        self.full_name = f"{self.f_name} {self.l_name}"
        self.login_attempts = 0

    def describe_user(self):
        print("Here are the Users' profile\n")
        print(f"User name: {self.full_name.title()}")

    def greet_user(self):
        print(f"Greeting,{self.full_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = Users("john", "doe")
print(user.login_attempts)

for i in range(101):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
