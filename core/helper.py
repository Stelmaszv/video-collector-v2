from PyQt5.QtWidgets import  QMessageBox
from PyQt5 import QtCore, QtWidgets
from .list import List
from app.db.models import Movies

class Message:

    def show(self,data):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(data[0])
        msg.setInformativeText(data[1])
        msg.setWindowTitle(data[2])
        msg.exec_()

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

    def movie_list(self,list,BaseView):
        BaseView.List.generate_list(
            'movies',
            list,
            self.scrollAreaWidgetContents,
            self.grid_for_scroll_var,
            1,
        )
        self.verticalLayout.addLayout(self.grid_for_scroll_var)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)