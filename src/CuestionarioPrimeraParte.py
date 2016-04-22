
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import CuestionarioSegundaParte


class CuestionarioPrimeraParte(QtGui.QWidget):

    def __init__(self, name=None, archivo=None):
        super(CuestionarioPrimeraParte, self).__init__()
        self.children = []
        self.datos = name
        self.archivo = archivo
        self.initUI()

    def initUI(self):
        x = 40
        y = 50
        t = 20
        tamHorizontal = 400
        tamVertical = 500
        preguntas = ["1.- Ser interrogado en clase", "2.-Preparar un trabajo individualmente", "3.-Preparar un trabajo en grupo", "4.-Preguntar una duda \na un profesor en clase (publico)", "5.-Preguntar una duda a un profesor fuera del salon de \nclase (en privado)", "6.-Hablar con un profesor sobre tus problemas academicos \n (en privado,  desacuerdos sobre resultados de examenes, \n demanda de orientacion)", "7.-Participar en un seminario (discusion de temas en grupos \n reducidos)",
                     "8.-Efectuar actividades de practicas", "9.-Exponer un tema en clase", "10.-Discutir problemas academicos con compañeros (en asambleas o reuniones)", "Entrar o salir del aula cuando la clase ya ha empezado", "Excesiva cantidad de materia de estudio ", "Falta de tiempo para estudiar", "Efectuar un examen oral", "Efectuar un examen escrito:", "Esperar los resultados de un examen", "Suspender un examen", "Preparar un examen inmediato"]
        respuestas = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        instr = "Instrucciones:" + "\n"
        instr += "Elige del 1 al 9, donde 1 es Poco estresante y 9 Muy estresante"

        labelInstruccion = QtGui.QLabel(instr, self)
        labelInstruccion.move(15, 10)

        labelPregunta1 = QtGui.QLabel(preguntas[0], self)
        labelPregunta1.move(x, y)

        self.comboRespuesta1 = QtGui.QComboBox(self)
        self.comboRespuesta1.addItems(respuestas)
        self.comboRespuesta1.setMinimumWidth(t)
        self.comboRespuesta1.move(x + 300, y)

        y += 40
        labelPregunta2 = QtGui.QLabel(preguntas[1], self)
        labelPregunta2.move(x, y)
        self.comboRespuesta2 = QtGui.QComboBox(self)
        self.comboRespuesta2.addItems(respuestas)
        self.comboRespuesta2.setMinimumWidth(t)
        self.comboRespuesta2.move(x + 300, y)

        y += 40
        labelPregunta3 = QtGui.QLabel(preguntas[2], self)
        labelPregunta3.move(x, y)
        self.comboRespuesta3 = QtGui.QComboBox(self)
        self.comboRespuesta3.addItems(respuestas)
        self.comboRespuesta3.setMinimumWidth(t)
        self.comboRespuesta3.move(x + 300, y)

        y += 40
        labelPregunta4 = QtGui.QLabel(preguntas[3], self)
        labelPregunta4.move(x, y)
        self.comboRespuesta4 = QtGui.QComboBox(self)
        self.comboRespuesta4.addItems(respuestas)
        self.comboRespuesta4.setMinimumWidth(t)
        self.comboRespuesta4.move(x + 300, y)

        y += 40
        labelPregunta5 = QtGui.QLabel(preguntas[4], self)
        labelPregunta5.move(x, y)
        self.comboRespuesta5 = QtGui.QComboBox(self)
        self.comboRespuesta5.addItems(respuestas)
        self.comboRespuesta5.setMinimumWidth(t)
        self.comboRespuesta5.move(x + 300, y)

        y += 40
        labelPregunta6 = QtGui.QLabel(preguntas[5], self)
        labelPregunta6.move(x, y)
        self.comboRespuesta6 = QtGui.QComboBox(self)
        self.comboRespuesta6.addItems(respuestas)
        self.comboRespuesta6.setMinimumWidth(t)
        self.comboRespuesta6.move(x + 300, y)

        y += 50
        labelPregunta7 = QtGui.QLabel(preguntas[6], self)
        labelPregunta7.move(x, y)
        self.comboRespuesta7 = QtGui.QComboBox(self)
        self.comboRespuesta7.addItems(respuestas)
        self.comboRespuesta7.setMinimumWidth(t)
        self.comboRespuesta7.move(x + 300, y)

        y += 40
        labelPregunta8 = QtGui.QLabel(preguntas[7], self)
        labelPregunta8.move(x, y)
        self.comboRespuesta8 = QtGui.QComboBox(self)
        self.comboRespuesta8.addItems(respuestas)
        self.comboRespuesta8.setMinimumWidth(t)
        self.comboRespuesta8.move(x + 300, y)

        y += 40
        labelPregunta9 = QtGui.QLabel(preguntas[8], self)
        labelPregunta9.move(x, y)
        self.comboRespuesta9 = QtGui.QComboBox(self)
        self.comboRespuesta9.addItems(respuestas)
        self.comboRespuesta9.setMinimumWidth(t)
        self.comboRespuesta9.move(x + 300, y)
        self.setFixedSize(400, 500)
        self.setWindowTitle('Primera Parte')
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        btnAceptar = QtGui.QPushButton('Siguiente', self)

        btnAceptar.clicked.connect(self.ingresarRespuestas)
        tamHorizontalBtn = 100
        tamVerticalBtn = 30
        btnAceptar.setMinimumSize(tamHorizontalBtn, tamVerticalBtn)
        btnAceptar.move(tamHorizontal - tamHorizontalBtn -
                        10, tamVertical - tamVerticalBtn - 10)
        self.show()

    def ingresarRespuestas(self):
        resp1 = str(self.comboRespuesta1.currentText())
        resp2 = str(self.comboRespuesta2.currentText())
        resp3 = str(self.comboRespuesta3.currentText())
        resp4 = str(self.comboRespuesta4.currentText())
        resp5 = str(self.comboRespuesta5.currentText())
        resp6 = str(self.comboRespuesta6.currentText())
        resp7 = str(self.comboRespuesta7.currentText())
        resp8 = str(self.comboRespuesta8.currentText())
        resp9 = str(self.comboRespuesta9.currentText())

        datos = "r1: " + resp1 + "\n"
        datos += "r2: " + resp2 + "\n"
        datos += "r3: " + resp3 + "\n"
        datos += "r4: " + resp4 + "\n"
        datos += "r5: " + resp5 + "\n"
        datos += "r6: " + resp6 + "\n"
        datos += "r7: " + resp7 + "\n"
        datos += "r8: " + resp8 + "\n"
        datos += "r9: " + resp9

        file = open(self.archivo + "PrimeraParte.txt", 'w')
        file.write(datos)
        file.close()
        nuevaVentana = CuestionarioSegundaParte.CuestionarioSegundaParte(
            name=self.datos, archivo=self.archivo)
        self.children.append(nuevaVentana)
        self.close()
