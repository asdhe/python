import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

window = QMainWindow()

window.resize(620, 400)

window.move(300, 310)

window.setWindowTitle('Student TABLE')
window.setWindowIcon(QtGui.QIcon('123.jpg'))

def handleClick():
 import 数据库
 a=db()
 a.checkDB()

button = QPushButton('点击生成表', window)
button.resize(200,100)
button.move(210,130)
button.clicked.connect(handleClick)
window.show()
sys.exit(app.exec_())
