import sys
import time

from Calculadora.Calculator import Calculator
from Exceptions import InvalidExpression


class Console:
    def __init__(self):
        self.calculadora = Calculator()
        self.option: int = None
        self.SCRIPT = '-'

    def start(self):
        self.mainMenu()


    @staticmethod
    def reglas():
        print('- Si las operaciones llevan paréntesis, corchetes o llaves, estos deben estar completos, de lo contrario la calculadora podría presentar un error')
    def opciones(self):
        print('1. Para iniciar la calculadora')
        print('2. Mostrar reglas de calculadora')
        print('3. Para salir')

    def mainMenu(self):
        while True:
            print(self.SCRIPT * 39)
            print(' B - I - E - N - V - E - N - I - D - O')
            print(self.SCRIPT * 39)
            self.opciones()
            try:
                self.option = int(input("INGRESE SU OPCION: "))
            except InvalidExpression as e:
                print(f'Ingrese una opción válida: {e}')

            if self.option == 1:
                ecuacion = str(input('Ingrese su ecuación: '))
                print('Resultado: ', self.calculadora.operar(ecuacion))
                time.sleep(5)
            elif self.option == 2:
                self.reglas()
                time.sleep(5)
            elif self.option == 3:
                sys.exit()



console = Console()
console.start()
