from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle
from random import randint
class question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question= question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(question('Нет дыма ...','без огня',' без меня',' без шашлыка','без рок композиции'))
question_list.append(question('Какого цвета не в флаге России?','зеленый','красный','синий','белый'))
question_list.append(question('Национальная хижина якутов','Ураса','Юрта','Уграса','Нидерлднаса'))
question_list.append(question('Кто озвучивал Андрея Миронова в фильме "Следопыт"?','голос Первого канала','голос России-1','голос НТВ','голос СТС'))
question_list.append(question('В каком году родилась Билли Айлиш?','в 2001 г.','в 1997 г.','в 2003 г.','в 1995 г.'))
question_list.append(question('Сколько футов в одном ярде?','3','2','4','1'))
question_list.append(question('Как по-простому называют дурнопахнущий аморфофаллус титанический?','трупный цветок','мёртвый цветок','падальный цветок','ядерный цветок'))
question_list.append(question('Что такое бакштейн?','сорт сыра','сорт кукурузы','сорт картофеля','сорт перца'))
question_list.append(question('Какое официальное название у Гонконга?','Специальный административный район Гонконг','Особый независимый район Гонконг','Китайское королевство Гонконг','Народно-демократическая республика Гонконг'))
question_list.append(question('У кого самый большой мозг?','У кашалота','У дельфина ','У меня','У орунгутана'))
question_list.append(question('Какой местности очень нехватает Луне?','бухт','болот','заливов','долин'))
question_list.append(question('Rакая планета солнечной системы названа в честь деда древнегреческого Юпитера и отца Сатурна?','Уран','Нептун','Меркурий','Марс'))
question_list.append(question('Как римскими цифрами записывается 2019 год?','MMXIX','LLXIX','LLXIII','MMXIIII'))
question_list.append(question('В каком году произошло ЛЕДОВОЕ ПОБОИЩЕ?','1242г.','1214г.','1235г.','1236г.'))




app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
def ask(q: question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 
def show_correct(res):
    lb_Result.setText(res)
    show_result() 
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1 
        print('Статистика \n-Всего впросов:', window.total,'\nправильных ответов:',window.score)
        print('Рейтинг: ', (window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100),'%')
def next_question():
    window.total += 1
    print('Статистика \n-Всего впросов:', window.total,'\nправильных ответов:',window.score)
    cur_question = randint(0 , len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text()== 'ответить':
        check_answer()
    else:
        next_question()



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

window.cur_question = -1

btn_OK.clicked.connect(click_OK) 

window.total = 0
window.score = 0
next_question()
window.show()
app.exec()
window.resize(400,300)