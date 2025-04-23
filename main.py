# main.py
import sys
from PyQt6 import QtWidgets
from test1_ui import Ui_Dialog

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.show()
    sys.exit(app.exec())