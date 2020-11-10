from PyQt5 import QtGui,QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget,QPushButton
from app.db.models import session
from core.strings import stringManipupations
from abc import ABC,abstractmethod

class AbstractPaginator(ABC):

    def __init__(self,obj):
        super(AbstractPaginator, self).__init__()
        self.obj=obj

    @abstractmethod
    def paginate(self):
        pass

class SeriesPaginator(AbstractPaginator):

    def paginate(self):

        left = 5
        top = 50
        seriesElment = 1

        for item in self.obj.seriesList:
            grid = self.grid(left,top)
            seriesItem = self.seriesItem(grid)
            self.title(grid,seriesItem,item)
            self.avatar(grid, seriesItem, item)
            self.if_more(grid, seriesItem, item)
            self.moviesList(grid,seriesItem,item)

            left = left + 390

            if seriesElment % 4 == 0:
                top = 280
                left = 5

            if seriesElment % 8 == 0:
                top = 50
                left = 5
                self.newPage = QtWidgets.QWidget()
                self.newPage.setObjectName("tabWidgetPage1")
                self.addPage = self.newPage
                self.tab.addTab(self.addPage, "")

            seriesElment = seriesElment + 1

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

    def moviesList(self,grid,seriesItem,item):
        row=1

        for el in item['movies']:
            if row < 6:
                name = QtWidgets.QLabel(grid)
                name.setMaximumSize(QtCore.QSize(10000000, 16777215))
                name.setObjectName("nameLabel")
                name.setText(el.name)
                seriesItem.addWidget(name, row, 1, 1, 1)

                info = QtWidgets.QPushButton(grid)
                info.setMinimumSize(QtCore.QSize(30, 0))
                info.setMaximumSize(QtCore.QSize(10, 16777215))
                info.setObjectName("InfoButton")
                info.setText("Info")
                seriesItem.addWidget(info, row, 3, 1, 1)

                play = QtWidgets.QPushButton(grid)
                play.setMinimumSize(QtCore.QSize(30, 0))
                play.setMaximumSize(QtCore.QSize(10, 16777215))
                play.setObjectName("playButton")
                play.setText("play")
                seriesItem.addWidget(play, row, 2, 1, 1)

                row = row + 1

    def seriesItem(self,grid):
        seriesItem = QtWidgets.QGridLayout(grid)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def grid(self,left,top):
        grid = QtWidgets.QWidget(self.obj.addPage)
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

class Pagination:

    def __init__(self,obj):
        self.obj=obj

    def tabs(self,data):
        tab = QtWidgets.QTabWidget(self.obj)
        tab.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        tab.setObjectName("tabWidget")
        return tab

    def paginate(self,type,obj):
        switcher = {
            'seriesPaginator' : SeriesPaginator(obj)
        }
        classObj = switcher.get(type, "Invalid data");
        return classObj.paginate()

class List:

    def __init__(self,obj):
        self.obj=obj

    def generate_grid_for_list(self,data):
        self.object_data=data
        self.grid_for_list = QtWidgets.QWidget(self.obj)
        self.grid_for_list.setGeometry(QtCore.QRect(self.object_data[0], self.object_data[1], self.object_data[2], self.object_data[3]))
        self.grid_for_list.setObjectName("infoWidget")

    def grid_info(self):
        self.info_grid = QtWidgets.QGridLayout(self.grid_for_list)
        self.info_grid.setContentsMargins(0, 0, 0, 0)
        self.info_grid.setObjectName("infoGrid")

    def generate_Loop(self, data, data_list, obj):
        self.buttongroup = QtWidgets.QButtonGroup()
        self.generate_grid_for_list(data)
        self.grid_info()
        row = 0

        for item in data_list:
            obj(item, row,self)
            row = row + 1

