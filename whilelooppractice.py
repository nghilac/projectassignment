groceries = {"chicken": 1.59 , "beef": 1.99 , "cheese": 1.00 , "milk": 2.50}
shoes = {"Jordan13": 1, "Yeezy": 8, "Foamposite": 10, "AirMax": 5, "SBDunk": 20}


def rectangleArea(width, height):
    area = width * height
    return area

"chicken", "beef", "cheese", "milk"

def total_price(item1, item2):
    item1_price = groceries[item1]
    item2_price = groceries[item2]
    price = item1_price + item2_price

    return price

#print("chicken and cheese price")
#print(total_price("chicken","cheese")) # 2.59

print("chicken and cheese price " + str(total_price ("chicken", "cheese")))
print("milk and beef price " + str(total_price ("milk", "cheese")))

def price_difference(item1, item2):
    item1_price = groceries[item1] #milk -> 2.5
    item2_price = groceries[item2] #cheese -> 1.8

    if item1_price > item2_price:
        difference = item1_price - item2_price
    else:
        difference = item2_price - item1_price

    #difference = item1_price - item2_price

    return difference

print(price_difference("chicken", "cheese"))
print(price_difference("chicken", "milk"))


