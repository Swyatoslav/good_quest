#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication)

"""Здесь мы научимся работать с сеточным макетом"""

# Этот макет делит пространство на строки и столбцы.
# Чтобы создать сеточный макет, мы используем класс QGridLayout.
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        # Первая строка - объявление класса сеточного макета
        # Вторая строка - помещение макета в приложение

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        # Имена будущих кнопок

        positions = [(i,j) for i in range(5) for j in range(4)]
        # Позиции наших кнопок в сетке макета

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

            # Перебирая имена кнопок и позиции, создаем кнопки на макете

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())