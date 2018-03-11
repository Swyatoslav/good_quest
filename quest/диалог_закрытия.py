#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

"""Здесь мы научились переопределять событие закрытия окна.
Мы добавили диалог Да/Нет, на случай если инициировали закрытие по ошибке"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        # Рабочий класс Example, наследуемый от QWidget
        # Конструктор, в котором вызывается конструктор родительского класса,
        # И вызывается метод, ответственный за GUI приложения

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()
        # Задаем положение приложения, ширину и высоту
        # Отображаем приложение

    # Если мы закрываем QWidget, генерируется QCloseEvent.
    # Чтобы изменить поведение виджета, нам нужно переопределить
    #  обработчик события closeEvent().
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Тупанул',
            "Не передумал? Нам будет тебя не хватать",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes)
        # Первая строка отображается в заголовке окна - название окна
        # Вторая строка - текстовое сообщение, отображаемое в окне
        # Третий аргумент определяет комбинацию кнопок в диалоге.
        # Последний аргумент - кнопка, на которой изначально стоит фокус клавы.
        # Возвращаемое значение хранится в переменной reply

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        # Проверяем - если в кнопке хранится Yes - соглашаемся с событием
        # Если в кнопке хранится другое - отказываемся от события


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())