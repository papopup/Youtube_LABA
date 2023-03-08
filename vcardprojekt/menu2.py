import sys
import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import signal
from PyQt5.QtGui import QGuiApplication, QFont

from menu import Ui_Dialog

class MainWindow (QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

def window():
    app = QGuiApplication(sys.argv)
    window = MainWindow
    window.show()
    sys.exit(app.exec_())

window()