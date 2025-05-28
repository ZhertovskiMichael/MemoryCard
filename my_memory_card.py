from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup) 
from random import randint, shuffle

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')

question = QLabel('Самый сложный вопрос в мире!')
QuestedGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
btn_OK = QPushButton('Ответить')

class Question:
        def __init__(self, q_text, right_ans, wronge1, wronge2, wronge3):
                self.q_text = q_text
                self.right_ans = right_ans
                self.wronge1 = wronge1
                self.wronge2 = wronge2
                self.wronge3 = wronge3

quest_list =[
 Question('На каком языке говорят в Бразилии?', 'Порнугальский', 'Немецкий', 'Бразильский', 'Американский'),
  Question('Столица России', 'Москва', 'Новосибирск', 'Сочи', 'Бийск'),
   Question('На каком языке говорят в Шардертуании?', 'Такой страны нет', 'Английский', 'Испанский', 'Русский')
]

gb_layout1 = QVBoxLayout()
gb_layout2 = QVBoxLayout()
gb_layout3 = QHBoxLayout()

gb_layout1.addWidget(rbtn1)
gb_layout1.addWidget(rbtn2)
gb_layout2.addWidget(rbtn3)
gb_layout2.addWidget(rbtn4)

btn_group = QButtonGroup()
btn_group.addButton(rbtn1)
btn_group.addButton(rbtn2)
btn_group.addButton(rbtn3)
btn_group.addButton(rbtn4)

gb_layout3.addLayout(gb_layout1)
gb_layout3.addLayout(gb_layout2)

QuestedGroupBox.setLayout(gb_layout3)

gb_layout3 = QVBoxLayout()

gb_layout3.addWidget(question, alignment=Qt.AlignCenter)
gb_layout3.addWidget(QuestedGroupBox)

AnsGroupBox = QGroupBox('Результат теста')
res = QLabel('Верно/Неверно')
answer = QLabel('Верный ответ')

gb_ans_layout = QVBoxLayout()

gb_ans_layout.addWidget(res, alignment=Qt.AlignLeft)
gb_ans_layout.addWidget(answer, alignment=Qt.AlignCenter)

AnsGroupBox.setLayout(gb_ans_layout)

gb_layout3.addWidget(AnsGroupBox)
gb_layout3.addWidget(btn_OK)
window.setLayout(gb_layout3)

QuestedGroupBox.show()
AnsGroupBox.hide()

def next_question():
        num = randint(0, len(quest_list) - 1)
        q = quest_list[num]
        ask(q)

def check_answer():
        if answers[0].isChecked():
            show_correct('Правельно!')
        elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')        

def show_result():
        QuestedGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следующий вопрос')

def show_question():
        QuestedGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Ответить')
        btn_group.setExclusive(False)
        rbtn1.setChecked(False)
        rbtn2.setChecked(False)
        rbtn3.setChecked(False)
        rbtn4.setChecked(False)
        btn_group.setExclusive(True)

def show_correct(resulte):
        res.setText(resulte)
        answer.setText(answers[0].text())
        show_result()


def show_window():
        if btn_OK.text() == 'Ответить':
                check_answer()
        else:
                next_question()

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q):
        shuffle(answers)
        question.setText(q.q_text)
        answers[0].setText(q.right_ans)
        answers[1].setText(q.wronge1)
        answers[2].setText(q.wronge2)
        answers[3].setText(q.wronge3)
        show_question()

btn_OK.clicked.connect(show_window)
q = Question('На каком языке говорят в Бразилии', 'Порнугальский', 'Немецкий', 'Бразильский', 'Американский')
ask(quest_list[0])
window.show()
app.exec_()