def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
print("cost of car rental",rental_car_cost(3000))
print("cost of plane  ride ",plane_ride_cost("Los Angeles"))
print("cost of hotel room",hotel_cost(3000))
print("cost of  trip",trip_cost("Los Angeles",3000,20000000))
