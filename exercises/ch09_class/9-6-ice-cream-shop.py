# 9-6 ice cream stand
class Restaurant:
    """初始化餐馆，包括餐馆名称和菜系类型"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆信息"""
        print(
            f"The restaurant name is {self.name.title()}\nThe restaurant offers {self.type}"
        )

    def open_restaurant(self):
        """描述餐馆正在营业"""
        print(f"The {self.name.title()} is open now!")


class IceCreamStand(Restaurant):
    """冰淇淋店是餐馆的一种特殊类型"""

    def __init__(self, restaurant_name, cuisine_type, ice_cream_flavor):
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavor = ice_cream_flavor

    def describe_ice_cream_flavor(self):
        """描述冰激凌口味"""
        print("Here are our ice cream flavors:")
        for flavor in self.ice_cream_flavor:
            print(f"- {flavor}")


ice_stand_1_flavor = "Vanilla, Chocolate, Strawberry, Matcha, Mango, Durian, Cookies and Cream, Salted Caramel, Blueberry, Pistachio"
ice_stand_1_list = ice_stand_1_flavor.split(", ")
ice_stand_1 = IceCreamStand("Creamy Corner", "ice cream", ice_stand_1_list)

ice_stand_1.describe_ice_cream_flavor()
