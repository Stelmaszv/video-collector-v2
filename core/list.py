from abc import ABC,abstractmethod
from PyQt5 import QtWidgets
from .view import Form

class AbstractList(ABC):

    def __init__(self,BaseView):
        self.BaseView = BaseView
        self.Form=Form(self.BaseView.obj)

    @abstractmethod
    def genrate(self,data,el,grid,col_start):
        pass

class MoviesList (AbstractList):

    def __init__(self, BaseView):
        super(MoviesList, self).__init__(BaseView)
        self.button_group_movies_play = QtWidgets.QButtonGroup()
        self.button_group_movies_info = QtWidgets.QButtonGroup()
        self.Form.buttons_loop= [
            {'button': self.on_movies_info, 'obejct': self.button_group_movies_info},
            {'button': self.on_movies_play, 'obejct': self.button_group_movies_play}
        ]

    def movie_play(self,item):
        self.BaseView.load_view('play', item)

    def movie_info(self,item):
        self.BaseView.load_view('movies', item)

    def on_movies_play(self,id):
        self.BaseView.Form.buttom_genarator(self.button_group_movies_play, self.movie_play, id)
    def on_movies_info(self,id):
        self.BaseView.Form.buttom_genarator(self.button_group_movies_info, self.movie_info, id)

    def genrate(self,data,el,grid,col_start):
        row=1
        for item in data:
            if row <4:
                self.Form.label([str(item.id),item.name],[row,col_start,1,1],grid,el)
                self.Form.button_loop(el, grid, item, [row, col_start+ 1, 1, 1],['info'],0)
                self.Form.button_loop(el, grid, item, [row, col_start +2, 1, 1],['play'],1)
            row=row+1

class SeriesList(AbstractList):

    def __init__(self, BaseView):
        super(SeriesList, self).__init__(BaseView)
        self.button_group_series_info = QtWidgets.QButtonGroup()
        self.Form.buttons_loop= [
            {'button': self.on_series_info, 'obejct': self.button_group_series_info},
        ]

    def on_series_info(self,id):
        self.BaseView.Form.buttom_genarator(self.button_group_series_info, self.series_info, id)

    def series_info(self,item):
        self.BaseView.load_view('series', item)

    def genrate(self,data,el,grid,col_start):
        row = 1
        for item in data:
            if row < 5:
                self.Form.label([str(item.id), item.name], [row, col_start, 1, 1], grid, el)
                self.Form.button_loop(el, grid, item, [row, col_start + 1, 1, 1], ['info'], 0)
            row = row + 1

class StarList(AbstractList):

    def __init__(self,BaseView):
        super(StarList, self).__init__(BaseView)
        self.button_group_stars_info = QtWidgets.QButtonGroup()
        self.Form.buttons_loop= [
            {'button': self.on_stars_info, 'obejct': self.button_group_stars_info},
        ]

    def on_stars_info(self,id):
        self.BaseView.Form.buttom_genarator(self.button_group_stars_info, self.star_info, id)

    def star_info(self,item):
        self.BaseView.load_view('stars', item)

    def genrate(self,data,el,grid,col_start):
        row = 1
        for item in data:
            if row < 5:
                self.Form.label([str(item.id), item.name], [row, col_start, 1, 1], grid, el)
                self.Form.button_loop(el, grid, item, [row, col_start + 1, 1, 1], ['info'], 0)
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
