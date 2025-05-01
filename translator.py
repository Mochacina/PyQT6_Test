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
        self.setWindowTitle("AI 번역기")
        
        # inputLangCombo 기본값, 변수 설정
        self.inputLangCombo.setCurrentIndex(1)
        self.inputLang = self.inputLangCombo.currentText()
        self.outputLang = self.outputLangCombo.currentText()

        # 연결: 글자 수 표시
        self.inputTextEdit.textChanged.connect(self.update_input_char_count)
        self.outputTextEdit.textChanged.connect(self.update_output_char_count)

        # 연결: 언어 동일 시 자동 교환
        self.inputLangCombo.currentTextChanged.connect(self.handle_lang_change)
        self.outputLangCombo.currentTextChanged.connect(self.handle_lang_change)

        # 연결: ⇄ 버튼
        self.swapLangButton.clicked.connect(self.swap_languages)

        # 초기 글자 수 표시
        self.update_input_char_count()
        self.update_output_char_count()

    def update_input_char_count(self):
        text = self.inputTextEdit.toPlainText()
        self.inputCharCount.setText(f"{len(text)}자 입력됨")

    def update_output_char_count(self):
        text = self.outputTextEdit.toPlainText()
        self.outputCharCount.setText(f"{len(text)}자 출력됨")

    def handle_lang_change(self):
        in_lang = self.inputLangCombo.currentText()
        out_lang = self.outputLangCombo.currentText()
        if in_lang == out_lang:
            self.inputLangCombo.setCurrentText(self.outputLang)
            self.outputLangCombo.setCurrentText(self.inputLang)
        self.inputLang = self.inputLangCombo.currentText()
        self.outputLang = self.outputLangCombo.currentText()

    def swap_languages(self):
        in_index = self.inputLangCombo.currentIndex()
        out_index = self.outputLangCombo.currentIndex()
        self.inputLangCombo.setCurrentIndex(out_index)
        self.outputLangCombo.setCurrentIndex(in_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(dark_stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
