# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

"""Здесь мы научились задавать иконку нашему приложению"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        # Пользуемся ООП.
        # Создаем класс, наследуемый от классса QWidget
        # C помощью функции super возвращаем родительский объект Example с классом
        # , после чего вызываем конструктор этого класса. Напомню что QWidget -
        # базовый класс для всех виджетов - окно

        self.initUI()

        # Сразу в конструкоре начинаем создание GUI. Для этого вызовем метод iniutUI,
        # Логику которого распишем чуть позднее, уже не в теле конструктора, а в теле самого класса


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')  # Название окна
        self.setWindowIcon(QIcon('C:\PycharmProjects\quest\images\icons8-череп-50.png'))

        # Три вышеобъявленных метода были унаследованы от класса QWidget

        # Метод setGeometry() делает две вещи: помещает окно на экране и устанавливает его размер
        # Первые два параметра х и у - это позиция окна.
        # Третий - ширина, и четвертый - высота окна.
        # На самом деле, он сочетает в себе методы resize() и move() в одном методе

        # Последний метод устанавливает иконку приложения. Чтобы сделать это, мы создали объект QIcon.
        # QIcon получает путь к нашей иконке для отображения.

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    # По запуску приложения создаются объекты классов zpplication и нашего Example
    # Запускается основной цикл приложения. Также прописываем функцию чистого выхода