import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget

class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)

        # Create line edit for displaying results
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)

        # Create buttons
        self.create_buttons()

        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display)
        self.layout.addLayout(self.buttons_layout)

        # Create central widget and set layout
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def create_buttons(self):
        self.buttons_layout = QHBoxLayout()
        buttons = ["7", "8", "9", "+",
                   "4", "5", "6", "-",
                   "1", "2", "3", "*",
                   "C", "0", "=", "/"]
        for button in buttons:
            btn = QPushButton(button, self)
            btn.clicked.connect(lambda state, x=button: self.process_clicks(x))
            self.buttons_layout.addWidget(btn)

    def process_clicks(self, value):
        if value == "C":
            self.display.setText("")
        elif value in "+-*/":
            if self.display.text() and self.display.text()[-1] in "+-*/":
                return
            self.display.setText(self.display.text() + value)
        elif value == "=":
            expression = self.display.text()
            if not expression:
                return
            if expression[-1] in "+-*/":
                return
            try:
                result = eval(expression)
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
