class Car:
    '''Продаем автомобиль'''

    def __init__(self, model, year_of_manufacture, engine_size, price, mileage):
        '''Инициализация параметров автомобиля'''
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.engine_size = engine_size
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description_car(self):
        '''Получение описания автомобиля'''
        if self.wheels > 4:
            w = "с"
        else:
            w = "са"
        if self.engine_size > 4:
            l = "ов"
        else:
            l = "а"
        description = self.model + ", " + str(self.year_of_manufacture) + " года выпуска, объем двигателя " + str(
            self.engine_size) \
                      + f' литр{l}' + ", стоимостью " + str(self.price) + "$, пробег " + str(
            self.mileage) + "тыс. км, имеет " \
                      + str(self.wheels) + f' коле{w}'
        print(description)

    def update_wheels(self, num_wheels):
        self.wheels = num_wheels


class Truck(Car):
    '''Продаем грузовик'''

    def __init__(self, model, year_of_manufacture, engine_size, price, mileage):
        '''Инициализация параметров грузовика'''
        super().__init__(model, year_of_manufacture, engine_size, price, mileage)


car = Car('BMW X7', 2019, 3, 102000, 48000)
car.description_car()
print()
truck = Truck('DAF XF 105', 2008, 13, 74600, 100000)
truck.update_wheels(8)
truck.description_car()


