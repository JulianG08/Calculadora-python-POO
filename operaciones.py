import psycopg2
import math

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
    
    def seno(self, num01):
        return math.sin(math.radians(num01))
    
    def coseno(self, num01):
        return math.cos(math.radians(num01))
    
    def tangente(self, num01):
        return math.tan(math.radians(num01))
    
    def promedio(self, num01, num02):
        return (num01 + num02) / 2
    
    def maximo(self, num01, num02):
        if num01 < num02:
            return num02
        else:
            return num01
        
    def minimo(self, num01, num02):
        if num01 < num02:
            return num01
        else:
            return num02