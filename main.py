from convertir_Numero import *
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from operaciones import operacion

ConvertidorTexto = ConvertidorTexto()

class calculadoraGUI(QMainWindow):
    def __init__(self):
        super() .__init__()
        uic.loadUi("Calculadora.ui",self)

        self.btn1.clicked.connect(self.uno)
        self.btn2.clicked.connect(self.dos)
        self.btn3.clicked.connect(self.tres)
        self.btn4.clicked.connect(self.cuatro)
        self.btn5.clicked.connect(self.cinco)
        self.btn6.clicked.connect(self.seis)
        self.btn7.clicked.connect(self.siete)
        self.btn8.clicked.connect(self.ocho)
        self.btn9.clicked.connect(self.nueve)
        self.btn0.clicked.connect(self.cero)

        self.btnborrar.clicked.connect(self.borrar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        self.btnsigno.clicked.connect(self.cambiarSigno)

        self.btnmas.clicked.connect(self.suma)
        self.btnmenos.clicked.connect(self.resta)
        self.btnmult.clicked.connect(self.multiplicacion)
        self.btndiv.clicked.connect(self.division)
        self.btnigual.clicked.connect(self.igual)
        self.btnmax.clicked.connect(self.maximo)
        self.btnmin.clicked.connect(self.minimo)
        self.btnsen.clicked.connect(self.seno)
        self.btncos.clicked.connect(self.coseno)
        self.btntan.clicked.connect(self.tangente)
        self.btnprom.clicked.connect(self.promedio)

    def uno(self):
        self.agregar_numero("1")

    def dos(self):
        self.agregar_numero("2")

    def tres(self):
        self.agregar_numero("3")

    def cuatro(self):
        self.agregar_numero("4")

    def cinco(self):
        self.agregar_numero("5")

    def seis(self):
        self.agregar_numero("6")

    def siete(self):
        self.agregar_numero("7")

    def ocho(self):
        self.agregar_numero("8")

    def nueve(self):
        self.agregar_numero("9")

    def cero(self):
        self.agregar_numero("0")

    def borrar(self):
        texto = self.label_result.text()
        self.label_result.setText(texto[:-1])
        self.label_text.setText("")

    def limpiar(self):
        self.label_result.setText("")
        self.label_operador.setText("")
        self.label_text.setText("")

    def suma(self):
        self.insertarOperador("+")

    def resta(self):
        self.insertarOperador("-")

    def multiplicacion(self):
        self.insertarOperador("*")

    def division(self):
       self.insertarOperador("/")

    def maximo(self):
        self.insertarOperador("MAX")

    def minimo(self):
        self.insertarOperador("MIN")

    def seno(self):
        self.realizarOperacion("sen")
        self.igual()

    def coseno(self):
        self.realizarOperacion("cos")
        self.igual()

    def tangente(self):
        self.realizarOperacion("tan")
        self.igual()

    def cambiarSigno(self):
        texto = self.label_operador.text()
        self.label_result.setText("-" + texto)

    def promedio(self):
      self.insertarOperador("PROM")

    def igual(self):
        operacion.num02 = float(self.label_result.text())
        if str(operacion.num02)[-2:] == ".0":
            operacion.num02 = int(operacion.num02)
        resultado = operacion.operar()
        self.label_result.setText(str(resultado))
        self.label_operador.setText("")
        self.label_text.setText(ConvertidorTexto.convertir_a_texto(resultado))
        self.label_text.setWordWrap (True)

    def realizarOperacion(self,operador):
        if operador=="MAX" or operador=="MIN":
            texto = self.label_result.text()
            operacion.num01 = int(texto)
            if str(operacion.num01)[-2:] == ".0":
                operacion.num01 = int(operacion.num01)
            self.label_result.setText("0")
            operacion.operador = operador
        elif operador == "sen" or operador == "cos" or operador == "tan":
            texto = self.label_result.text()
            self.label_operador.setText(operador + "(" + texto + ") ")
            operacion.num01 = float(texto)
            if str(operacion.num01)[-2:] == ".0":
                operacion.num01 = int(operacion.num01)
            self.label_result.setText("0")
            operacion.operador = operador
    
    def insertarOperador(self,operador):
        texto = self.label_result.text()
        self.label_operador.setText(texto + " " + operador + " ")
        operacion.num01 = float(texto)
        if str(operacion.num01)[-2:] == ".0":
            operacion.num01 = int(operacion.num01)
        self.label_result.setText("0")
        operacion.operador = operador
    
    def agregar_numero(self, numero):
        texto = self.label_result.text()
        if len(texto)<10:
            if self.label_result.text()=="0":
                self.label_result.setText(numero)
            else:
                self.label_result.setText(texto+numero)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = calculadoraGUI()
    ui.show()
    sys.exit(app.exec_())