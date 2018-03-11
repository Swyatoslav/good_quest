#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow

"""Здесь мы научимся абсолютному позиционированию элементов и размещению простых текстов"""
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        # Объявили рабочий класс. В конструкторе класса инициализируем
        # Родительский класс Qwidget

    def initUI(self):

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)
        # QLabel - обычный текст в приложении
        # Жестко задаем его координаты

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()
        # Задали координаты окна, ширину и высоту
        # Назвали наше приложение
        # Отобразили наше приложение


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    # Объявили экземпляр класса application
    # Объявили экземпляр рабочего класса
    # Прописали правильный выход из приложения