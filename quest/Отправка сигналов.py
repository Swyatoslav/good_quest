import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

"""Посылаем пользовательский сигнал"""
class Communicate(QObject):
    # Создаем класс, в котором реализуем пользовательские сигналы
    closeApp = pyqtSignal()
    # новый сигнал, названный closeApp
    # Сигнал создаётся с помощью pyqtSignal()
    # как атрибут внешнего класса Communicate.


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        # Присоединяем наш сигнал к слоту close() класса QMainWindow

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()


    def mousePressEvent(self, event):

        self.c.closeApp.emit()
        # Когда мы кликаем на окне курсором мыши,
        # посылается сигнал closeApp. Приложение завершается.


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())