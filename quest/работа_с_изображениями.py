#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QMainWindow,
    QLabel, QApplication, QGridLayout, QPushButton, QAction)
from PyQt5.QtGui import QPixmap, QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # Главный макет окна
        vbox = QVBoxLayout(self)

        pixmap = QPixmap("C:\PycharmProjects\quest\images\IMG_2015.JPG")
        # QPixMap – это один из виджетов, использующихся для работы с изображениями.
        # Он оптимизирован для показа изображений на экране.

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        # Мы поместили изображение в виджет QLabel.

        # Текст квеста
        vbox.addWidget(lbl)
        lbl2 = QLabel(" "*30 + 'Ты стоишь на берегу озера, вокруг ни одной души.', self)
        lbl3 = QLabel(" "*30 + 'Слева ты видишь брошеный рюкзак, наполовину утоновший в воде', self)
        lbl4 = QLabel(" "*30 + 'Справа деревянный знак, к которому прикреплена записка.')
        lbl5 = QLabel(" "*30 + 'В животе заурчало - я не ел уже несколько дней...')
        vbox.addWidget(lbl2)
        vbox.addWidget(lbl3)
        vbox.addWidget(lbl4)
        vbox.addWidget(lbl5)

        # Макет с кнопками действий
        hbox = QHBoxLayout(self)

        # Кнопки квеста
        leftBtn = QPushButton('Подойти к рюкзаку', self)
        leftBtn.resize(leftBtn.sizeHint())
        rightBtn = QPushButton('Подойти к знаку', self)
        rightBtn.resize(rightBtn.sizeHint())
        otherBtn = QPushButton('Перекусить бананом', self)
        otherBtn.resize(otherBtn.sizeHint())
        hbox.addWidget(leftBtn)
        hbox.addWidget(rightBtn)
        hbox.addWidget(otherBtn)

        # Помешение кнопок в главный макет
        vbox.addLayout(hbox)

        # Установка главного макета в программу
        self.setLayout(vbox)

        self.move(300, 200)
        self.setWindowTitle('Озеро')
        self.setWindowIcon(QIcon('C:\PycharmProjects\quest\images\icons8-череп-50.png'))
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())