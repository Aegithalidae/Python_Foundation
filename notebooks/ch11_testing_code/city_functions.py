def city_country_population(city_name, nation_name, population=""):
    if population:
        location_info = (
            f"{city_name.title()}, {nation_name.title()} -population {population}"
        )
    else:
        location_info = f"{city_name.title()}, {nation_name.title()}"

    return location_info
