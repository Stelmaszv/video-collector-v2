from abc import ABC,abstractmethod
from PyQt5 import QtGui,QtCore, QtWidgets

class AbstractList(ABC):

    count=0
    run=0

    @abstractmethod
    def genrate(self,data,el,grid,col_start):
        pass

    def buttom_genarator(self,list,fuction,id):
        for button in list.buttons():
            if button is list.button(id):
                fuction(list.button(id).data)

    def label(self,el,grid,item,data):
        label = QtWidgets.QLabel(el)
        label.setObjectName("label")
        label.setText(item.name)
        grid.addWidget(label, data[0], data[1], data[2], data[3])

    def if_run(self):
        count=0
        for item in self.ids:
            if item == self.run:
                count = count + 1

        if count == 1:
            return True

    def button(self, el, grid, item, data, info, index):
        button = QtWidgets.QPushButton(el)
        button.setMinimumSize(QtCore.QSize(30, 0))
        button.setMaximumSize(QtCore.QSize(10, 16777215))
        button.setObjectName("InfoButton")
        button.setText(info[0])
        button.data = item
        grid.addWidget(button, data[0], data[1], data[2], data[3])
        self.buttons[index]['obejct'].addButton(button)
        self.buttons[index]['obejct'].buttonClicked[int].connect(self.buttons[index]['button'])

class MoviesList (AbstractList):

    def __init__(self,menu):
        self.menu=menu
        self.button_group_movies_play = QtWidgets.QButtonGroup()
        self.button_group_movies_info = QtWidgets.QButtonGroup()
        self.buttons= [
            {'button': self.on_movies_info, 'obejct': self.button_group_movies_info},
            {'button': self.on_movies_play, 'obejct': self.button_group_movies_play}
        ]

    def movie_play(self,item):

        #print('movie play ' + str(item.data))
        self.menu.load_view('play', item)

    def movie_info(self,item):
        self.menu.load_view('movies',item)

    def on_movies_play(self,id):
       self.buttom_genarator(self.button_group_movies_play, self.movie_play, id)

    def on_movies_info(self,id):
        self.buttom_genarator(self.button_group_movies_info, self.movie_info, id)

    def genrate(self,data,el,grid,col_start):
        row=1
        for item in data:
            if row <4:
                self.label(el,grid,item,[row,col_start,1,1])
                self.button(el, grid, item, [row, col_start+ 1, 1, 1],['info'],0)
                self.button(el, grid, item, [row, col_start +2, 1, 1],['play'],1)
            row=row+1

class SeriesList(AbstractList):

    def __init__(self,menu):
        self.menu=menu
        self.button_group_series_info = QtWidgets.QButtonGroup()
        self.buttons= [
            {'button': self.on_series_info, 'obejct': self.button_group_series_info},
        ]

    def on_series_info(self,id):
        self.buttom_genarator(self.button_group_series_info, self.series_info, id)

    def series_info(self,item):
        self.menu.load_view('series',item)

    def genrate(self,data,el,grid,col_start):
        row = 1
        for item in data:
            if row < 5:
                self.label(el, grid, item, [row, col_start, 1, 1])
                self.button(el, grid, item, [row, col_start + 1, 1, 1], ['info'], 0)
            row = row + 1

class StarList(AbstractList):

    def __init__(self,menu):
        self.menu=menu
        self.button_group_stars_info = QtWidgets.QButtonGroup()
        self.buttons= [
            {'button': self.on_stars_info, 'obejct': self.button_group_stars_info},
        ]

    def on_stars_info(self,id):
        self.buttom_genarator(self.button_group_stars_info, self.star_info, id)

    def star_info(self,item):
        self.menu.load_view('stars',item)

    def genrate(self,data,el,grid,col_start):
        row = 1
        for item in data:
            if row < 5:
                self.label(el, grid, item, [row, col_start, 1, 1])
                self.button(el, grid, item, [row, col_start + 1, 1, 1], ['info'], 0)
            row = row + 1

class List:

    def __init__(self,obj):
        self.obj=obj

    def generate_list(self,place,list,el,grid,col):

        switcher = {
            'movies' : MoviesList(self.obj),
            'series' : SeriesList(self.obj),
            'stars'  : StarList(self.obj)
        }

        classObj = switcher.get(place, "Invalid data");
        classObj.genrate(list,el,grid,col)
