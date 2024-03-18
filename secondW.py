# напиши здесь код для второго экрана приложения
# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from final_win import *

class Info():
    def __init__(self, name, age, P1, P2, P3):
        self.name = name
        self.age = age
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3


class SecondW(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Здоровье")
        self.resize(900, 700)

        self.main_line = QHBoxLayout()
        self.v_line1 = QVBoxLayout()
        self.main_line.addLayout(self.v_line1)

        self.Name = self.createLabel("Введите Ф.И.О.")
        self.InputName = self.createLineEdit("Ф.И.О.")
        self.Age = self.createLabel("Полных лет:")
        self.InputAge = self.createLineEdit("0")
        self.Instruction1 = self.createLabel("Лягте на спину и замерьте пульс за 15 сек. Результат запишите в соответствующее поле.")
        self.Quiet = self.createLineEdit("0")
        self.Instruction2 = self.createLabel("Выполните 30 приседаний за 45 сек. \nЛягте на спину и замерьте пульс за первые 15 секунд минуты, затем за последние 15 секунд. Результат запишите в соответствующие поля.")
        self.Result1 = self.createLineEdit("0")
        self.Result2 = self.createLineEdit("0")

        self.GetButton = QPushButton("Отправить результаты")
        self.GetButton.clicked.connect(self.click_result)

        self.v_line1.addWidget(self.Name, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.InputName, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.Age, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.InputAge, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.Instruction1, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.Quiet, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.Instruction2, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.Result1, alignment=Qt.AlignLeft)
        self.v_line1.addWidget(self.Result2, alignment=Qt.AlignLeft)

        self.v_line1.addWidget(self.GetButton, alignment=Qt.AlignCenter)

        self.setLayout(self.main_line)

        self.show()

    def createLabel(self, text):
        return QLabel(text)
    
    def createLineEdit(self, text):
        inp = QLineEdit()
        inp.setPlaceholderText(text)
        return inp

    def click_result(self):
        if self.InputName.text() == "":
            self.name = "Имя"
        else:
            self.name = self.InputName.text()

        if self.InputAge.text() == "":
            self.age = 7
        else:
            self.age = int(self.InputAge.text())

        if self.Quiet.text() == "":
            self.P1 = 0
        else:
            self.P1 = int(self.Quiet.text())
        
        if self.Result1.text() == '':
            self.P2 = 0
        else:
            self.P2 = int(self.Result1.text())

        if self.Result2.text() == '':
            self.P3 = 0
        else:
            self.P3 = int(self.Result2.text())


        self.info = Info(self.name, self.age ,self.P1 ,self.P2 ,self.P3 )

        self.NW = ThirdW(self.info)
        self.hide()
        self.NW.show()

