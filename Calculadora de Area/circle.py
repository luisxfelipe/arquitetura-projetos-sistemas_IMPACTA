from calculator import Calculator

class Circle(Calculator):

    def __init__(self, radius:float):
        self.__radius = radius

    def calculate(self) -> float:
        return float("%.2f" % (3.14*(self.__radius ** 2)))       
         