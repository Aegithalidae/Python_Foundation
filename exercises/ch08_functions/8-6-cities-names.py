# 8-6 cities_names
def city_country(city_name, nation):
    output = f"{nation}, {city_name}"
    return output.title()


while True:
    city_name = input("City name:")
    if city_name == "q":
        break

    nation = input("Nation:")
    if nation == "q":
        break

    result = city_country(city_name, nation)
    print(result)
