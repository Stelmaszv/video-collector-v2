from core.media_player import Player
from core.strings import stringManipupations
import json

open_wnidows=[]

class setWindow():

    def returnObj(self, object):
        from view.series.series import SerieView
        from view.movie.movie import MovieView
        from view.movie.add_movie import AddMovieView
        from view.star.stars import StarView
        from view.SeriesMovieListView.MovieListView import MovieListView


        switcher = {
            'stars': StarView(),
            'movies': MovieView(),
            'series': SerieView(),
            'add_movie': AddMovieView(),
            'movie_list' : MovieListView(),
            'play': Player()
        }
        return switcher.get(object, "Invalid data");

class Router:
    searchIn = 'movies'
    active=0

    def __init__(self, base_view):
        self.base_view = base_view

    def open(self, item=False):
        self.window = setWindow().returnObj(self.searchIn)
        self.window.Router = self
        self.window.obj = self.base_view
        if item:

            if str(item).find("{")==-1:
                self.window.id = item.id
            else:
                self.window.data = item
                self.window.id   = item['id']
        else:
            self.window.id = 0


        self.window.window_id = stringManipupations.random(20)
        open_wnidows.append(self.window)
        if self.active == 0:
            self.active=self.window.window_id
        item=self.is_open()
        if item is not None:
            item.run_window()

    def close_window(self):
        for item in open_wnidows:
            if item.window_id==0:
                open_wnidows.remove(item)

        self.active=0

    def is_open(self):
        movie=None
        for item in open_wnidows:
            if item.window_id != self.active:
                item.window_id=0
                movie = None
            elif item.window_id == self.active:
                movie = item
        return movie
