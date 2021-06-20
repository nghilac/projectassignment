#               0           1           2           3           4           5        6          7           8           9
city_list = ["Oakland","Atlanta", " NewYorkCity", "Seattle", "Memphis", "Miami", "Boston", "LosAngelas", "Denver", "NewOrleans"]

city_list[0] = "SanFranciso"
city_list[2] = "Brooklyn"
city_list[7] = "HollyWood"
city_list[5] = "Tampa"

city_list.pop(4)
city_list.remove("Seattle")
del city_list[1]
 
threecities = (city_list[6:8])
print(threecities)

US_cities = city_list[5:9]
print(US_cities)

US_cities.append("Oakland")
US_cities.extend(["NewYorkCity", "LosAngeles"])
US_cities.insert(7,"Miami")

print(city_list)


#               0       1       2       3       4       5           6          7        8       9
animal_list = ["Dog","Cat", " Lion", "Bird", "Tiger", "Chicken", "Duck", "Lizard", "Seagull", "Otter"]
print(animal_list)
print(animal_list[4])


