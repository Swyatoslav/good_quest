#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont

"""В данном уроке мы научимся создавать виджет кнопки, перемещать кнопку,
создавать всплывающую подсказку для кнопки"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        # Создаем наш класс Example, наследуемый от QWidget. Вызываем его конструктор,
        # и конструктор базового класса. В конструкторе будет вызываться ответственный
        # За QUI метод initUI()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        # Данный статический метод устанавливаем шрифт, используемый для отображения
        # подсказки. В данном случае шрифт SansSerif, 10px

        self.setToolTip('This is a <b>QWidget</b> widget')

        # Метод создает саму всплывающую подсказку. Можем использовать
        # html форматирование текста этой подсказки

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # Создаем виджет кнопки и устанавливаем подсказку для него
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # метод resize(btn.sizeHint()) создает рекомендуемый размер кнопки
        # метод move в данном случае помещает кнопку в координаты относительно окна

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

        # Первый метод - задаем координаты окна, высоту и ширину
        # второй метод - задает название окну
        # третий метод - делает окно видимым


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    # Создаем экземпляр приложения с переданными аргументами
    # Создаем экземпляр класса Example
    # Задаем правильный выход из приложения