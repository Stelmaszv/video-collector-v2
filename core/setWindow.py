from view.star.stars import stars
from view.series.series import series
from view.movie.movie import Movie


class setWindow():
    def __init__(self,className):
        self.className=className

    def returnObj(self, menu):
        switcher = {
            'movies' : Movie(),
            'series' : series(),
            'stars'  : stars()
        }
        return  switcher.get(self.className, "Invalid data");