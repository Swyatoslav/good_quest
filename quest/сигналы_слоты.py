#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    # Создаем рабочий класс, конструктор класса
    # Ключевым словом super вызываем конструктор родительского класса QWidget
    # initUI - метод ответственный за графику


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        # Первая строка - экземпляр LCD циферблата
        # Вторая строка - экземпляр бегунка

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        # Первая строка - вертикальный макет
        # Вторая строка - добавляем lcd дисплей в макет
        # третья строка - добавляем бегунок в макет

        self.setLayout(vbox)
        # Помещаем макет в приложение
        sld.valueChanged.connect(lcd.display)
        # Здесь мы присоединяем сигнал valueChanged слайдера к слоту display числа lcd.
        # Отправитель – объект, который посылает сигнал.
        # Получатель – объект, который получает сигнал.
        # Слот – это метод, который реагирует на сигнал.

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        # Задаем координаты, ширину и высоту приложения
        # Задаем название приложения
        # Отображаем наше приложение


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    # Обязательный экземпляр приложения
    # Создание объекта нашщего рабочего класса
    # Правильный выход из приложения