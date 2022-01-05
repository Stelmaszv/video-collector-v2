import os
from core.dir import MoviesIsStarNameDir,AddMovieToStarDir,AddMovieToSeriesDir,MovieNormalLoopDir
from abc import ABC,abstractmethod

class AbstracAddLoop(ABC):

    @abstractmethod
    def run(self,obj):
        pass

    def faind_last_elment(self,dir):
        path=dir.split('\\')
        value=path[len(path)-1]
        return value

class MovieNormalLoop(AbstracAddLoop):

     def run(self,obj):
         filenames = os.listdir(obj.dir_location_value)
         MovieNormalLoopDir(filenames,obj)

class MoviesIsStarName(AbstracAddLoop):

    def run(self, obj):
        filenames = os.listdir(obj.dir_location_value)
        MoviesIsStarNameDir(filenames)

class AddMovieToStar(AbstracAddLoop):

    def run(self,obj):
        star=self.faind_last_elment(obj.dir_location_value)
        filenames = os.listdir(obj.dir_location_value)
        AddMovieToStarDir(filenames,star,obj)

class AddMovieToSeries(AbstracAddLoop):

    def run(self,obj):
        series = self.faind_last_elment(obj.dir_location_value)
        filenames = os.listdir(obj.dir_location_value)
        AddMovieToSeriesDir(filenames, series, obj)

class MovieAddLoop:

    def __init__(self,base_view):
        self.base_view=base_view

    def return_obj(self):

        switcher = {
            'normal'              : MovieNormalLoop(),
            'movie_is_star_name'  : MoviesIsStarName(),
            'add_movie_to_star'   : AddMovieToStar(),
            'add_movie_to_series' : AddMovieToSeries()
        }

        return switcher.get(self.base_view.add_type_value, "Invalid data");

class AddItems:

    def __init__(self,base_view):
        self.base_view=base_view
        self.loop_obj=self.set_obj()
        self.run_obj=self.loop_obj.return_obj()
        self.run_obj.run(self.base_view)

    def set_obj(self):
        switcher = {
            'AddMovieView': MovieAddLoop(self.base_view),
        }

        return switcher.get(self.base_view.__class__.__name__, "Invalid data");