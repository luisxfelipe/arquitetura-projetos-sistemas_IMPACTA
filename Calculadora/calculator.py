'''
Coesão:
- Calculator:
    O código da classe Calculator atende ao principio de coesão, 
    pois o objetivo da classe Calculator é realizar calculos e
    todos os metodos existentes na classe servem para fazer um 
    tipo de operação matemática. Dessa forma a classe só tem a 
    função de realizar calculos e cada função faz apenas a operação
    requisitada

'''
'''
Acoplamento:
    O programa no geral tem o minimo de acoplamento possivel, visto que 
    na classe Calculator nenhum método depende do outro para funcionar 
    e a própria classe não depende de nenhuma outra classe ou módulo do
    sistema para funcionar.
'''

'''
Princípios SOLID:
- Single Responsability Principle:
    O programa atende ao primeiro principio SOLID, pois a classe 
    calculator tem apenas a responsabilidade de fazer calculos e cada um
    de seus metódos tem apenas a responsabilidade de fazer a operação 
    desejada

- Open/Closed Principle:
    O programa atende ao segundo princípio SOLID, pois se necessario a 
    adição de novas operações matemáticas não será necessário alterar as
    demais, visto que elas não estão acopladas. Então pode-se considerar 
    que a classe está aberta para extensão e fechado para modificação
'''

class Calculator:

    def __init__(self, number_one: float, number_two: float) -> None:
        
        self.__number_one = number_one
        self.__number_two = number_two

    def sum(self) -> float:

        return self.__number_one + self.__number_two       
            
    def subtract(self) -> float:
        
        return self.__number_one - self.__number_two

    def multiplication(self) -> float:
        return self.__number_one * self.__number_two

    def division(self) -> float:

        try:
            return self.__number_one / self.__number_two
        except ZeroDivisionError:
            return 'Não é possivel realizar divisão de um número por 0'
        
  


