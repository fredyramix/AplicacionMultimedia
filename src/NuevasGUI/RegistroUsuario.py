
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import MenuUsuario

class RegistroUsuario(QtGui.QWidget):
    def __init__(self):
        super(RegistroUsuario, self).__init__()
        self.children = []
        self.iptNombre = QtGui.QLineEdit(self)
        self.iptApaterno = QtGui.QLineEdit(self)
        self.iptAmaterno = QtGui.QLineEdit(self)
        self.iptCorreoE = QtGui.QLineEdit(self)
        self.iptEdad = QtGui.QLineEdit(self)
        self.iptSemestre = QtGui.QLineEdit(self)
        self.initUI()

    def initUI(self):
        tamHorizontal = 350
        tamVertical = 300
        self.setFixedSize(tamHorizontal, tamVertical)
        self.setWindowTitle('Registra Usuario')
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))

        marginLeftLbl = 22
        contTopLbl = 25
        marginLeftIpt = 100
        sizeIpt = 200

        # Nombre
        lblNombre = QtGui.QLabel('Nombre:', self)
        lblNombre.move(marginLeftLbl, contTopLbl)
        self.iptNombre.setMinimumWidth(sizeIpt)
        self.iptNombre.move(marginLeftLbl + marginLeftIpt, contTopLbl)
        contTopLbl += 35

        # Apellido Paterno
        lblApaterno = QtGui.QLabel('Apellido Paterno:', self)
        lblApaterno.move(marginLeftLbl, contTopLbl)
        self.iptApaterno.setMinimumWidth(sizeIpt)
        self.iptApaterno.move(marginLeftLbl + marginLeftIpt, contTopLbl)
        contTopLbl += 35

        # Apellido Materno
        lblAmaterno = QtGui.QLabel('Apellido Materno:', self)
        lblAmaterno.move(marginLeftLbl, contTopLbl)
        self.iptAmaterno.setMinimumWidth(sizeIpt)
        self.iptAmaterno.move(marginLeftLbl + marginLeftIpt, contTopLbl)
        contTopLbl += 35

        # e-mail
        lblCorreoE = QtGui.QLabel(u'Correo electrónico:', self)
        lblCorreoE.move(marginLeftLbl, contTopLbl)
        self.iptCorreoE.setMinimumWidth(sizeIpt)
        self.iptCorreoE.move(marginLeftLbl + marginLeftIpt, contTopLbl)
        contTopLbl += 35

        # Edad
        lblEdad = QtGui.QLabel(u'Edad:', self)
        lblEdad.move(marginLeftLbl, contTopLbl)
        self.iptEdad.setMinimumWidth(sizeIpt)
        self.iptEdad.move(marginLeftLbl + marginLeftIpt, contTopLbl)
        contTopLbl += 35

        # Semestre
        lblSemestre = QtGui.QLabel(u'Semestre:', self)
        lblSemestre.move(marginLeftLbl, contTopLbl)
        self.iptSemestre.setMinimumWidth(sizeIpt)
        self.iptSemestre.move(marginLeftLbl + marginLeftIpt, contTopLbl)

        btnAceptar = QtGui.QPushButton('Ingresar', self)
        btnAceptar.clicked.connect(self.ingresarUsuario)
        tamHorizontalBtn = 100
        tamVerticalBtn = 35
        btnAceptar.setMinimumSize(tamHorizontalBtn, tamVerticalBtn)
        btnAceptar.move(tamHorizontal - tamHorizontalBtn - 10, tamVertical - tamVerticalBtn - 10)
        
        self.show() 
    
    def ingresarUsuario(self):
        nombre = str((self.iptNombre.text()).toAscii())
        aPaterno = str((self.iptApaterno.text()).toAscii())
        aMaterno = str((self.iptAmaterno.text()).toAscii())
        correoE = str((self.iptCorreoE.text()).toAscii())
        edad = str((self.iptEdad.text()).toAscii())
        semestre = str((self.iptSemestre.text()).toAscii())

        
        datos = nombre + " " + aPaterno + " " + aMaterno + " " + correoE + " " + edad + " " + semestre
        archivo = nombre + "_" + aPaterno + "_" + aMaterno
        nuevaVentana = MenuUsuario.MenuUsuario(name=datos,archivo=archivo)
        self.children.append(nuevaVentana)
        self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    main_window = RegistroUsuario()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()