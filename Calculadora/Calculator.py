from Exceptions import InvalidExpression
from Tree import BinaryTree
from Tree import Node


class Calculator:
    def __init__(self):
        self.operatorsPriority = {'+': 1, '-': 1, '/': 2, '*': 2}
        self.operadores = {'+', '-', '*', '/'}
        self.tree = BinaryTree()

    def shunting_yard(self, expression):
        pila = []  # Pila para operadores y paréntesis
        salida = []  # Lista para la salida en notación postfija
        number = ''  # String temporal para acumular números de más de un dígito

        for token in expression.replace(" ", ""):  # Elimina los espacios y itera sobre cada carácter de la expresión
            if token.isdigit():
                number += token  # Acumula dígitos en la variable number
            else:
                if number:
                    salida.append(number)  # Agrega el número acumulado a la salida
                    number = ''  # Reinicia la variable number
                if token in self.operadores:
                    while (pila and pila[-1] in self.operadores and
                           self.operatorsPriority[pila[-1]] >= self.operatorsPriority[token]):
                        salida.append(pila.pop())  # Mueve operadores de la pila a la salida según la prioridad
                    pila.append(token)  # Agrega el operador actual a la pila
                elif token == '(':
                    pila.append(token)  # Agrega un paréntesis izquierdo a la pila
                elif token == ')':
                    while pila and pila[-1] != '(':
                        salida.append(
                            pila.pop()) # Mueve operadores del stack a la salida hasta encontrar un paréntesis izquierdo
                    pila.pop()  # Elimina el paréntesis izquierdo de la pila

        if number:
            salida.append(number)  # Agrega el último número acumulado si hay alguno

        while pila:
            salida.append(pila.pop())  # Mueve los operadores restantes de la pila a la salida

        return salida  # Retorna la expresión en notación postfija

    def construir_arbol(self, ecuacion):
        stack = []
        for n in ecuacion:
            if n.isdigit():
                stack.append(Node(value=n))  # Si el valor del nodo es un numero, entonces lo agrega al stack
            else:
                node = Node(value=n)  # Si es un operador crea el nodo respectivo
                #  Agrega los numeros como hijos del nuevo nodo (operador)
                node.right_child = stack.pop()
                node.left_child = stack.pop()
                stack.append(node)

        self.tree.root = stack.pop()
        return self

    def operar(self, ecuacion):
        #  Llamados de las funciones para realizar la operación
        res = self.shunting_yard(ecuacion)
        self.construir_arbol(res)
        return self.tree.evaluar_arbol(self.tree.root)
