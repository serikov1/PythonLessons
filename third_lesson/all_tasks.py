# 1 2 4 5
#class Car:
#     def __init__(self, capacity, speed, number):
#         self.capacity = capacity
#         self.speed = speed
#         self.number = number
#
#     def __str__(self):
#         return f'<Car capacity:{self.capacity} speed:{self.speed} number:{self.number}>'
#
#     def __eq__(self, other):
#         if isinstance(other, Car):
#             return self.number == other.number
#         return False
#
#     def __hash__(self):
#         return hash(self.number)
#
#
# # Причём a и c - одна и та же машина с точки зрения сравнения
# a = Car(100, 100, "asd")
# b = Car(100, 100, "zzz")
# c = Car(200, 50, "asd")
#
# # Эти не равны
# print(a == b)
# # Эти равны
# print(a == c)
#
# # А эта пара примеров должна не упасть
# # и корректно сказать, что машина не равна ни None, ни целому числу
# print(a == None)
# print(a == 1)
#
# # Попробуем сложить машины в set
# s = set()
# s.add(a)
# s.add(b)
# s.add(c)
# s.add(a)
# s.add(a)
#
# # Ожидаем увидеть номера двух машин,
# # так как всё остальное в описанной логике является дублями
# print("=== Cars in set ===")
# for z in sorted(s, key=lambda e: e.number):
#     print(z.number)
#
# class RaceCar(Car):
#     def __init__(self, speed):
#         self.capacity = 0
#         self.number = None
#         self.speed = speed
#
#
# c = Car(1000, 100, "a720po")
# print(c.capacity, c.speed, c.number)
# r = RaceCar(300)
# print(r.capacity, r.speed, r.number)


#3
# class MoneyBox:
#     def __init__(self):
#         self.box = 0
#         self.amount = 0
#
#     def add_coin(self, value):
#         self.box += 1
#         self.amount += value
#
#     def get_coins_number(self):
#         return self.box
#
#     def get_coins_value(self):
#         return self.amount
#
#
# m = MoneyBox()
#     # Добавили монетку достоинством 10
# m.add_coin(10)
#     # Добавили монетку достоинством 5
# m.add_coin(5)
#     # Ожидаем, что монеток внутри 2 штуки
# print(m.get_coins_number())
#     # Ожидаем, что общее достоинство всех монеток 15
# print(m.get_coins_value())


#6
class Garage:
    def __init__(self):
        self.cars = []

    def park(self, v):
        self.cars.append(v)

    def count(self, t):
        amount = 0
        for car in self.cars:
            if isinstance(car, t):
                amount += 1
        return amount

    def get_fastest_of_type(self, t):
        fastest_car = 0
        for car in self.cars:
            if isinstance(car, t) and (fastest_car == 0 or fastest_car.speed < car.speed):
                fastest_car = car
        return fastest_car

class Car:
    def __init__(self, c, s, n):
        self.capacity = int(c)
        self.speed = int(s)
        self.number = n

# Грузовик
class Truck(Car):
    pass

# Автобус
class Bus(Car):
    pass

# Создаём гараж
g = Garage()
# Паркуем машины
g.park(Car(1, 100, "abc"))
g.park(Truck(1000, 150, "zzz"))
g.park(Bus(100, 50, "QWE"))
g.park(Bus(100, 80, "ASD"))
g.park(Bus(100, 20, "ZXC"))

# Сколько всего машин? Ожидаем 5, потому что грузовик и автобус - тоже машины.
print(g.count(Car))
# Сколько всего грузовиков? Ожидаем 1.
print(g.count(Truck))
# Сколько всего автобусов? Ожидаем 3.
print(g.count(Bus))
# Получим самую быструю машину и выведем её номер. Ожидаем zzz, потому что грузовик внезапно самый быстрый.
print(g.get_fastest_of_type(Car).number)
# Получим самый быстрый грузовик и выведем его номер. Ожидаем zzz.
print(g.get_fastest_of_type(Truck).number)
# Получим самый быстрый автобус и выведем его номер. Ожидаем ASD.
print(g.get_fastest_of_type(Bus).number)