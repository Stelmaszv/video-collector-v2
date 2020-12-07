from abc import ABC,abstractmethod
from PyQt5 import QtGui,QtCore, QtWidgets
from .list import List
from core.strings import stringManipupations
from .helper import Pagination, Scroller
from .view import Form

class AbstractSection(ABC):

    @abstractmethod
    def run(self,data,data_list,page):
        pass

class StarsSection(AbstractSection):


    def __init__(self, BaseView):
        self.BaseView = BaseView
        self.obj =BaseView.obj
        self.List= List(self.BaseView,25)
        self.pagination = Pagination(self.obj)
        self.button_group_info = QtWidgets.QButtonGroup()
        self.Form = Form(self.BaseView.obj)
        self.Form.buttons_loop= [
            {'button': self.on_info_button, 'obejct': self.button_group_info },
        ]

    def on_info_button(self,id):
        self.Form.buttom_genarator(self.button_group_info , self.info_button, id)

    def info_button(self,data):
        self.BaseView.load_view('movie_list', data)

    def more(self,grid,seriesItem,item,left,top):
        button = QtWidgets.QPushButton(self.addPage)
        button.setObjectName("show-movies")
        button.setText('Show Movies')
        button.setGeometry(left+20,top+200, 130,50)
        button.data = item
        self.Form.buttons_loop[0]['obejct'].addButton(button)
        self.Form.buttons_loop[0]['obejct'].buttonClicked[int].connect(self.Form.buttons_loop[0]['button'])

    def avatar(self,grid,seriesItem,item):
        seriesAvatar = QtWidgets.QLabel(grid)
        seriesAvatar.setMaximumSize(QtCore.QSize(150, 150))
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

    def run(self, data, data_list, page):
        self.tabWidget = self.pagination.tabs([80, 430, 1080, 500])
        self.addPage = self.pagination.tab()
        left = 5
        top = 50
        seriesElment = 1
        for item in data_list:
            grid = self.grid(left, top)
            seriesItem = self.seriesItem(grid)
            self.title(grid, seriesItem, item)
            self.avatar(grid, seriesItem, item)
            self.more(grid, seriesItem, item,left,top)
            left = left + 200
        self.tabWidget.addTab(self.addPage, "1")
        print('run')
        """
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
        """

class SeriesSection(AbstractSection):

    per_page = 25

    def __init__(self, BaseView):
        self.obj = BaseView.obj
        self.data= BaseView.data
        self.BaseView=BaseView
        self.List = List(self.BaseView, self.per_page)
        self.Scroller = Scroller(self.obj)
        self.Pagination = Pagination(self.obj)

    def info(self,tab):
        data   = [100,300,300,200]
        rows = ['itemNmae','itemName2']
        info_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]
        self.BaseView.info(info_data,data,rows,tab)

    def seriesItem(self,grid):
        seriesItem = QtWidgets.QGridLayout(grid)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def run(self, data, data_list, page):
        pages = self.data.sezons
        self.tabWidget = self.Pagination.tabs([data[0], data[1], data[2], data[3]])
        for item in range(1, pages + 1):
            movies = self.faind_movies_with_sezon(self.data.movies, item)
            tab = self.Pagination.tab()
            src = 'C:/Users/DeadlyComputer/Desktop/photo/5c8df35745d2a09e00a18c36.jpg'
            self.BaseView.avatar([50, 50, 250, 250], tab, src)
            self.info(tab)
            self.Scroller.run([400, 10, 780, 850], tab)
            self.Scroller.movie_list(
                movies,
                self,
                'movies'
            )
            self.tabWidget.addTab(tab, str(item))


    def faind_movies_with_sezon(self,arry,page):
        movies_in_sezon=[]
        for movie in arry:
            if movie.sezon == page:
                movies_in_sezon.append(movie)

        return movies_in_sezon

class MovieListSection(AbstractSection):

    per_page = 50

    def __init__(self, BaseView):
        self.obj = BaseView.obj
        self.BaseView = BaseView
        self.Scroller = Scroller(self.obj)
        self.List = List(self.BaseView,self.per_page)
        #self.Pagination = Pagination(self.obj)

    def run(self, data, data_list, page):
        self.Scroller.run([400, 10, 780, 850],self.obj)
        self.Scroller.movie_list(
            data_list,
            self,
            'movies'
        )

class MenuSection(AbstractSection):

    per_page=50

    def __init__(self, BaseView):
        self.obj = BaseView.obj
        self.BaseView = BaseView
        self.Scroller = Scroller(self.obj)
        self.List = List(self.BaseView,self.per_page)
        self.Pagination = Pagination(self.obj)

    def scroll_area_widget_contents(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.obj)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

    def grid_for_scroll(self):
        self.grid_for_scroll_obj = QtWidgets.QGridLayout(self.obj)
        self.grid_for_scroll_obj.setObjectName("gridLayout")

    def grid(self,tab):
        seriesItem = QtWidgets.QGridLayout(tab)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def run(self, data, data_list,page):
        start = self.return_start_page(page)
        end = self.return_end_page(start,page)
        self.Scroller.run([data[0], data[1], data[2], data[3]], self.obj)
        self.Scroller.movie_list(
            data_list[start:end],
            self,
            self.obj.searchIn
        )

    def return_start_page(self,page):
        if page<0:
            return 0
        else:
            return page*25

    def return_end_page(self,start,page):
        if page>0:
            return start+self.per_page;
        return self.per_page
