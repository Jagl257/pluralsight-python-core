def print_numbers(num1, num2, *numbers):
    print(num1)
    print(num2)
    print(numbers)

def color(red, blue, green, **colors):

    print(f"r = {red}")
    print(f"b = {blue}")
    print(f"g = {green}")
    print(colors)

class Car():

    def __init__(self, brand, wheels, year, color):

        self._brand = brand
        self._wheels = wheels
        self._year = year
        self._color = color

    def get_car_details(self):

        print(f"{self._brand} {self._color} car from {self._year}")



if __name__ == "__main__":


    print("unpacking tuple as args")

    t = (1,2,3,4,5,6,7)

    print_numbers(*t)


    print("Unpacking map types as kwargs")

    k = {'red': 1, 'blue': 2, 'green': 3, 'cyan': 4, 'purple': 5}

    color(**k)
    
    print("For classes")

    k_car = {"brand": "BMW", "wheels": 4, "year": 2004, "color": "blue"}

    car = Car(**k_car)

    car.get_car_details()
