from abc import ABC,abstractmethod
from PyQt5 import QtWidgets
from .view import Form

class AbstractList(ABC):

    def __init__(self,BaseView,per_page):
        self.BaseView = BaseView
        self.per_page=per_page
        self.Form=Form(self.BaseView.obj)

    @abstractmethod
    def genrate(self,data,el,grid,col_start):
        pass

class MoviesList (AbstractList):

    def __init__(self, BaseView,per_page):
        super(MoviesList, self).__init__(BaseView,per_page)
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
            self.Form.label([str(item.id),item.name],[row,col_start,1,1],grid,el)
            self.Form.button_loop(el, grid, item, [row, col_start+ 1, 1, 1],['info'],0)
            #self.Form.button_loop(el, grid, item, [row, col_start +2, 1, 1],['play'],1)
            row=row+1

class SeriesList(AbstractList):

    def __init__(self, BaseView,per_page):
        super(SeriesList, self).__init__(BaseView,per_page)
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
            self.Form.label([str(item.id), item.name], [row, col_start, 1, 1], grid, el)
            self.Form.button_loop(el, grid, item, [row, col_start + 1, 1, 1], ['info'], 0)
            row = row + 1

class StarList(AbstractList):

    def __init__(self,BaseView,per_page):
        super(StarList, self).__init__(BaseView,per_page)
        self.button_group_stars_info = QtWidgets.QButtonGroup()
        self.Form.buttons_loop= [
            {'button': self.on_stars_info, 'obejct': self.button_group_stars_info},
        ]

    def on_stars_info(self,id):
        self.BaseView.Form.buttom_genarator(self.button_group_stars_info, self.star_info, id)

    def star_info(self,item):
        self.BaseView.load_view('stars', item)
        return False

    def genrate(self,data,el,grid,col_start):
        row = 1
        for item in data:
            self.Form.label([str(item.id), item.name], [row, col_start, 1, 1], grid, el)
            self.Form.button_loop(el, grid, item, [row, col_start + 1, 1, 1], ['info'], 0)
            row = row + 1


class List:

    def __init__(self,obj,per_page=0):
        self.obj=obj
        self.per_page=per_page

    def generate_list(self,place,list,el,grid,col):
        self.set_per_page(list)

        switcher = {
            'movies' : MoviesList(self.obj,self.per_page),
            'series' : SeriesList(self.obj,self.per_page),
            'stars'  : StarList(self.obj,self.per_page)
        }

        classObj = switcher.get(place, "Invalid data");
        classObj.genrate(list,el,grid,col)

    def set_per_page(self,list):
        if self.per_page==0:
            self.per_page=len(list)