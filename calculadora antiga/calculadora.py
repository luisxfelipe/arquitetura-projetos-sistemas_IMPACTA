def calculate():
    operation = input('''
Por favor, selecione o operador que deseja utilizar na calculadora:
+ Adição
- Subtração
* Multiplicação
/ Divisão
''')


#Uma classe depende da outra para funcionar, no caso um exemplo de acoplamento e coesão.
    number_1 = int(input('Primeiro número: '))
    number_2 = int(input('Segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, reinicie o programa')

        # add a função again() para função calculate()
    again()

def again():
    calc_again = input('''
Deseja utilizar a calculadora novamente?
Digite Y para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('até logo.')
    else:
        again()

calculate()
