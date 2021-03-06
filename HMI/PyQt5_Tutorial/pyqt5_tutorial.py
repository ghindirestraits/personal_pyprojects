#! /usr/bin/env python

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

xpos = 200
ypos = 200
width = 300
height = 300

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle('PyQt5 Tutorial')

    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    label.move(100, 50)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
