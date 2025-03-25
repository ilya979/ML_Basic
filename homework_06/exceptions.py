__all__ = [
    "LowFuelError",
    "NotEnoughFuel",
    "CargoOverload",
    "CarNotStarted"
]

class LowFuelError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return(f"LowFuelError")

class NotEnoughFuel(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return(f"NotEnoughFuel")


class CargoOverload(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return(f"CargoOverload")

class CarNotStarted(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return(f"CarNotStarted")
