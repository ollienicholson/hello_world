import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        # NOTE Option 1 =====================
        # dlg = QMessageBox(self)
        # dlg.setWindowTitle("I have a question!")
        # dlg.setText("This is a simple dialog")
        # dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # dlg.setIcon(QMessageBox.Question)
        # button = dlg.exec()

        # if button == QMessageBox.Yes:
        #     print("Yes!")
        # else:
        #     print("No!")

        # NOTE Option 2 =====================
        # button = QMessageBox.question(
        #     self, "Question dialog", "The longer message"
        # )
        # if button == QMessageBox.Yes:
        #     print("Yes!")
        # else:
        #     print("No!")

        # NOTE Option 3 =====================
        button = QMessageBox.warning(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll
            | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")

        dlg = CustomDialog(self)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec()


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Save | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()