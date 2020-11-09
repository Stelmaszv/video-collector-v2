from view.star.stars import stars
from view.series.series import series
from view.movie.test import movie


class setWindow():
    def __init__(self,className):
        self.className=className

    def returnObj(self, menu):
        switcher = {
            'movies' : movie(),
            'series' : series(),
            'stars'  : stars()
        }
        return  switcher.get(self.className, "Invalid data");