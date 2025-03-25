"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CarNotStarted, LowFuelError, NotEnoughFuel, CargoOverload

class Plane(Vehicle):
    _cargo = 0
    _max_cargo = 2000
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self._max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        if self._cargo + add_cargo > self._max_cargo:
            raise CargoOverload
        else:
            self._cargo = self._cargo + add_cargo

    def remove_all_cargo(self):
        cur_cargo = self._cargo
        self._cargo = 0
        return cur_cargo
    
    def __str__(self):
        return f"Plane: max.cargo: {self._cargo}, cur.cargo:{self._cargo}"

    

