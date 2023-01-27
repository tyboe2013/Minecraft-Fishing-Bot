import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)

from PyQt5.uic import loadUi

from MainWindow import Ui_Title


class Window(QMainWindow, Ui_Title):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())