class baseView:

    def __init__(self,data,obj):
        self.data=data
        self.model=obj.model
        self.obj=obj.obj
        self.pagination = Pagination(self.obj)
        self.menu=obj.menu
        self.list=List(self.obj)

    def buttom_genarator(self,list,fuction,id):
        for button in list.buttons():
            if button is list.button(id):
                fuction(list.button(id).data)

    def generate_Loop(self, data, data_list, obj):
        self.list.generate_Loop(data, data_list, obj)

    def create_pagination(self):

        self.tab = Pagination(self.obj).tabs([600,100,1200,900])

        self.starPage = QtWidgets.QWidget()
        self.starPage.setObjectName("tabWidgetPage1")
        self.addPage=self.starPage
        self.tab.addTab(self.addPage, "")

        self.NPage = QtWidgets.QWidget()
        self.NPage.setObjectName("tabWidgetPage1")
        self.tab.addTab(self.NPage, "")

    def get_movies(self,data, data_list):
        self.create_pagination()

        self.button_group_movies_play = QtWidgets.QButtonGroup()
        self.button_group_movies_info = QtWidgets.QButtonGroup()

        def grid(left, top):
            grid = QtWidgets.QWidget(self.addPage)
            grid.setGeometry(QtCore.QRect(left, top, 0, 0))
            grid.setMinimumSize(QtCore.QSize(390, 200))
            grid.setMaximumSize(QtCore.QSize(380, 200))
            grid.setObjectName("gridLayoutWidget_15")
            return grid

        def movie_play(item):
            print('movie play ' + str(item))

        def movie_info(item):
            print('movie info '+str(item))

        def on_movies_play(id):
            self.buttom_genarator(self.button_group_movies_play, movie_play, id)

        def on_movies_info(id):
            self.buttom_genarator(self.button_group_movies_info, movie_info, id)


        grid=grid(0,0)

        def abstrat_row(item, row, obj):
            col1 = QtWidgets.QLabel(grid)
            col1.setMinimumSize(QtCore.QSize(1400000, 0))
            col1.setMaximumSize(QtCore.QSize(1400000, 16777215))
            col1.setObjectName("col1")

            if obj.object_data[2] > 400:
                col1.setText(stringManipupations.short(item.name, 35))
            else:
                col1.setText(item.name)

            obj.info_grid.addWidget(col1, row, 0)

            el = QtWidgets.QPushButton(grid)
            el.setMinimumSize(QtCore.QSize(30, 0))
            el.setMaximumSize(QtCore.QSize(10, 16777215))
            el.setObjectName(item.name)
            el.setText('info')
            el.data = item

            self.button_group_movies_info.addButton(el)
            obj.info_grid.addWidget(el, row, 1)
            self.button_group_movies_info.buttonClicked[int].connect(on_movies_info)

            el = QtWidgets.QPushButton(grid)
            el.setMinimumSize(QtCore.QSize(30, 0))
            el.setMaximumSize(QtCore.QSize(10, 16777215))
            el.setObjectName(item.name)
            el.setText('play')
            el.data = item

            self.button_group_movies_play.addButton(el)
            obj.info_grid.addWidget(el, row, 2)
            self.button_group_movies_play.buttonClicked[int].connect(on_movies_play)

        self.generate_Loop(data, data_list, abstrat_row)

    def get_stars(self, data, data_list):

        self.button_group_for_star_info = QtWidgets.QButtonGroup()

        def open_view(item):
            print('star info '+str(item))

        def on_button_clicked(id):
            self.buttom_genarator(self.button_group_for_star_info, open_view, id)

        def abstrat_row(item, row, obj):

            col1 = QtWidgets.QLabel()
            col1.setMinimumSize(QtCore.QSize(1400000, 0))
            col1.setMaximumSize(QtCore.QSize(1400000, 16777215))
            col1.setObjectName("col1")

            if obj.object_data[2] > 400:
                col1.setText(stringManipupations.short(item.name, 35))
            else:
                col1.setText(item.name)

            obj.info_grid.addWidget(col1, row, 0, 2, 2)

            el = QtWidgets.QPushButton()
            el.setMinimumSize(QtCore.QSize(30, 0))
            el.setMaximumSize(QtCore.QSize(10, 16777215))
            el.setObjectName(item.name)
            el.setText('info')
            el.data = item

            self.button_group_for_star_info.addButton(el)
            obj.info_grid.addWidget(el, row, 1, 2, 2)
            self.button_group_for_star_info.buttonClicked[int].connect(on_button_clicked)

        self.generate_Loop(data, data_list, abstrat_row)

    def listView(self, data, data_list,obj_name):

        switcher = {
            'Stars'  : self.get_stars,
            'Movies' : self.get_movies
        }
        classObj = switcher.get(obj_name, "Invalid data");
        classObj(data, data_list)

    def title(self,data,text):
        self.title = QtWidgets.QLabel(self.obj)
        self.title.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.title.setObjectName("title")
        self.title.setText(text)

    def avatar(self,data):
        self.avatar = QtWidgets.QLabel(self.obj)
        self.avatar.setGeometry(QtCore.QRect(data[0],data[1],data[2],data[3]))
        self.avatar.setText("")
        self.avatar.setPixmap(QtGui.QPixmap(self.data.avatar))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")

    def info(self,infoData,data,rows):
        self.infoWidget = QtWidgets.QWidget(self.obj)
        self.infoWidget.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.infoWidget.setObjectName("infoWidget")
        self.infoGrid = QtWidgets.QGridLayout(self.infoWidget)
        self.infoGrid.setContentsMargins(0, 0, 0, 0)
        self.infoGrid.setObjectName("infoGrid")

        row=0

        for item in infoData:

            col1 = QtWidgets.QLabel(self.infoWidget)
            col1.setObjectName("col1")
            col1.setText(item[rows[0]])
            self.infoGrid.addWidget(col1, row, 0,2, 2)

            col2 = QtWidgets.QLabel(self.infoWidget)
            col2.setObjectName("col2")
            col2.setText(item[rows[1]])
            self.infoGrid.addWidget(col2, row, 1, 2, 2)

            row=row+1

    def galery(self,data,size,inRow):
        photos = self.data.photos
        self.galeryGrid = QtWidgets.QWidget(self.obj)
        self.galeryGrid.setGeometry(QtCore.QRect(data[0],data[1],data[2],data[3]))
        self.galeryGrid.setObjectName("galeryGrid")

        self.galeryGrid2 = QtWidgets.QGridLayout(self.galeryGrid)
        self.galeryGrid2.setContentsMargins(0, 0, 0, 0)
        self.galeryGrid2.setObjectName("galeryGrid2")
        row = 0
        col = 0
        for photo in photos:
            item = QtWidgets.QLabel(self.galeryGrid)
            item.setMaximumSize(QtCore.QSize(size[0], size[1]))
            item.setText("")
            item.setPixmap(QtGui.QPixmap(photo.src))
            item.setScaledContents(True)
            item.setObjectName("galeryItem")
            self.galeryGrid2.addWidget(item, col, row, 1, 1)
            row = row + 1
            if row > inRow:
                row = 0
                col = col + 1

class abstractView(QWidget):

    def __init__(self):
        super(abstractView, self).__init__()

    def getOne(self):
        self.data=session.query(self.model).get(self.id)

    def setupUi(self):
        pass

    def createObj(self):
        self.obj = QtWidgets.QMainWindow()
        self.obj.setObjectName("StarList")
        self.obj.resize(1920, 1080)

    def show(self,data):

        self.id = data.id
        self.createObj()

        self.setBaseView(data,self)
        self.getOne()
        self.setupUi()
        QtCore.QMetaObject.connectSlotsByName(self.obj)
        self.obj.show()

    def setBaseView(self,data,obj):
        self.baseView = baseView(data,obj)
