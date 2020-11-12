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
        self.scrollArea = self.scroll_area([400, 10, 780, 850], obj)
        self.scrollAreaWidgetContents = self.scroll_area_widget_contents()
        self.verticalLayout = self.vertical_layout(self.scrollAreaWidgetContents)
        self.grid_for_scroll = self.grid_for_scroll()

    def movie_list(self,list,buttons):

        row=0
        for item in list:
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setObjectName("label")
            label.setText(item.name)
            self.grid_for_scroll.addWidget(label, row, 0, 1, 1)

            pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            pushButton.setObjectName("pushButton")
            pushButton.setText('info')
            pushButton.data=item
            self.grid_for_scroll.addWidget(pushButton, row, 1, 1, 1)
            buttons[0]['obejct'].addButton(pushButton)
            buttons[0]['obejct'].buttonClicked[int].connect(buttons[0]['button'])

            pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            pushButton_2.setObjectName("pushButton_2")
            pushButton_2.setText('play')
            pushButton_2.data = item
            buttons[1]['obejct'].addButton(pushButton_2)
            buttons[1]['obejct'].buttonClicked[int].connect(buttons[1]['button'])
            self.grid_for_scroll.addWidget(pushButton_2, row, 2, 1, 1)
            row=row+1

        self.verticalLayout.addLayout(self.grid_for_scroll)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

class Pagination:

    def __init__(self,obj):
        self.obj=obj

    def tabs(self,data):
        tab = QtWidgets.QTabWidget(self.obj)
        tab.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        tab.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        tab.setObjectName("tabWidget")
        return tab

    def paginate(self,type,obj):
        switcher = {
            'seriesPaginator' : SeriesPaginator(obj)
        }
        classObj = switcher.get(type, "Invalid data");
        return classObj.paginate()

    def tab(self):
        tab = QtWidgets.QWidget()
        tab.setObjectName("tab")
        return tab

class SeriesList:

    def __init__(self, BaseView):
        self.obj = BaseView.obj
        self.data= BaseView.data
        self.BaseView=BaseView
        self.Scroller = Scroller(self.obj)
        self.pagination = Pagination(self.obj)
        self.button_group_movies_play = QtWidgets.QButtonGroup()
        self.button_group_movies_info = QtWidgets.QButtonGroup()

    def info(self):
        data   = [100,300,300,200]
        rows = ['itemNmae','itemName2']
        info_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]
        self.BaseView.info(info_data,data,rows,self.tab)

    def movie_play(self,item):
        print('movie play ' + str(item.data))

    def movie_info(self,item):
        print('movie info ' + str(item.data))

    def run(self):
        def on_movies_play(id):
           self.BaseView.buttom_genarator(self.button_group_movies_play, self.movie_play, id)

        def on_movies_info(id):
            self.BaseView.buttom_genarator(self.button_group_movies_info, self.movie_info, id)

        self.tabWidget = self.pagination.tabs([500,100,1200,900])
        self.tab = self.pagination.tab()

        src = 'C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg'
        self.BaseView.avatar([50, 50, 250, 250], self.tab, src)
        self.info()
        self.BaseView.galery([50, 520, 300, 200],[100,100],3,self.tab)

        self.Scroller.run([400, 10, 780, 850], self.tab)
        self.Scroller.movie_list(
            self.data.movies,
            [
             {'button': on_movies_info,  'obejct': self.button_group_movies_info},
             {'button': on_movies_play,  'obejct': self.button_group_movies_play}
            ]
        )
        self.tabWidget.addTab(self.tab, "Seson 1")

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
        self.Scroller=Scroller(self.obj)

    def buttom_genarator(self,list,fuction,id):
        for button in list.buttons():
            if button is list.button(id):
                fuction(list.button(id))

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

    def get_movie(self,data, data_list):
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

    def get_movies(self, data, data_list):
        def movie_play(item):
            print('movie play ' + str(item.data))

        def movie_info(item):
            print('movie info ' + str(item.data))

        def on_movies_play(id):
           self.buttom_genarator(self.button_group_movies_play, movie_play, id)

        def on_movies_info(id):
            self.buttom_genarator(self.button_group_movies_info, movie_info, id)

        self.button_group_movies_play = QtWidgets.QButtonGroup()
        self.button_group_movies_info = QtWidgets.QButtonGroup()

        self.tabWidget = self.pagination.tabs(data)

        self.tab = self.pagination.tab()


        #scoroller

        self.scrollArea = self.Scroller.scroll_area([400, 10, 780, 850], self.tab)

        self.scrollAreaWidgetContents = self.Scroller.scroll_area_widget_contents()

        self.verticalLayout= self.Scroller.vertical_layout(self.scrollAreaWidgetContents)


        self.grid_for_scroll = self.Scroller.grid_for_scroll()

        self.Scroller.movie_list(
            self.scrollAreaWidgetContents,
            self.grid_for_scroll,
            self.verticalLayout,
            self.scrollArea,
            self.data.movies,
            [
             {'button': on_movies_info,  'obejct': self.button_group_movies_info},
             {'button': on_movies_play,  'obejct': self.button_group_movies_play}
            ]
        )

        src='C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg'
        self.avatar([50, 50, 250, 250],self.tab,src)

        data   = [100,300,300,200]

        rows = ['itemNmae','itemName2']

        info_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        data2 = [50, 520, 300, 200]

        self.info(info_data,data,rows,self.tab)
        self.galery(data2,[100,100],3,self.tab)

        self.tabWidget.addTab(self.tab, "Seson 1")

    def listView(self, data, data_list,obj_name):

        switcher = {
            'Stars'    : self.get_stars,
            'Movies'   : SeriesList,
        }

        classObj = switcher.get(obj_name, "Invalid data");
        classObj(self).run()


    def title(self,data,text):
        self.title = QtWidgets.QLabel(self.obj)
        self.title.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.title.setObjectName("title")
        self.title.setText(text)

    def avatar(self,data,obj=None,src=None):
        if obj == None:
            obj = self.obj
        if src == None:
            src = self.data.avatar
        self.avatar_photo = QtWidgets.QLabel(obj)
        self.avatar_photo.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.avatar_photo.setText("")
        self.avatar_photo.setPixmap(QtGui.QPixmap(src))
        self.avatar_photo.setScaledContents(True)
        self.avatar_photo.setObjectName("avatar")

    def info(self,infoData,data,rows,obj=None):
        if obj==None:
            obj=self.obj
        self.infoWidget = QtWidgets.QWidget(obj)
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

    def galery(self,data,size,inRow,obj=None,photos=None):
        if photos == None:
            photos = self.data.photos
        if obj == None:
            obj = self.obj

        self.galeryGrid = QtWidgets.QWidget(obj)
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
