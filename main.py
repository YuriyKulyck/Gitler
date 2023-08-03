import random

from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(500, 500)

firstText = QLabel("Тицни, щоби дізнатися переможця!")
secondText = QLabel("Переможець: Оксана Психушка")
button = QPushButton("Визначити переможця.")

line = QVBoxLayout()
line.addWidget(firstText)
line.addWidget(secondText)
line.addWidget(button)

window.setLayout(line)

def winner():
    a = str(random.randint(0, 100))
    secondText.setText(a)

button.clicked.connect(winner)

window.show()
app.exec()
