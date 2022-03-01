import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_input1 = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_first1 = QHBoxLayout()
        self.hbox_first2 = QHBoxLayout()
        self.hbox_c = QHBoxLayout()
        
        
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_input1)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_first1)
        self.vbox.addLayout(self.hbox_first2)
        self.vbox.addLayout(self.hbox_result)
        self.vbox.addLayout(self.hbox_c)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.input1 = QLineEdit(self)
        self.hbox_input1.addWidget(self.input1)
        self.input2 = QLineEdit(self)
        self.hbox_input1.addWidget(self.input2)
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)
        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)
        self.b_4 = QPushButton("4", self)
        self.hbox_first1.addWidget(self.b_4)
        self.b_5 = QPushButton("5", self)
        self.hbox_first1.addWidget(self.b_5)
        self.b_6 = QPushButton("6", self)
        self.hbox_first1.addWidget(self.b_6)
        self.b_minus = QPushButton("-", self)
        self.hbox_first1.addWidget(self.b_minus)
        self.b_7 = QPushButton("7", self)
        self.hbox_first2.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)
        self.hbox_first2.addWidget(self.b_8)
        self.b_9 = QPushButton("9", self)
        self.hbox_first2.addWidget(self.b_9)
        self.b_umn = QPushButton("x", self)
        self.hbox_first2.addWidget(self.b_umn)
        self.b_t = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_t)
        self.b_0 = QPushButton("0", self)
        self.hbox_result.addWidget(self.b_0)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        self.b_del = QPushButton(":", self)
        self.hbox_result.addWidget(self.b_del)
        self.b_C = QPushButton("C", self)
        self.hbox_c.addWidget(self.b_C)
        
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_umn.clicked.connect(lambda: self._operation("*"))
        self.b_del.clicked.connect(lambda: self._operation("/"))
        self.b_C.clicked.connect(lambda: self._operation("C"))
        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_t.clicked.connect(lambda: self._button("."))
        
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)



    def _operation(self, op):

        a=self.input.text()
        z=a.find('.')
        z1=a.find('-')
        if z!=-1:
            a=a.replace('.', '')
        if z1==0:
            a=a.replace('-', '')
            if z!=-1:
                z-=1
        b=str(a.isdigit())
        if b=='True':
            if z!=-1:
                a=a[:z] + '.' + a[z:]
            if z1==0:
                a='-'+a
            self.num_1 = float(a)
        else: self.num_1 = 0
        self.input1.setText(str(self.num_1))
        
        self.op = op
        self.input.setText("")
    
    def _result(self):
       
        a=self.input.text()
        z=a.find('.')
        z1=a.find('-')
        if z!=-1:
            a=a.replace('.', '')
        if z1==0:
            a=a.replace('-', '')
            if z!=-1:
                z-=1
        b=str(a.isdigit())
        if b=='True':
            if z!=-1:
                a=a[:z] + '.' + a[z:]
            if z1==0:
                a='-'+a
            self.num_2 = float(a)
        else: self.num_2 = 0
        self.input2.setText(str(self.num_2))
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == "/":
            if self.num_2!=0:
                self.input.setText(str(self.num_1 / self.num_2))
            else: self.input.setText('Ошибка, на ноль делить нельзя!')
        if self.op == "C":
            self.num_1=0
            self.num_2=0
            self.input.setText('')
            
            
        
        
app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_()) 