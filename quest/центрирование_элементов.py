#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

"""Здесь мы научились центрировать конкретный виджет"""
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

        # Создание рабочего класса, наследуемого от QMainWindow
        # Инициализация конструктора, и вызов родительского конструктора
        # Вызов метода, ответственного за GUI

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        # Здесь в первой строке мы создаем виджет редактирования текста
        # Во второй строке мы делаем его центральным виджетом.
        # Тоесть он займет все оставшееся пространство приложения

        exitAction = QAction(QIcon('C:\PycharmProjects\quest\images\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        # Создаем абстрактное действие, задаем ему картинку и пояснительный текст
        # Задаем описание комбинации клавиш этого действия
        # Задаем подсказку в статус баре при наведении курсора на действие
        # Задаем событие действию - в нашем случае закрытие приложения

        self.statusBar()
        # Инициализируем статус бар, добавляем себе в приложение

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        # Создаем экземпляр Меню
        # Добавляем в это меню вкладку
        # Добавляем на вкладку созданное ранее действие

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        # Создаем экземпляр класса Тулбар
        # Добавляем на тулбар созданное ранее действие

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()
        # Задаем координаты, ширину и высоту приложения
        # Задаем название приложению
        # Отображаем приложение


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())