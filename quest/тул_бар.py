#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

"""Здесь мы научились создавать тулбар"""
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAction = QAction(QIcon('C:\PycharmProjects\quest\images\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        # Аналогично созданию меню.
        # В первой строке мы создали абстрактное действие, задали ему текст и картинку
        # Во второй строке прописали комбинацию клавиш этого действия
        # В третьей строке сказали, что это действие инициирует закрытие приложения

        self.toolbar = self.addToolBar('Выход')
        self.toolbar.addAction(exitAction)
        # TODO В первой строке мы задаем пояснение к кнопке.
        # При нажатии ПКМ в приложении мы увидим возможность исключить
        # Действие из доступных в тулбаре, где увидим пояснение Выход
        # TODO Во второй строке мы добавляем действие на тулбар

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())