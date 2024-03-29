import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Hello, world!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Open color dialog', self)
        button.setToolTip('This opens the color dialog')
        button.move(10, 10)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):

        openColorDialog(self)


def openColorDialog(self):

    color = QColorDialog.getColor()

    if color.isValid():
        print(color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())