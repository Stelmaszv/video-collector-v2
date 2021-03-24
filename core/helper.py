from PyQt5.QtWidgets import  QMessageBox,QDialog
from PyQt5 import QtCore, QtWidgets
from sys import exit as sysExit
from .list import List
from app.db.models import Movies

class QueryCounter:

    def __init__(self,query,per_page):
        self.query=query;
        self.per_page=per_page
        self.page_count=query.count()

    def if_page_exist(self,page):
        if page in range(0,int(self.page_count/self.per_page)):
            return True
        return False

class Message:

    rezolution_index = []

    def set_resolution(self,data):
        self.rezolution_index=data

    def show(self,data):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(data[0])
        msg.setInformativeText(data[1])
        msg.setWindowTitle(data[2])
        msg.exec_()

    def dialog(self,text):

        d = QDialog()
        b1 =  QtWidgets.QPushButton("ok", d)
        l  =  QtWidgets.QLabel(text,d)
        d.setGeometry(100,100,1000,1000)
        l.move(0,0)
        b1.move(50, 50)
        d.setWindowTitle("Dialog")
        d.exec_()

class Pagination:


    def __init__(self,obj):
        self.obj=obj

    def tabs(self,data):
        tab = QtWidgets.QTabWidget(self.obj)
        tab.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        tab.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        tab.setObjectName("tabWidget")
        return tab

    def tab(self):
        tab = QtWidgets.QWidget()
        tab.setObjectName("tab")
        return tab

class Scroller:

    def __init__(self,obj):
        self.obj=obj

    def scroll_area(self,data,obj=None):
        if self.obj == None:
            obj=self.obj

        scroll_area_obj = QtWidgets.QScrollArea(obj)
        scroll_area_obj.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        scroll_area_obj.setWidgetResizable(True)
        scroll_area_obj.setObjectName("scrollArea")
        return  scroll_area_obj

    def scroll_area_widget_contents(self):
        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 499))
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        return scrollAreaWidgetContents

    def grid_for_scroll (self):
        grid_for_scroll_obj = QtWidgets.QGridLayout()
        grid_for_scroll_obj.setObjectName("gridLayout")
        return grid_for_scroll_obj

    def vertical_layout(self,obj):
        vertical_Layout_grid = QtWidgets.QVBoxLayout(obj)
        vertical_Layout_grid.setObjectName("verticalLayout")
        return vertical_Layout_grid

    def run(self,data,obj):
        self.scrollArea = self.scroll_area([data[0], data[1], data[2], data[3]], obj)
        self.scrollAreaWidgetContents = self.scroll_area_widget_contents()
        self.verticalLayout = self.vertical_layout(self.scrollAreaWidgetContents)
        self.grid_for_scroll_var = self.grid_for_scroll()

    def movie_list(self,list,BaseView,searchIn):
        BaseView.List.generate_list(
            searchIn,
            list,
            self.scrollAreaWidgetContents,
            self.grid_for_scroll_var,
            1,
        )
        self.verticalLayout.addLayout(self.grid_for_scroll_var)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)



