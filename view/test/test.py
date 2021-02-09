from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QHBoxLayout
from PyQt5 import QtWidgets
from time import sleep
import sys

def test(window):
    button1 = QtWidgets.QPushButton("One")
    button2 = QtWidgets.QPushButton("Two")
    button3 = QtWidgets.QPushButton("Three")
    button4 = QtWidgets.QPushButton("Four")
    button5 = QtWidgets.QPushButton("Five")

    layout = QHBoxLayout()
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    layout.addWidget(button4)
    layout.addWidget(button5)

    window.setLayout(layout)
    window.show()

def clear_Layout(window):
    item = window.layout().itemAt(0)
    print(item)
    window.show()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Memory")

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)

        # creating a label widget
        self.label_1 = QtWidgets.QPushButton("Label", self)

        # moving position
        self.label_1.move(100, 100)

        # setting up border
        self.label_1.setStyleSheet("border: 1px solid black;")

        # delete reference
        self.label_1.deleteLater()

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())