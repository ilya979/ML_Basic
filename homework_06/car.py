"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle

class Car(Vehicle):
    def __init__(self):
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine

    def __str__(self):
        return f"Car: {self._weight}, {self._fuel}, {self.engine}"
