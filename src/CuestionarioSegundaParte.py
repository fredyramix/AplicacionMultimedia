
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class CuestionarioSegundaParte(QtGui.QWidget):

    def __init__(self, name=None, archivo=None):
        super(CuestionarioSegundaParte, self).__init__()
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

        labelPregunta10 = QtGui.QLabel(preguntas[0], self)
        labelPregunta10.move(x, y)
        self.comboRespuesta10 = QtGui.QComboBox(self)
        self.comboRespuesta10.addItems(respuestas)
        self.comboRespuesta10.setMinimumWidth(t)
        self.comboRespuesta10.move(x + 300, y)

        y += 40
        labelPregunta11 = QtGui.QLabel(preguntas[1], self)
        labelPregunta11.move(x, y)
        self.comboRespuesta11 = QtGui.QComboBox(self)
        self.comboRespuesta11.addItems(respuestas)
        self.comboRespuesta11.setMinimumWidth(t)
        self.comboRespuesta11.move(x + 300, y)

        y += 40
        labelPregunta12 = QtGui.QLabel(preguntas[2], self)
        labelPregunta12.move(x, y)
        self.comboRespuesta12 = QtGui.QComboBox(self)
        self.comboRespuesta12.addItems(respuestas)
        self.comboRespuesta12.setMinimumWidth(t)
        self.comboRespuesta12.move(x + 300, y)

        y += 40
        labelPregunta13 = QtGui.QLabel(preguntas[3], self)
        labelPregunta13.move(x, y)
        self.comboRespuesta13 = QtGui.QComboBox(self)
        self.comboRespuesta13.addItems(respuestas)
        self.comboRespuesta13.setMinimumWidth(t)
        self.comboRespuesta13.move(x + 300, y)

        y += 40
        labelPregunta14 = QtGui.QLabel(preguntas[4], self)
        labelPregunta14.move(x, y)
        self.comboRespuesta14 = QtGui.QComboBox(self)
        self.comboRespuesta14.addItems(respuestas)
        self.comboRespuesta14.setMinimumWidth(t)
        self.comboRespuesta14.move(x + 300, y)

        y += 40
        labelPregunta15 = QtGui.QLabel(preguntas[5], self)
        labelPregunta15.move(x, y)
        self.comboRespuesta15 = QtGui.QComboBox(self)
        self.comboRespuesta15.addItems(respuestas)
        self.comboRespuesta15.setMinimumWidth(t)
        self.comboRespuesta15.move(x + 300, y)

        y += 70
        labelPregunta16 = QtGui.QLabel(preguntas[6], self)
        labelPregunta16.move(x, y)
        self.comboRespuesta16 = QtGui.QComboBox(self)
        self.comboRespuesta16.addItems(respuestas)
        self.comboRespuesta16.setMinimumWidth(t)
        self.comboRespuesta16.move(x + 300, y)

        y += 40
        labelPregunta17 = QtGui.QLabel(preguntas[7], self)
        labelPregunta17.move(x, y)
        self.comboRespuesta17 = QtGui.QComboBox(self)
        self.comboRespuesta17.addItems(respuestas)
        self.comboRespuesta17.setMinimumWidth(t)
        self.comboRespuesta17.move(x + 300, y)

        y += 40
        labelPregunta18 = QtGui.QLabel(preguntas[8], self)
        labelPregunta18.move(x, y)
        self.comboRespuesta18 = QtGui.QComboBox(self)
        self.comboRespuesta18.addItems(respuestas)
        self.comboRespuesta18.setMinimumWidth(t)
        self.comboRespuesta18.move(x + 300, y)
        self.setFixedSize(400, 500)
        self.setWindowTitle('Segunda Parte')
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        btnAceptar = QtGui.QPushButton('Enviar', self)

        btnAceptar.clicked.connect(self.ingresarRespuestas)
        tamHorizontalBtn = 100
        tamVerticalBtn = 30
        btnAceptar.setMinimumSize(tamHorizontalBtn, tamVerticalBtn)
        btnAceptar.move(tamHorizontal - tamHorizontalBtn -
                        10, tamVertical - tamVerticalBtn - 10)
        self.show()

    def ingresarRespuestas(self):
        resp10 = str(self.comboRespuesta10.currentText())
        resp11 = str(self.comboRespuesta11.currentText())
        resp12 = str(self.comboRespuesta12.currentText())
        resp13 = str(self.comboRespuesta13.currentText())
        resp14 = str(self.comboRespuesta14.currentText())
        resp15 = str(self.comboRespuesta15.currentText())
        resp16 = str(self.comboRespuesta16.currentText())
        resp17 = str(self.comboRespuesta17.currentText())
        resp18 = str(self.comboRespuesta18.currentText())

        datos = "r10: " + resp10 + "\n"
        datos += "r11: " + resp11 + "\n"
        datos += "r12: " + resp12 + "\n"
        datos += "r13: " + resp13 + "\n"
        datos += "r14: " + resp14 + "\n"
        datos += "r15: " + resp15 + "\n"
        datos += "r16: " + resp16 + "\n"
        datos += "r17: " + resp17 + "\n"
        datos += "r18: " + resp18

        file = open(self.archivo + "SegundaParte.txt", 'w')
        file.write(datos)
        file.close()

        # Mostrar panel dando las gracias al usuario

        self.close()
