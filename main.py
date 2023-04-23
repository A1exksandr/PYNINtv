from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QlineEdit
from PyQt5.QtWidgets imports  
line_name = QLineEdit ('Текст виджета')
  from second_win import *
  
class MainWin(QWidget):
  def __init_(self):
    super().__init__()
    self.iniyUI()
    self.connects()
    self.set_appear()

  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
    
  def initUI(self):
    self.hello_text = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)
    self.button = QPushButton(text_next)
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.hello_texy)
    self.layout.addWidget(self.instruction)
    self.layout.addWidget(self.button)
    
  def connets(self):
    self.btn_next.clicked.connect(self.next_click)
  def next_click(self):
  def next_click(self):
      self.hide()
      self.tw = TestWin()
  
  app = QApplication([])
  mw = MainWin()
  app.exec_()
  
  
    
   
