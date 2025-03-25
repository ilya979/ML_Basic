"""
create dataclass `Engine`
"""

__all__ = [
    "Engine"
]

class Engine:
    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons

    def __str__(self):
        return f"Engine: {self.pistons}, {self.volume}"