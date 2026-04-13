# 8-14 cars
def make_car(brand, region, **others):
    cars = {}
    cars["brand"] = brand
    cars["region"] = region
    for key, value in others.items():
        cars[key] = value
    return cars


car = make_car("subaru", "outback", color="blue", tow_package=True)
print("cars = ", car)
