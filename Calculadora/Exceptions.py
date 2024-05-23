class InvalidExpression(Exception):
    def __init__(self, mensaje="Expresión ingresada inválida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)