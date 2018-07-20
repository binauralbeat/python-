planet_list = ["Mercury", "Mars"]
new_planets = "Jupiter", "Saturn"
planet_list.extend(new_planets)
planet_list.insert(2,"Venus")
planet_list.insert(1, "Earth")

spacecraft_list = tuple("Apple", "Mercury", "Mars")
print(planet_list)
