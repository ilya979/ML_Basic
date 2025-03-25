from base import Vehicle
from car import Car
from exceptions import CarNotStarted, LowFuelError, NotEnoughFuel, CargoOverload
from engine import Engine
from plane import Plane

print("vehicle")
try:
    vehicle = Vehicle(1200, 50, 10)
    vehicle.start()
    vehicle.move(100)
except LowFuelError:
    print("Мало топлива")
except NotEnoughFuel:
    print("Типлива не достаточно для поездки")
except CargoOverload:
    print("Машина перегружена")
except CarNotStarted:
    print("Машина не заведена")
finally:
    print(vehicle)

try:
    print("vehicle2")
    vehicle2 = Vehicle(1200, 50, 10)
    vehicle2.start()
    vehicle2.move(1000)
except LowFuelError:
    print("Мало топлива")
except NotEnoughFuel:
    print("Типлива не достаточно для поездки")
except CargoOverload:
    print("Машина перегружена")
except CarNotStarted:
    print("Машина не заведена")
finally:
    print(vehicle2)

print("vehicle3")
try:
    vehicle3 = Vehicle(1200, 50, 10)
    # vehicle3.start()
    vehicle3.move(100)
except LowFuelError:
    print("Мало топлива")
except NotEnoughFuel:
    print("Типлива не достаточно для поездки")
except CargoOverload:
    print("Машина перегружена")
except CarNotStarted:
    print("Машина не заведена")
finally:
    print(vehicle3)

engine = Engine(100, 2)
car = Car()
car.set_engine(engine)

print(car)

plane = Plane(10000, 1000, 100, 10000)

try:
    print("plane")
    plane.start()
    plane.move(1000)
    plane.load_cargo(5000)
    plane.load_cargo(4000)
except LowFuelError:
    print("Мало топлива")
except NotEnoughFuel:
    print("Типлива не достаточно для поездки")
except CargoOverload:
    print("Машина перегружена")
except CarNotStarted:
    print("Машина не заведена")
finally:
    print(plane)

try:
    print("plane")
    plane.load_cargo(5000)
    plane.load_cargo(4000)
except LowFuelError:
    print("Мало топлива")
except NotEnoughFuel:
    print("Типлива не достаточно для поездки")
except CargoOverload:
    print("Машина перегружена")
except CarNotStarted:
    print("Машина не заведена")
finally:
    print(plane)

print(f"cur.cargo: {plane.remove_all_cargo()}")

try:
    print("plane")
    plane.load_cargo(5000)
    plane.load_cargo(4000)
except LowFuelError:
    print("Мало топлива")
except NotEnoughFuel:
    print("Типлива не достаточно для поездки")
except CargoOverload:
    print("Машина перегружена")
except CarNotStarted:
    print("Машина не заведена")
finally:
    print(plane)
