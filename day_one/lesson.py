

class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color):
        self.color = new_color


class Car(Transport):
    wheels_count = 4  # attribute of class

    def __init__(self, model, year, color, penalties=0):
        super().__init__(model, year, color)
        self.penalties = penalties

    def drive(self, city):
        print(f'\nCar {self.model} is driving to {city}')


class Truck(Car):
    wheels_count = 4

    def __init__(self, model, year, color, penalties=0, load_capacity=0):
        super().__init__(model, year, color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, the_type, weight):
        if weight > self.load_capacity:
            print(f'Can not load cargo more than {self.load_capacity}')
        else:
            print(f'Cargo of {the_type} {weight} was successfully loaded on truck')


class Plane(Transport):
    def __init__(self, model, year, color,):
        super().__init__(model, year, color)


bmw_car = Car('BMW M5 E90', 2020, 'Orange')

print('bmw_car', bmw_car)


def show_object(car_model: Transport) -> None:
    print(
        f'\nModel={car_model.model}\n'
        f'Year={car_model.year}\n'
        f'Color={car_model.color}\n'
    )


show_object(bmw_car)

nissan_car = Car(model='Nissan GTR R34', year=2000, color='Black', penalties=900)

show_object(nissan_car)

nissan_car.drive('Bishkek')

bmw_car.drive('Dubai')

# nissan_car.color = 'White'
nissan_car.change_color('White')

show_object(nissan_car)

print(f'We need: {Car.wheels_count * 10 * 5000} soms for winter lastics')

Car.wheels_count = 5

print(f'We need: {Car.wheels_count * 10 * 5000} soms for winter lastics')

boing_plane = Plane('Boeing 737', 2022, 'Blue')

show_object(boing_plane)

man_truck = Truck(model='Man 60', year=2009, color='Black', penalties=1000, load_capacity=25000)

show_object(man_truck)

# man_truck.load_cargo('Apple', 30000)

man_truck.change_color('Brown')

show_object(man_truck)

man_truck.drive('London')

print(f'{Truck.wheels_count}')
