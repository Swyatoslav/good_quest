#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        # Создаем кнопку с названием Диалог
        # Помещаем кнопку по кооординатам
        # Задаем кнопке событие - отображение Диалога

        self.le = QLineEdit(self)
        # Виджет, позволяющий вводить и редактировать строку текста.
        # Для виджета доступны функции "Отменить". "Повторить", "Вырезать", "Вставить"
        self.le.move(130, 22)
        #

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):
    # Метод, отображающий диалог
    # диалог содержит кнопки ok и cancel

        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')
        # Задаем диалог с названием Input Dialog и сообщение внутри диалога
        # Enter your name

        if ok:
            self.le.setText(str(text))
        # Диалог возвращает введённый текст и логическое значение.
        # Если мы нажимаем кнопку «ОК», то логическое значение является правдой.
        # Текст, который мы получили из диалога,
        # устанавливается в виджет редактирования строки.


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())