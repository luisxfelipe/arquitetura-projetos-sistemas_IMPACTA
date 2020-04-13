from calculator import Calculator
from calculator_manager import CalculatorManager

def interactWithUser() -> str:

    number_one = None
    number_two = None
    calculationResult = None
    disableFunctionality = None
    enableFunctionality = None
    execution = True
    again = None
    
    calculatorManagerObject = CalculatorManager()

    while execution == True:

        again = None
        
        print('\nOpções: ')
        print('\n1 - Realizar operação matemática')
        print('2 - Desabilitar funcionalidade')
        print('3 - Habilitar funcionalidade')

        desiredAction = input('\nDigite o número correspondente a ação desejada: ')

        if desiredAction == '1':

            number_one = float(input("\nDigite o 1º número da operação: "))

            print('\nOpções: ')
            print('\n+ Adição')
            print('- Subtração')
            print('* Multiplicação')
            print('/ Divisão')

            desiredOperation = input('\nDigite o simbolo correspondente a operação desejada: ')

            number_two = float(input("\nDigite o 2º número da operação: "))

            calculationResult = calculatorManagerObject.calculate(number_one, number_two, desiredOperation)

            if type(calculationResult) == float:
                print(f'\n{number_one} {desiredOperation} = {calculationResult}')
            elif type(calculationResult) == str:
                print(f'\n{calculationResult}')

        elif desiredAction ==  '2':

            print('\nOpções: ')
            print('\n1 - Desabilitar completamente a calculadora')
            print('2 - Desabilitar a funcionalidade somar da calculadora')
            print('3 - Desabilitar a funcionalidade subtrair da calculadora')
            print('4 - Desabilitar a funcionalidade multiplicar da calculadora')
            print('5 - Desabilitar a funcionalidade dividir da calculadora')

            disableFunctionality = input('\nDigite o número correspondente a funcionalidade que deseja desabilitar: ')

            if disableFunctionality == '1':
                calculatorManagerObject.changeCalculatorStatus('calculadora', False)
            elif disableFunctionality == '2':
                calculatorManagerObject.changeCalculatorStatus('somar', False)
            elif disableFunctionality == '3':
                calculatorManagerObject.changeCalculatorStatus('subtrair', False)
            elif disableFunctionality == '4':
                calculatorManagerObject.changeCalculatorStatus('multiplicar', False)
            elif disableFunctionality == '5':
                calculatorManagerObject.changeCalculatorStatus('dividir', False)
            
        elif desiredAction == '3':

            print('\nOpções: ')
            print('\n1 - Habilitar completamente a calculadora')
            print('2 - Habilitar a funcionalidade somar da calculadora')
            print('3 - Habilitar a funcionalidade subtrair da calculadora')
            print('4 - Habilitar a funcionalidade multiplicar da calculadora')
            print('5 - Habilitar a funcionalidade dividir da calculadora')

            enableFunctionality = input('\nDigite o número correspondente a funcionalidade que deseja habilitar: ')

            if enableFunctionality == '1':
                calculatorManagerObject.changeCalculatorStatus('calculadora', True)
            elif enableFunctionality == '2':
                calculatorManagerObject.changeCalculatorStatus('somar', True)
            elif enableFunctionality == '3':
                calculatorManagerObject.changeCalculatorStatus('subtrair', True)
            elif enableFunctionality == '4':
                calculatorManagerObject.changeCalculatorStatus('multiplicar', True)
            elif enableFunctionality == '5':
                calculatorManagerObject.changeCalculatorStatus('dividir', True)

        while again == None:

            print('\nDeseja executar novamente o programa?')

            again = input('\nDigite S para SIM ou N para NÃO: ')
                    
            if again.upper() == 'N':
                print("\nFim da execução...")
                execution = False
            elif again.upper() != 'S':
                again = None
        
        


interactWithUser()