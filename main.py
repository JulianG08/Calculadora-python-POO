from operaciones import *
from convertir__Numero import *

if __name__ == '__main__':
    operacion1 = Operacion("", "", "")
    num01 = int(input("Digite un numero: ")[0:10])
    #num02 = int(input("Digite otro numero: ")[0:10])
    print(operacion1.seno(num01))
    print(numeros_a_palabras(operacion1.seno(num01)))