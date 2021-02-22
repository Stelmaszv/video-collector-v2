from core.media_player import Player
from core.strings import stringManipupations
import sys
from PyQt5.QtWidgets import QApplication

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

        switcher = {
            'add_tag_to_model_no_save' :AddTagToModelNoSave(),
            'advance_search'    : AdvanceSearch(),
            'menu'              : Menu(),
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
            'play': Player()
        }
        return switcher.get(object, "Invalid data");
class Router:
    search_In = 'movies'

    def __init__(self, base_view):
        self.base_view = base_view

    def open(self, item=False):
        self.window = setWindow().returnObj(self.search_In)
        self.window.Router = self
        self.window.obj = self.base_view
        if item:
            self.window.id = item.id
        self.window.run_window()

