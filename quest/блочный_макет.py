#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication)

"""Здесь мы научимся методу блочного макета, работе с горизонтальным
и вертикальным макетами, и немного больше работе с кнопками"""

# Управление макетом классами макета является более гибким и практичным.
# Это предпочтительный путь размещения виджетов в окне.
# QHBoxLayout и QVBoxLayout – это основные классы макета,
# которые выстраивают виджеты горизонтально или вертикально.

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # Создаем две кнопки - OK и Cancel. Текст кнопок передается в аргумент QPushButton

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # Первая строка - объявляем класс горизонтального макета
        # Вторая строка - добавляем показатель растяжения
        # Третья и четвертая строки - добавляем в макет созданные кнопки

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # Первая строка - объявление класса вертикального макета
        # Вторая строка - добавляем показатель вертикального растяжения
        # Третья строка - вкладываем горизонтальный макет в вертикальный
        # Показатель растяжения в вертикальном блоке прижмёт
        # горизонтальный блок с кнопками к нижней части окна.

        self.setLayout(vbox)
        # Устанавливаем главный макет окна. Без этого элементы просто не отобразятся

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())