import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox, QLineEdit
)
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Hello, world!'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(30, 30)
        self.textbox.resize(280, 40)
        # add the button
        self.button = QPushButton('Click me', self)
        # create a hover message
        # self.button.setToolTip('thanks for thinking about me')
        # set the buttons location
        self.button.move(100, 70)
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(
            self, 'Confirm: ', textboxValue, QMessageBox.Ok | QMessageBox.No,
            QMessageBox.Ok
        )
        self.textbox.setText('...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())