# Calculadora de Expresiones Matemáticas 

*Objetivo*: Desarrollar una calculadora de expresiones matemáticas utilizando árboles binarios de expresión. La calculadora debe ser capaz de evaluar expresiones matemáticas ingresadas como cadenas de texto, manejar errores sintácticos y devolver el resultado o el tipo de error encontrado.

*Descripción*: Implementa un sistema de consola básico que transforme una expresión matemática, dada en formato de texto, en un árbol binario de expresión para realizar la evaluación. Cada nodo debe representar un operador (como +, -, *, /) o un operando (un número). La calculadora debe gestionar correctamente las operaciones según las reglas de precedencia, así como manejar paréntesis y operadores con diferentes prioridades.

*Funcionalidades*:

* Entrada de Expresión: El programa debe permitir al usuario ingresar una expresión matemática como cadena de texto (e.g., "5 + 6 - 3 * 3" o "(5 + 4) * 3 / (4 + 2)").
* Árbol de Expresión: La expresión debe convertirse en un árbol binario, donde cada nodo representa un operador o un operando. El árbol se debe construir teniendo en cuenta la precedencia de los operadores y respetando el uso de paréntesis.
* Evaluación de Expresiones: Implementar un método para evaluar el árbol de expresión, recorriéndolo y aplicando las operaciones en el orden correcto para obtener el resultado final.
* Errores Sintácticos: El programa debe identificar y reportar errores comunes, como paréntesis desbalanceados, operadores u operandos faltantes, operadores consecutivos o caracteres no permitidos.
* Espacios en Blanco: La expresión debe poder manejar espacios en blanco entre números y operadores.

*Ejemplo de Entrada*:

* "5 + 6 - 3 * 3"
* "(5 + 4) * 3 / (4 + 2)"

*Ejemplo de Salida*:

* Resultado: 2.0 para "5 + 6 - 3 * 3"
* Resultado: 4.5 para "(5 + 4) * 3 / (4 + 2)"

*Ejemplo de Errores*:

*"5 + * 3" debería producir Error*: operador faltante entre dos operandos
*"((5 + 2) * 3" debería producir Error*: paréntesis desbalanceados