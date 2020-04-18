from calculator import Calculator

class Square(Calculator):
    
    def __init__(self, base:float):
        self.__base = base

    def calculate(self) -> float:
        return float("%.2f" % self.__base ** 2)