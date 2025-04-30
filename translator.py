# main.py
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# 다크모드 스타일 시트 (VSCode/Obsidian 유사한 느낌)
dark_stylesheet = """
QMainWindow {
    background-color: #1e1e1e;
    color: #d4d4d4;
}

QTabWidget::pane {
    border: 1px solid #3c3c3c;
    background-color: #1e1e1e;
}

QWidget {
    background-color: #1e1e1e;
    color: #d4d4d4;
    font-size: 14px;
}

QPlainTextEdit, QTextEdit, QLineEdit {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    padding: 4px;
    border-radius: 4px;
}

QComboBox, QSpinBox, QDoubleSpinBox {
    background-color: #2d2d30;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    padding: 2px;
    border-radius: 4px;
}

QPushButton {
    background-color: #0e639c;
    color: #ffffff;
    border: none;
    padding: 6px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #1177bb;
}
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("translator_ui.ui", self)
        self.setWindowTitle("AI Translator by mochabrie")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(dark_stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
