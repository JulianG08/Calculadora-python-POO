import psycopg2

class Operacion:
    num01 = ""
    operacion = ""
    num02 = ""

    def __init__(self, num01, operacion, num02):
        self.num01 = num01
        self.operacion = operacion
        self.num02 = num02

    def suma(self, num01, num02):
        return num01 + num02
    
    def resta(self, num01, num02):
        return num01 - num02
    
    def multiplicacion(self, num01, num02):
        return num01 * num02
    
    def division(self, num01, num02):
        return num01 / num02