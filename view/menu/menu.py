from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from PyQt5 import QtCore, QtWidgets
from core.search import setFactory
from core.PyQt5Helpel import Layout
from core.setWindow import setWindow
from app.db.seaders import initSeader
from core.view import MoviesList,SeriesList,List


initSeader().initNow()

class menu(QMainWindow):
    searchIn='series'
    searchFaze=''
    deepSearch=False
    tags=[]

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
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
        self.buttongroup = QtWidgets.QButtonGroup()
        self.Layout.clear(self.resultArea)

        self.ManuGrid = QtWidgets.QGridLayout(self.centralwidget)
        self.ManuGrid.setContentsMargins(0, 0, 0, 0)
        self.ManuGrid.setObjectName("infoGrid")
        list = setFactory(self.searchIn, self).getFactory()
        self.set_list(list, self.centralwidget, self.ManuGrid)




    def set_list(self,list,grid,el):
        List(self).generate_list(
            'Movies',
            list,
            grid,
            el,
            1,
        )

    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.open(self.buttongroup.button(id).data)

    def open(self,item,setObject=None):
        self.getDataFrom(setObject)
        obj=setWindow(self.searchIn)
        self.window = obj.returnObj(self)
        self.window.menu = self
        self.window.MainWindow=QtWidgets.QMainWindow()
        if self.window.isVisible():
            self.window.hide()
        else:
            self.window.show(item)

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

    def getDataFrom(self,setObject=None):
        self.searchFaze=self.serchLineEdit.text() or None
        if setObject:
            self.searchIn=setObject
        else:
            self.searchIn = self.serchInComboBox.currentText() or None
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
        self.serchInComboBox.setItemText(0, _translate("MainWindow", "series"))
        self.serchInComboBox.setItemText(1, _translate("MainWindow", "stars"))
        self.serchInComboBox.setItemText(2, _translate("MainWindow", "movies"))
        self.pushButton.setText(_translate("MainWindow", "Search"))





app = QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = menu()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()

