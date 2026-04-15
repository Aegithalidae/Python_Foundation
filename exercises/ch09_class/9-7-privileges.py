# 9-7 Admin
class Users:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name
        self.full_name = f"{self.f_name} {self.l_name}"

    def describe_user(self):
        print("Here are the Users' profile\n")
        print(f"User name: {self.full_name.title()}")

    def greet_user(self):
        print(f"Greeting,{self.full_name.title()}!")


class Admin(Users):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print(f"{self.full_name.title()} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_privileges = ["can add post", "can delete post", "can ban user"]
admin = Admin("Wu", "Kaiyuan", admin_privileges)
admin.show_privileges()
