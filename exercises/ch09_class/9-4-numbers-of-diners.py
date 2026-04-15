# 9-4 Numbers of diners
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print
        (
            f"The restaurant name is {self.name.title()}\nThe restaurant offers {self.type}"
        )

    def open_restaurant(self):
        print(f"The {self.name.title()} is open now!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num):
        self.number_served += num


restaurant = Restaurant("McDonald's", "fast food")
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(150)
print(restaurant.number_served)

restaurant.increment_number_served(300)
print(restaurant.number_served)
