from calculator import Calculator

'''
Coesão:
- CalculatorManager:
    O código da classe CalculatorManager atende ao principio de coesão, 
    pois o objetivo da classe CalculatorManager é gerenciar a classe as 
    funções da classe Calculator e todos os metodos existentes na classe 
    servem para fazer um tipo gerenciamento. Dessa forma a classe só tem 
    a função de realizar calculos e cada função faz apenas a operação
    requisitada

'''
'''
Acoplamento:
    A classe CalculatorManager esta acoplada a classe Calculator, pois
    é ela quem gerencia a classe Calculator, habilitando e desabilitando
    as funcionalidades e passando operações para a classe realizar os 
    calculos e returnar os resultados.
    As funções da classe não estão acopladas entre si e uma não depende
    da outra para funcionar, assim como a alteração de uma não causa 
    impacto na outra
'''
class CalculatorManager:

    def __init__(self):
        self.__calculatorObject = Calculator
        self.__calculatorStatus = True
        self.__sumFunctionState = True
        self.__subtractFunctionState = True
        self.__multiplicationFunctionState = True
        self.__divisionFunctionState = True
        

    def changeCalculatorStatus(self, function, state) -> None:
        
        if function == 'calculadora':
            if state == True:
                self.__calculatorStatus = True

            elif state == False:
                self.__calculatorStatus = False

        elif function == 'somar':

            if state == True:
                self.__sumFunctionState = True

            elif state == False:
                self.__sumFunctionState = False

        elif function == 'subtrair':

            if state == True:
                self.__subtractFunctionState = True

            elif state == False:
                self.__subtractFunctionState = False

        elif function == 'multiplicar':

            if state == True:
                self.__multiplicationFunctionState = True

            elif state == False:
                self.__multiplicationFunctionState = False

        elif function == 'dividir':

            if state == True:
                self.__divisionFunctionState = True

            elif state == False:
                self.__divisionFunctionState = False

    def calculate(self, number_one: float, number_two: float, arithmeticOperator: str) -> str:
        
        if self.__calculatorStatus == False:
            return 'A calculadora está temporariamente indisponivel!'
        
        elif self.__calculatorStatus == True:
        
            if arithmeticOperator == '+':

                if self.__sumFunctionState == False:
                    return 'A funcionalidade somar da calculadora está temporariamente indisponivel!'
                elif self.__sumFunctionState == True:
                    return self.__calculatorObject(number_one, number_two).sum()

            elif arithmeticOperator == '-':

                if self.__subtractFunctionState == False:
                    return 'A funcionalidade subtrair da calculadora está temporariamente indisponivel!'
                elif self.__subtractFunctionState == True:
                    return self.__calculatorObject(number_one, number_two).subtract()

            elif arithmeticOperator == '*':

                if self.__multiplicationFunctionState == False:
                    return 'A funcionalidade multiplicar da calculadora está temporariamente indisponivel!'
                elif self.__multiplicationFunctionState == True:
                    return self.__calculatorObject(number_one, number_two).multiplication()

            elif arithmeticOperator == '/':

                if self.__divisionFunctionState == False:
                    return 'A funcionalidade dividir da calculadora está temporariamente indisponivel!'
                elif self.__divisionFunctionState == True:
                    return self.__calculatorObject(number_one, number_two).division()