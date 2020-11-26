from core.media_player import Player

class setWindow():

    def returnObj(self, object):
        from view.star.stars import StarView
        from view.series.series import Serie
        from view.movie.movie import Movie
        from view.movie.add_movie import AddMovieView


        switcher = {
            'stars'     :   StarView(),
            'movies'    :   Movie(),
            'series'    :   Serie(),
            'add_movie' :   AddMovieView(),
            'play'      :   Player()
        }
        return  switcher.get(object, "Invalid data");

class Router:
    windows_opens=[]

    def __init__(self,base_view):
        self.base_view=base_view

    def open(self,item=False,type=False):
        #self.getDataFrom(setObject)
        self.window = setWindow().returnObj(self.searchIn)

        self.window.Router=self
        self.window.obj = self.base_view


        if item:
            self.window.id=item.id
        else:
            self.window.id = 0

        if self.is_open(self.searchIn,self.window.id):
            self.window.run_window()
            self.windows_opens.append({'view': self.searchIn, 'id': self.window.id})

    def close_window(self):
        self.windows_opens = []

    def is_open(self, view, id):
        count = 0
        for item in self.windows_opens:
            if item['view'] == view and item['id'] == id:
                count = count + 1

        if count == 0:
            return True