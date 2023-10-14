import math

class Operaciones:
    num01 = -23685320324598643120
    operador = ""
    num02 = -23685320324598643120
    vector = []

    def __init__(self, num01 = -23685320324598643120, operador = "", num02 = -23685320324598643120, vector = []):
        self.num01 = num01
        self.operador = operador
        self.num02 = num02
        self.vector = vector

    def operar(self):
        if self.operador == "+":
            resultado = self.num01 + self.num02
            return resultado
        elif self.operador == "-":
            resultado = self.num01 - self.num02
            return resultado
        elif self.operador == "*":
            resultado = self.num01 * self.num02
            return resultado
        elif self.operador == "/":
            resultado = self.num01 / self.num02
            return resultado
        elif self.operador == "sen":
            grado = (self.num01*math.pi)/180
            resultado = math.sin(grado)
            return resultado
        elif self.operador == "cos":
            grado = (self.num01*math.pi)/180
            resultado = math.cos(grado)
            return resultado
        elif self.operador == "tan":
            grado = (self.num01*math.pi)/180
            resultado = math.tan(grado)
            return resultado
        elif self.operador == "MAX":
            resultado = max(self.num01, self.num02)
            return int(resultado)
        elif self.operador == "MIN":
            resultado = min(self.num01, self.num02)
            return int(resultado)
        elif self.operador == "PROM":
            resultado = (self.num01 + self.num02)/2
            return resultado

operacion = Operaciones()