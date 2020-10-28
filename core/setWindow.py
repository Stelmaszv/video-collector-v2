from view.star.stars import stars
from view.series.test import series
from view.movie.test import movie


class setWindow():
    def __init__(self,className):
        self.className=className

    def returnObj(self):
        switcher = {
            'movies' : movie(),
            'series' : series(),
            'stars'  : stars()
        }
        return  switcher.get(self.className, "Invalid data");