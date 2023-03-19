import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QDialog,
    QVBoxLayout
)
'''
simple window example:
'''

# app = QApplication(sys.argv)

# root = QWidget()
# root.resize(320, 240)
# root.setWindowTitle("Hello world")
# root.show()

# sys.exit(app.exec())
'''
verbose way to create a window:
'''


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

        buttonReply = QMessageBox.question(
            self,
            'Hello',
            "Do you like cookies?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.
            No  # this last QMessageBox sets which option is highlighted by default
        )
        if buttonReply == QMessageBox.Yes:
            print("Yeah")
        else:
            print("Nah")
        # add the button
        button = QPushButton('Click me', self)
        # create a hover message
        button.setToolTip('thanks for thinking about me')
        # set the buttons location
        button.move(100, 70)
        # add a status bar to the bottom of the GUI
        self.statusBar().showMessage("in progress")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
'''
add apop out dialog box
'''
# class Dialog(QDialog):
#     def slot_method(self):
#         print("calling the slot")

#     def __init__(self):
#         super(Dialog, self).__init__()
#         button = QPushButton("click moi")
#         button.clicked.connect(self.slot_method)
#         mainlayout = QVBoxLayout()
#         mainlayout.addWidget(button)
#         self.setLayout(mainlayout)
#         self.setWindowTitle("Hello world!")
#         self.setGeometry(100, 100, 200, 200)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dialog = Dialog()
# dialog.exec()