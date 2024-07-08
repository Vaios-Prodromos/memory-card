#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGroupBox, 
QButtonGroup, QHBoxLayout, QVBoxLayout, QRadioButton, QPushButton)
from random import *

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
answers = []

# Application and window creation
app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(400, 200)

# Widget creation
# Answer button
answer_button = QPushButton("Answer")
question = QLabel("Which nationality does not exist?")

# Answers inside group box
radio_btn1 = QRadioButton("Enets")
radio_btn2 = QRadioButton("Smurfs")
radio_btn3 = QRadioButton("Chulyms")
radio_btn4 = QRadioButton("Aleuts")

RadioGroup = QButtonGroup()
RadioGroup.addButton(radio_btn1)
RadioGroup.addButton(radio_btn2)
RadioGroup.addButton(radio_btn3)
RadioGroup.addButton(radio_btn4)

# Answer Group Box
AnswerGroupBox = QGroupBox("Test Result")

result = QLabel("Correct!")
correct_label = QLabel("You are correct, the answer is:")

answer_layout = QVBoxLayout()
answer_layout.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
answer_layout.addWidget(correct_label, alignment=Qt.AlignHCenter)

AnswerGroupBox.setLayout(answer_layout)

# Creation of group box and layouts
RadioGroupBox = QGroupBox("Answer Options")

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(radio_btn1)
layout_ans2.addWidget(radio_btn2)
layout_ans3.addWidget(radio_btn3)
layout_ans3.addWidget(radio_btn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

# Window Layouts
layout_line1 = QHBoxLayout() # Layout for question
layout_line2 = QHBoxLayout() # Layout for group box
layout_line3 = QHBoxLayout() # Layout for answer button

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnswerGroupBox)
AnswerGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(answer_button, stretch=2, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addStretch(1)

layout_window = QVBoxLayout()
layout_window.addLayout(layout_line1, stretch=2)
layout_window.addLayout(layout_line2, stretch=8)
layout_window.addStretch(1)
layout_window.addLayout(layout_line3, stretch=1)
layout_window.addStretch(1)
layout_window.setSpacing(5)

window.setLayout(layout_window)

def answer_clicked():
    # question.setText("The result of your answer is:")
    
    AnswerGroupBox.show()
    RadioGroupBox.hide()

    answer_button.setText("Next Question")

answers = [radio_btn1, radio_btn2, radio_btn3, radio_btn4]

def ask(q: Question):
    shuffle(answers) # Shuffling answers in the buttons

    answers[0].setText(q.right_answer) # Right and wrong answers
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    question.setText(q.question) # Question label in the window

    correct_label.setText(q.right_answer)

    show_question()

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    answer_button.setText("Answer")

    RadioGroup.setExclusive(False)

    radio_btn1.setChecked(False)
    radio_btn2.setChecked(False)
    radio_btn3.setChecked(False)
    radio_btn4.setChecked(False)

    RadioGroup.setExclusive(True)

def check_answer():
    if answers[0].isChecked():
        result.setText("Correct!")
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        result.setText("Incorrect!")
    
    answer_clicked()

def next_question():
    window.current_question += 1

    if window.current_question >= len(questions_list):
        window.current_question = 0
    
    q = questions_list[window.current_question]
    ask(q)

def check_button():
    if answer_button.text() == 'Next Question':
        next_question()
    elif answer_button.text() == "Answer":
        check_answer()

window.current_question = -1

q1 = Question("Which nationality does not exist?", "Chulyms", "Enets", "Smurfs", "Aleuts")
q2 = Question("What language do they speak in Brazil?", "Portuguese", "Spanish", "English", "French")
q3 = Question("Which is the capital city of Lithuania?", "Vilnius", "Athens", "Berlin", "Paris")

questions_list = [q1, q2, q3]
# questions_list.append(q1)

# ask(q)

answer_button.clicked.connect(check_button)

window.show()
app.exec()