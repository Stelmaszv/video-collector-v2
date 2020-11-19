class setWindow():

    def returnObj(self, object):
        from view.star.stars import stars
        from view.series.series import Serie
        from view.movie.movie import Movie

        switcher = {
            'movies' : Movie(),
            'series' : Serie(),
            'stars'  : stars()
        }
        return  switcher.get(object, "Invalid data");

class Router:
    windows_opens=[]
    searchIn='series'

    def __init__(self,base_view):
        self.base_view=base_view

    def open(self,item):
        #self.getDataFrom(setObject)
        self.window = setWindow().returnObj(self.searchIn)
        print(self.window)
        self.window.Router=self
        self.window.obj = self.base_view
        self.window.id=item.data.id

        if self.is_open(self.searchIn,item.data.id):
            self.window.run_window()
            self.windows_opens.append({'view': self.searchIn, 'id': item.data.id})



    def close_window(self):
        self.windows_opens = []

    def is_open(self, view, id):
        count = 0
        for item in self.windows_opens:
            if item['view'] == view and item['id'] == id:
                count = count + 1

        if count == 0:
            return True