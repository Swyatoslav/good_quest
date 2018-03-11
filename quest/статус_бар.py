#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Класс QMainWindow предоставляет главное окно приложения.
# Это позволяет создать классический каркас приложений с статусбаром,
# тулбаром и меню.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

"""Здесь мы научились создавать статус бар"""
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

        # Рабочий класс с функциями. Инициализация основного конструктора, и
        # Вызов конструктора родительского класса QMainWindow

    def initUI(self):

        self.statusBar().showMessage('Ready')
        # Строка состояния. Чтобы получить её, вызывается метод statusBar
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())