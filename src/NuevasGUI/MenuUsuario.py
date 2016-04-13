
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
import ReproductorMultimedia

class MenuUsuario(QtGui.QWidget):
    def __init__(self, name=None, archivo=None):
        super(MenuUsuario, self).__init__()
        self.children = []
        self.datos = name
        self.archivo = archivo
        self.initUI()
 
    def initUI(self):
        
        buttonCuestionario = QtGui.QPushButton('Realizar Cuestionario')
        buttonCuestionario.clicked.connect(self.presentarCuestionario)

        buttonContenidoMultimedia = QtGui.QPushButton('Presentar Contenido Multimedia')
        buttonContenidoMultimedia.clicked.connect(self.presentarContenidoMultimedia)

        buttonCuestionario.setMaximumSize(235, 35)
        buttonContenidoMultimedia.setMaximumSize(235, 35)

        boxVertical = QtGui.QVBoxLayout(self)
        boxVertical.addWidget(buttonCuestionario)
        boxVertical.addWidget(buttonContenidoMultimedia)

        self.setFixedSize(260, 150)
        self.setWindowTitle('Menu de Usuario')
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.show()

    def presentarContenidoMultimedia(self):
        nuevaVentana = ReproductorMultimedia.ReproductorMultimedia(name=self.datos)
        self.children.append(nuevaVentana)
        self.close()

    def presentarCuestionario(self):
        print "Cuestionario" + self.datos
