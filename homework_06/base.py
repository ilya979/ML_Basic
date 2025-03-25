from abc import ABC
from exceptions import CarNotStarted, LowFuelError, NotEnoughFuel

__all__ = [
    "Vehicle"
]

class Vehicle(ABC):
    _weight = 1000
    _started = False
    _fuel = 100
    _fuel_consumption = 8

    def __init__(self, weight, fuel, fuel_consumption):
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    def start(self):
        if self._fuel > 0:
            self._started = True
        else:
            raise LowFuelError
        
    def move(self, dist):
        if not self._started:
            raise CarNotStarted
        fuel_req = dist/100 * self._fuel_consumption
        if self._fuel < dist/100 * self._fuel_consumption:
            raise NotEnoughFuel
        else:
            self._fuel = self._fuel - fuel_req

    def __str__(self):
        return f"Started: {self._started}, fuel: {self._fuel}"
