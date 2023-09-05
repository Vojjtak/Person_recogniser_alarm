import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
import recognizer


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Person recognizer')

        button = QPushButton('Start app')
        button.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        self.show()

    def button_clicked(self):
        call = recognizer.PersonRecognizer()
        call.recognizer()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())




