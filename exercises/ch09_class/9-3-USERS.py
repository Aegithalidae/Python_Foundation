# 9-3 USERS
"""
class Users():
    def __init__(self, first_name, last_name):
        Users.f_name = first_name
        Users.l_name = last_name
        Users.full_name = f"{Users.f_name} {Users.l_name}"

    def describe_user(self):
        print("Here are the Users' profile\n")
        print(f"User name: {Users.full_name.title()}")

    def greet_user(self):
        print(f"Greeting,{Users.full_name.title()}!")

user_data = [
    ('john', 'doe'),
    ('jane', 'doe'),
    ('alice', 'smith'),
    ('bob', 'johnson')
]
users = []
for first_name, last_name in user_data:
    user = Users(first_name, last_name)
    users.append(user)
for user in users:
    user.describe_user()
    user.greet_user()
    print('---')
"""

"""
上面的代码存在一个问题，即使用了类属性来存储用户数据。类属性是属于类的，而不是属于实例的，因此所有实例共享同一个类属性。
当创建多个用户实例时，最后一个创建的用户的数据会覆盖之前的用户数据，导致所有实例都显示最后一个创建的用户的信息。
这就好比所有用户都在使用同一个账户，无法区分不同用户的数据。
"""

# 使用类属性来存储用户数据可能会导致数据混乱，因为所有实例共享同一个类属性。
# 每次创建一个新的用户实例时，都会覆盖之前的用户数据，导致所有实例都显示最后一个创建的用户的信息。
# 这就好比所有用户都在使用同一个账户，无法区分不同用户的数据。
# 所以应该使用实例属性来存储每个用户的独立数据，这样每个用户实例都有自己的属性，不会互相干扰。
# 修改方式为将类属性改为实例属性，即在__init__方法中使用self来定义属性，而不是直接使用类名。如下所示：


# 9-3 USERS
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


user_data = [("john", "doe"), ("jane", "doe"), ("alice", "smith"), ("bob", "johnson")]
users = []
for first_name, last_name in user_data:
    user = Users(first_name, last_name)
    users.append(user)
for user in users:
    user.describe_user()
    user.greet_user()
    print("---")
