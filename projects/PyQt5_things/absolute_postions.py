import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Hello, world!'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel('Pink', self)
        label.move(50, 50)
        label2 = QLabel('Blue', self)
        label2.move(100, 100)
        label3 = QLabel('Green', self)
        label3.move(150, 150)
        label4 = QLabel('Lavender', self)
        label4.move(200, 200)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())