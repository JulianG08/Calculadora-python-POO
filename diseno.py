import sys
import typing
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

class EjemploGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("VentanaPrincipal.ui", self)
        self.boton.clicked.connect(self.mostrarBoton)

    def mostrarBoton(self):
        print("Hola mundo")
        vara = self.vara.text()
        varb = self.varb.text()
        print(str(vara), str(varb))
        print(str(float(vara) * float(varb)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = EjemploGUI()
    gui.show()
    sys.exit(app.exec_())