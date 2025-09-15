
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.create_widgets()

    def create_widgets(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)
        self.grid.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_clicked)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = QPushButton("C")
        clear_button.clicked.connect(self.clear_display)
        self.grid.addWidget(clear_button, row, 0, 1, 2)
        
        back_button = QPushButton("<-")
        back_button.clicked.connect(self.backspace)
        self.grid.addWidget(back_button, row, 2, 1, 2)


    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Ошибка")
        else:
            current_text = self.display.text()
            if current_text == "Ошибка":
                self.display.setText(text)
            else:
                self.display.setText(current_text + text)

    def clear_display(self):
        self.display.clear()
        
    def backspace(self):
        current_text = self.display.text()
        if current_text != "Ошибка":
            self.display.setText(current_text[:-1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
