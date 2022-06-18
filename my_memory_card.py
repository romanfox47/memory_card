from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QGroupBox, QRadioButton, QButtonGroup

)
from random import shuffle

app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый простейший вопрос в мире.')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_1 = QRadioButton('Вариант 2')
rbtn_1 = QRadioButton('Вариант 3')
rbtn_1 = QRadioButton('Вариант 4')

RadioGroupBox = QButtonGroup()
RadioGroupBox.addButton(rbtn_1)
RadioGroupBox.addButton(rbtn_2)
RadioGroupBox.addButton(rbtn_3)
RadioGroupBox.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox

main_win = QWidget()
main_win.resize(100, 100)
main_win.move(100, 100)
main_win.move(100, 100)

answer1 = QRadioButton('Смурфы')
answer2 = QRadioButton('Алеуты')
answer3 = QRadioButton('Чулымцы')
answer4 = QRadioButton('Энцы')
question = QLabel('Какой национальности не существует?')
QPushButton = QLabel('Ответить')

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(question, alignment = Qt.AlignCenter)
layoutH3.addWidget(question, alignment = Qt.AlignCenter)

layout_main = QHBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)

def show_win():
    victory=QMessegeBox()
    victory.setText('Правильный ответ!')
    victory.exec_()

def show_lose():
    victory.setText('Они существуют.')
    victory.exec_
answer1.clicked.connect(show_win)
answer2.clicked.connect(show_lose)
nswer3.clicked.connect(show_lose)
answer4.clicked.connect(show_lose)


main_win.show()
app.exec_()