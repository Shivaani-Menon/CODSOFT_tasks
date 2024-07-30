import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pyqt_checkbox_list_widget import CheckBoxListWidget
class TDApp(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle("To-Do Application")
        self.setGeometry(200,200,500,700)
        self.setStyleSheet('background-color: #F4ECE8')

        self.taskgrp=[]

        self.label = QLabel("New Task:",self)
        self.label.setFont(QFont('Times font', 12))

        self.input_det=QLineEdit()
        self.input_det.setStyleSheet('background-color: #FFFFFF')
        self.input_det.setFixedHeight(40)
        self.input_det.setFont(QFont('Times font', 12))

        self.btn_add=QPushButton("ADD TASK")
        self.btn_add.setStyleSheet('background-color: #5C62D6')
        self.btn_add.setFont(QFont('Times font', 14))

        self.allCheck=QCheckBox("ALL")
        self.allCheck.setFixedHeight(25)
        self.allCheck.setFont(QFont('Times font', 12))
        self.cb_list=CheckBoxListWidget()
        self.cb_list.setStyleSheet('background-color: #FFFFFF')
        self.cb_list.setFont(QFont('Times font', 12))

        self.btn_done=QPushButton("TASKS DONE")
        self.btn_done.setStyleSheet('background-color: #5C62D6')
        self.btn_done.setFont(QFont('Times font', 14))

        self.layout=QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_det)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.allCheck)
        self.layout.addWidget(self.cb_list)
        self.layout.addWidget(self.btn_done)

        self.btn_add.clicked.connect(self.add_task)
        self.allCheck.stateChanged.connect(self.cb_list.toggleState)
        self.btn_done.clicked.connect(self.task_done)
        self.setLayout(self.layout)
    
    def add_task(self):
        task=self.input_det.text()
        if task:
            self.cb_list.addItem(task)
            self.taskgrp.append(task)
            self.input_det.clear()
    
    def task_done(self):
        self.check=[]
        for i in range(self.cb_list.count()):
            item=self.cb_list.item(i)
            if item.checkState():
                self.check.append(item.text())
        
        for k in range(len(self.check)):
            for j in range(len(self.taskgrp)-1,-1,-1):
                if self.check[k] == self.taskgrp[j]:
                    self.taskgrp.pop(j)

        self.cb_list.removeCheckedRows()
        self.allCheck.setChecked(False)
        print("Tasks Checked out = ", self.check) #checked out tasks -list
        print("Task List = ", self.taskgrp) #the task list without checked out task

app=QApplication(sys.argv)
window=TDApp()
window.show()
app.exec_()