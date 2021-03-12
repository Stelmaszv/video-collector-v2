from core.media_player import Player
from core.strings import stringManipupations
import sys
from PyQt5.QtWidgets import QApplication
from core.custum_errors import Error

open_wnidows=[]

class setWindow():

    def returnObj(self, object):
        from view.series.series import SerieView
        from view.movie.movie import MovieView
        from view.movie.add_movie import AddMovieView
        from view.star.stars import StarView
        from view.SeriesMovieListView.MovieListView import MovieListView
        from view.star.edit_star import EditStarView
        from view.tags.add_tags import AddTagView
        from view.series.editseries import EditSeries
        from view.set_photo_to_series.set_photo_to_series import SetPhotoToSeries
        from view.star.add_star_to_model import AddStarToModelView
        from view.menu.menu import Menu
        from view.menu.advande_search import AdvanceSearch
        from view.tags.add_tag_to_model_no_save import AddTagToModelNoSave
        from view.movie.edit_movie import EditMovieView
        from view.star.add_star_to_model import MovieAddStarToModelView

        switcher = {
            'add_tag_to_model_no_save' :AddTagToModelNoSave(),
            'advance_search'    : AdvanceSearch(),
            'menu'              : Menu(),
            'edit_movie'        : EditMovieView(),
            'add_star_to_model' :AddStarToModelView(),
            'set_photo_to_series' : SetPhotoToSeries(),
            'add_tags': AddTagView(),
            'stars': StarView(),
            'edit_series':EditSeries(),
            'edit_star': EditStarView(),
            'movies': MovieView(),
            'series': SerieView(),
            'add_movie': AddMovieView(),
            'movie_list' : MovieListView(),
            'play': Player(),
            'movie_add_star_to_model_view' :MovieAddStarToModelView()
        }

        get = switcher.get(object, "Invalid data")
        if get =='Invalid data':
            Error.throw_error('Viev '+object+' not found')
        return switcher.get(object, "Invalid data");
class Router:
    search_In = 'movies'

    def __init__(self, base_view):
        self.base_view = base_view

    def open(self, item=False,list=False):
        self.window = setWindow().returnObj(self.search_In)
        self.window.Router = self
        self.window.obj = self.base_view
        if item:
            self.window.id = item.id
        if list:
            self.window.list=list
        self.window.run_window()

