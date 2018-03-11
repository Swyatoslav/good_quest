#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

"""В этом уроке мы научились создавать кнопку закрытия приложения"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        # Наш рабочий класс. Конструкторы нашего класса и родительского QWinget
        # Вызов метода initUI для построение GUI

    def initUI(self):

        qbtn = QPushButton('Quit', self)
        # Создаем кнопку. Первый параметр - название, второй - родительский виджет
        # Родительский виджет - Example, наследующийся ль QWidget

        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # По нажатию кнопки инициализируется закрытие приложения

        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        # Размеры кнопки и её координаты

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()
        # Координаты, высота и ширина окна
        # название окна
        # Отображение окна


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    # Инициализация QApplication
    # Инициализация рабочего класса
    # Правильный выход