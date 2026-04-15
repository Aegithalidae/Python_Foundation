# 9-1 restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(
            f"The restaurant name is {self.name.title()}\nThe restaurant offers {self.type}"
        )

    def open_restaurant(self):
        print(f"The {self.name.title()} is open now!")


restaurant = Restaurant("McDonald's", "fast food")
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
