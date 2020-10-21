# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuBeta.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets,QtGui
from core.search import setFactory
from core.PyQt5Helpel import Layout
from app.db.seeder import runSeeader
runSeeader()

class menu(QtWidgets.QWidget):
    searchIn='movies'
    searchFaze='Fudzi'
    deepSearch=True

    def setupUi(self, MainWindow):
        self.Layout=Layout()
        self.mianSetings()
        self.formLayout()
        self.searchArea()
        self.serchRadioBox()
        self.menuSerch()
        self.ManuBar()
        self.searchResult()

    def ManuBar(self):
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.listWidget = QtWidgets.QListWidget(self)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def formLayout(self):
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 381, 841))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.resultArea = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.resultArea.setContentsMargins(0, 0, 0, 0)
        self.resultArea.setObjectName("resultArea")

    def searchResult(self):
        row=0
        self.Layout.clear(self.resultArea)
        for item in setFactory(self.searchIn,self).getFactory():
             el = QtWidgets.QPushButton(self.serchAreaMain)
             el.setObjectName(item.name)
             el.setText(item.name)
             self.resultArea.setWidget(row, QtWidgets.QFormLayout.FieldRole, el)
             row=row+1

    def mianSetings(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 1040)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.serchAreaMain = QtWidgets.QGroupBox(self.centralwidget)
        self.serchAreaMain.setGeometry(QtCore.QRect(0, 0, 401, 151))

    def menuSerch(self):
        self.pushButton = QtWidgets.QPushButton(self.serchAreaMain)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getDataFrom)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)

    def getDataFrom(self):
        self.searchFaze=self.serchLineEdit.text() or None
        self.searchIn=self.serchInComboBox.currentText() or None
        self.deepSearch=self.deepSerchCheckBox.isChecked()
        self.searchResult()

    def searchArea(self):
        self.serchAreaMain.setObjectName("serchAreaMain")
        self.formLayout = QtWidgets.QFormLayout(self.serchAreaMain)
        self.formLayout.setObjectName("formLayout")
        self.serchLabel = QtWidgets.QLabel(self.serchAreaMain)
        self.serchLabel.setObjectName("serchLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.serchLabel)
        self.serchLineEdit = QtWidgets.QLineEdit(self.serchAreaMain)
        self.serchLineEdit.setObjectName("serchLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.serchLineEdit)
        self.serchInLabel = QtWidgets.QLabel(self.serchAreaMain)
        self.serchInLabel.setObjectName("serchInLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.serchInLabel)
        self.serchInComboBox = QtWidgets.QComboBox(self.serchAreaMain)
        self.serchInComboBox.setObjectName("serchInComboBox")
        self.serchInComboBox.addItem("")
        self.serchInComboBox.addItem("")
        self.serchInComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.serchInComboBox)

    def serchRadioBox(self):
        self.deepSerchCheckBox = QtWidgets.QCheckBox(self.serchAreaMain)
        self.checkBox = QtWidgets.QFormLayout()
        self.checkBox.setObjectName("checkBox")
        self.deepSerchCheckBox.setObjectName("deepSerchCheckBox")
        self.deepSerchCheckBox.setText("Deep Search")
        self.checkBox.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deepSerchCheckBox)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.checkBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Main Window", "Main Window"))
        self.serchLabel.setText(_translate("MainWindow", "Search"))
        self.serchInLabel.setText(_translate("MainWindow", "Search In"))
        self.serchInComboBox.setItemText(0, _translate("MainWindow", "movies"))
        self.serchInComboBox.setItemText(1, _translate("MainWindow", "series"))
        self.serchInComboBox.setItemText(2, _translate("MainWindow", "stars"))
        self.pushButton.setText(_translate("MainWindow", "Search"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
