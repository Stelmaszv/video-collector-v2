import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMenu, QAction,QMainWindow,QLabel
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from core.view import BaseView
from core.search import setFactory
from app.db.seaders import initSeader

#initSeader().initNow()
class Menu(QMainWindow):
    deepSearch = False
    searchFaze = ''
    searchIn = 'movies'

    def __init__(self,data=False):
        super().__init__()
        self.window_title = 'Menu'
        self.left = 30
        self.top = 20
        self.width = 1320
        self.height = 1200
        self.model=''
        self.BaseView=BaseView([], self)
        self.initUI(data)
        self.windows_opens=[]

    def search_box(self):
        data = [0, 150, 200, 50]
        list = ['movies','series','stars']
        self.search_in_combo_box=self.BaseView.form.combo_box(data, list)
        data_search_button = [200,150,200,50]
        data_button_info=['serch003','search']
        self.BaseView.form.button(data_button_info, data_search_button, self.click_search)
        data_line = [0,100,400,50]
        self.search_button_edit_line=self.BaseView.form.edit_line(data_line, 'search Faze')

    def click_search(self):
        self.close()
        self.searchIn = self.search_in_combo_box.currentText()
        self.searchFaze = self.search_button_edit_line.text()
        Menu([self.searchIn,self.searchFaze])

    def title(self):
        data = [0, 0, 400 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">search</span></p></body></html>"
        self.BaseView.title(data, text)

    def list_view(self):
        data = [500, 100, 1200, 900]
        self.BaseView.menu.searchIn=self.searchIn
        list = setFactory(self).getFactory(self.BaseView.menu.searchIn)
        self.BaseView.listView(data, list, 'Menu')

    def set_up(self,data):
        self.searchIn=data[0]
        self.searchFaze=data[1]

    def initUI(self,data=False):
        if data:
            self.set_up(data)
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.search_box()
        self.title()
        self.menu()
        self.list_view()
        self.show()

    def menu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Add')
        newAct = QAction('new movie', self)
        newAct.triggered.connect(self.add_new_movie)
        fileMenu.addAction(newAct)

    def add_new_movie(self):
        self.BaseView.load_view('add_movie')

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        print(self.BaseView)



















"""
class Menu(AbstractView):
    model = False
    searchIn = 'series'
    deepSearch=False
    searchFaze=''
    width_val=400
    height_val= 1000
    widows_array=[]

    def closeEvent(self, event):
        print(event)

    def title(self):
        data = [0, 0, 400 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">search</span></p></body></html>"
        self.baseView.title(data,text)

    def search_box(self):
        data = [0, 150, 200, 50]
        list = ['movies','series','stars']
        self.baseView.form.combo_box(data, list)
        data_search_button = [200,150,200,50]
        data_button_info=['serch003','search']
        self.baseView.form.button(data_button_info,data_search_button,self.click_search)
        data_line = [0,100,400,50]
        self.baseView.form.edit_line(data_line)

    def list_view(self):
        data = [500, 100, 1200, 900]
        list = setFactory(self).getFactory(self.searchIn)
        self.baseView.listView(data, list, 'Menu')

    def set_list(self,list,grid,el):

        List(self).generate_list(
            self.searchIn,
            list,
            grid,
            el,
            1
        )

    def click_search(self):
        print('dqwdqwd')
        self.hide()

    def load_view(self):
        print('fwef')


    def setupUi(self):
        self.title()
        self.search_box()
        self.list_view()

    def getDataFrom(self,setObject=None):
        self.searchFaze=self.serchLineEdit.text() or None
        if setObject:
            self.searchIn=setObject
        else:
            self.searchIn = self.serchInComboBox.currentText() or None
        self.deepSearch=self.deepSerchCheckBox.isChecked()
        self.searchResult()

    def open(self, item, view,id):
        if id != 0:
            self.widows_array.append({'view': view, 'id': id})
        #self.getDataFrom(view)
        obj=setWindow(self.searchIn)
        self.window = obj.returnObj(self)

        if self.if_window_active(view,id):
            self.window.show(item.data)
        else:
            self.window.obj.hide()

    def if_window_active(self,view,id):
        count=0
        for item in self.widows_array:
            if item['view'] == view and item['id']==id:
                count=count+1

        print(count)

        if count==0:
            return True
        return  False

"""

"""
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

        menu_grid = QtWidgets.QGridLayout(self.centralwidget)
        menu_grid.setGeometry(QtCore.QRect(10, 150, 381, 841))
        menu_grid.setObjectName("infoGrid")

        list = setFactory(self.searchIn, self).getFactory()

        self.set_list(list, self.serchAreaMain, menu_grid)

    def set_list(self,list,grid,el):

        List(self).generate_list(
            self.searchIn,
            list,
            grid,
            el,
            1
        )

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
        print(self.isVisible())

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
        self.serchInComboBox.setItemText(0, _translate("MainWindow", "movies"))
        self.serchInComboBox.setItemText(1, _translate("MainWindow", "stars"))
        self.serchInComboBox.setItemText(2, _translate("MainWindow", "series"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
"""


