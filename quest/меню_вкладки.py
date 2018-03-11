#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

"""Мы научились создавать меню, вкладки в меню, а также действия во вкладках"""
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAction = QAction(QIcon('C:\PycharmProjects\quest\images\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # QAction является абстракцией для действий, совершенных из меню,
        # панели инструментов, или комбинаций клавиш.
        # TODO В первой строке мы инициализируем экземпляр этого класса.
        # Первый аргумент - картинка с изображением этого действия
        # Второй аргумент - Текст с действием. В примере текст был &Exit, но особой разницы
        # я не заметил.
        # Третий аргумент - указание на родительский класс
        # TODO Во второй строке мы указываем комбинацию клавиш для этого действия
        # TODO В третьей строке мы задаем подсказку, которая появляется в статус баре,
        # при наведении курсора на пункт меню

        exitAction.triggered.connect(qApp.quit)
        # Когда мы выбираем именно это действие, срабатывает сигнал.
        # Сигнал подключен к методу quit() виджета QApplication. Это завершает приложение.

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        # В первой строке мы создаем экземпляр меню
        # Во второй строке мы добавляем вкладку в это меню
        # В третьей строке мы добавляем наш пукнт закрытия во вкладку меню

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

        # Задали размеры и положение окна, задали название, отобразили окно


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    # Создали объект приложения
    # Инициализировали экземпляр рабочего класса
    # прописали правильный выход из приложения