from abc import ABC,abstractmethod
from PyQt5 import QtGui,QtCore, QtWidgets
from .list import List
from .view import Pagination,Scroller
from core.strings import stringManipupations

class AbstractSection(ABC):

    @abstractmethod
    def run(self,data,data_list):
        pass

class StarsSection(AbstractSection):

    def __init__(self, BaseView):
        self.BaseView = BaseView
        self.obj =BaseView.obj
        self.List= List(self.BaseView)
        self.pagination = Pagination(self.obj)

    def if_more(self,grid,seriesItem,item):
        if len(item['movies']) > 4:
            more = QtWidgets.QPushButton(grid)
            more.setMinimumSize(QtCore.QSize(30, 0))
            more.setObjectName("InfoButton")
            more.setText("more")
            seriesItem.addWidget(more, 0, 2, 1, 2)

    def avatar(self,grid,seriesItem,item):
        seriesAvatar = QtWidgets.QLabel(grid)
        seriesAvatar.setMaximumSize(QtCore.QSize(100, 100))
        seriesAvatar.setText("")
        seriesAvatar.setPixmap(QtGui.QPixmap(item['avatar']))
        seriesAvatar.setScaledContents(True)
        seriesAvatar.setObjectName("seriesAvatar")
        seriesItem.addWidget(seriesAvatar, 1, 0, 5, 1)

    def seriesItem(self,grid):
        seriesItem = QtWidgets.QGridLayout(grid)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def grid(self,left,top):
        grid = QtWidgets.QWidget(self.addPage)
        grid.setGeometry(QtCore.QRect(left, top, 0, 0))
        grid.setMinimumSize(QtCore.QSize(390, 200))
        grid.setMaximumSize(QtCore.QSize(380, 200))
        grid.setObjectName("gridLayoutWidget_15")
        return grid

    def title(self,grid,seriesItem,item):
        title = QtWidgets.QLabel(grid)
        title.setObjectName("seriesTitle")
        title.setText("<html><head/><body><span style=\" font-size:12pt; font-weight:600; \">" ""
                      + stringManipupations.short(item['name'], 35) +
                      "</span></body></html>")
        seriesItem.addWidget(title, 0, 0, 1, 2)

    def run(self,data,data_list):
        self.tabWidget = self.pagination.tabs([data[0], data[1], data[2], data[2]])
        self.addPage = self.pagination.tab()

        left = 5
        top = 50
        seriesElment = 1

        for item in data_list:
            grid = self.grid(left, top)
            seriesItem = self.seriesItem(grid)
            self.title(grid, seriesItem, item)
            self.avatar(grid, seriesItem, item)
            self.if_more(grid, seriesItem, item)

            self.List.generate_list(
                'movies',
                item['movies'],
                grid,
                seriesItem,
                1,
            )

            left = left + 390

            if seriesElment % 4 == 0:
                top = 280
                left = 5

            if seriesElment % 8 == 0:
                top = 50
                left = 5
                self.addPage = self.pagination.tab()
                self.tabWidget.addTab(self.addPage, "2")

            seriesElment = seriesElment +1

        self.tabWidget.addTab(self.addPage, "1")

class SeriesSection(AbstractSection):

    def __init__(self, BaseView):
        self.obj = BaseView.obj
        self.data= BaseView.data
        self.BaseView=BaseView
        self.Scroller = Scroller(self.obj)
        self.pagination = Pagination(self.obj)

    def info(self):
        data   = [100,300,300,200]
        rows = ['itemNmae','itemName2']
        info_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]
        self.BaseView.info(info_data,data,rows,self.tab)

    def seriesItem(self,grid):
        seriesItem = QtWidgets.QGridLayout(grid)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def run(self,data,data_list):
        self.tabWidget = self.pagination.tabs([500, 100, 1200, 900])
        self.tab = self.pagination.tab()

        src = 'C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg'
        self.BaseView.avatar([50, 50, 250, 250], self.tab, src)
        self.info()
        self.BaseView.galery([50, 520, 300, 200],[100,100],3,self.tab)

        self.Scroller.run([400, 10, 780, 850], self.tab)

        self.Scroller.movie_list(
            self.data.movies,
            self.BaseView
        )

        self.tabWidget.addTab(self.tab, "Seson 1")

class MenuSection(AbstractSection):
    def __init__(self, BaseView):
        self.obj = BaseView.obj
        self.BaseView = BaseView
        self.Scroller = Scroller(self.obj)
        self.List = List(self.BaseView)
        self.pagination = Pagination(self.obj)

    def scroll_area_widget_contents(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.obj)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

    def grid_for_scroll(self):
        self.grid_for_scroll_obj = QtWidgets.QGridLayout(self.obj)
        self.grid_for_scroll_obj.setObjectName("gridLayout")

    def grid(self):
        seriesItem = QtWidgets.QGridLayout(self.tab)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def run(self, data, data_list):
        self.tabWidget = self.pagination.tabs([0, 200, 400, 800])
        self.tab = self.pagination.tab()
        grid=self.grid()

        self.List.generate_list(
            self.BaseView.menu.searchIn,
            data_list,
            self.tab,
            grid,
            0,
        )

        self.tabWidget.addTab(self.tab, "Page 1")