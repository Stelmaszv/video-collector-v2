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

        switcher = {
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
    searchIn = 'movies'

    def __init__(self, base_view):
        self.base_view = base_view

    def open(self, item=False):
        self.window = setWindow().returnObj(self.searchIn)
        self.window.Router = self
        self.window.obj = self.base_view
        self.window.id = item.id
        self.window.run_window()
