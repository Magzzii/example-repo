''' Holiday Cost 20/07/2026 '''
# City flight options and prices
city_flights = {
    "Johannesburg": 5000,
    "George": 4000,
    "Cape Town": 6000,
    "Durban": 4500,
    "Port Elizabeth": 5500,
    "Pretoria": 4800,
    "Bloemfontein": 4700,
    "Kimberley": 4300,
    "East London": 4600,
    "Nelspruit": 4900,
}


def hotel_cost(num_nights):
    """Return the total hotel cost for the number of nights."""
    hotel_per_night = 955.85
    return num_nights * hotel_per_night


def plane_cost(destination_city):
    """Return the flight cost for the chosen city."""
    if destination_city in city_flights:
        return city_flights[destination_city]
    else:
        print("City not found. Please pick one of the listed cities.")
        return 0


def car_rental(rental_days):
    """Return the total car rental cost for the number of days."""
    daily_rental_cost = 550.00
    return rental_days * daily_rental_cost


def holiday_cost(num_nights, destination_city, rental_days):
    """Return the total holiday cost."""
    total = hotel_cost(num_nights) + plane_cost(destination_city) + car_rental(rental_days)
    return total


print("Available cities:")
for i, city in enumerate(city_flights, start=1):
    print(f"{i}. {city}")

while True:
    city_choice = input("Choose a number from the list above: ").strip()
    if city_choice.isdigit():
        city_index = int(city_choice) - 1
        if 0 <= city_index < len(city_flights):
            city_flight = list(city_flights.keys())[city_index]
            break
    print("Please enter a valid number from the list.")

while True:
    try:
        stay_nights = int(input("Enter the number of nights you will stay: "))
        if stay_nights >= 0:
            break
    except ValueError:
        print("Please enter a valid whole number.")

while True:
    try:
        rental_days = int(input("Enter how many days you will rent a car: "))
        if rental_days >= 0:
            break
    except ValueError:
        print("Please enter a valid whole number.")

hotel_total = hotel_cost(stay_nights)
plane_total = plane_cost(city_flight)
car_total = car_rental(rental_days)
total_cost = holiday_cost(stay_nights, city_flight, rental_days)

print("\nHoliday details")
print("=" * 20)
print(f"City: {city_flight}")
print(f"Hotel cost: R{hotel_total:.2f}")
print(f"Plane cost: R{plane_total:.2f}")
print(f"Car rental cost: R{car_total:.2f}")
print(f"Total holiday cost: R{total_cost:.2f}")
