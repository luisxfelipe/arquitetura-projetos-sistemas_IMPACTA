from calculator import Calculator

class Cube(Calculator):

    def __init__(self, edge:float):
        self.__edge = edge

    def calculate(self) -> float:
        return float("%.2f" % (6 * (self.__edge ** 2)))