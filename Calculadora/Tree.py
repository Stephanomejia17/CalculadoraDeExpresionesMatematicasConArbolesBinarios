class Node:
    def __init__(self, value=None, right_child=None, left_child=None) -> None:
        self.value = value
        self.left_child: Node = left_child
        self.right_child: Node = right_child

    def __str__(self) -> str:
        return f"Value: {self.value}, Left Child: {self.left_child}, Right Child: {self.right_child}"

    def setValue(self, value):
        self.value = value

    def setLeftChild(self, value):
        self.left_child = value

    def setRightChild(self, value):
        self.right_child = value


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    #  Insertar elementos al arbol
    def insert(self, node: Node, value: str):
        if self.root is None:
            self.root = Node(value=value)
        else:
            if node.left_child is None:
                node.left_child = Node(value=value)
            elif node.right_child is None:
                node.right_child = Node(value=value)
            else:
                pass

    #  Hacer operaciones para los nodos hojas
    def evaluar_arbol(self, node):
        if node is None:
            return 0

        if node.left_child is None and node.right_child is None:  # La recursión llegó a un nodo hoja (número)
            return int(node.value)

        # Llamados recursivos
        left_val = self.evaluar_arbol(node.left_child)
        right_val = self.evaluar_arbol(node.right_child)

        #  Evaluación del nodo principal y operación
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val

    # Imprimir arbol
    def print(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right_child:
            self.print(node.right_child, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left_child:
            self.print(node.left_child, prefix + ("    " if is_left else "│   "), True)


