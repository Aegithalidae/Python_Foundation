# 9-2 THREE RESTAURANT
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


restaurant_1 = Restaurant("Sushi Zen", "japanese")
restaurant_2 = Restaurant("Pasta House", "italian")
restaurant_3 = Restaurant("Spicy Garden", "chinese")
restaurant_list = [restaurant_1, restaurant_2, restaurant_3]
for _ in restaurant_list:
    _.describe_restaurant()
    print("---")
