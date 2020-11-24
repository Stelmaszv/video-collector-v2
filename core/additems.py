import os
from core.dir import ManageDir,MoviesIsStarNameDir,AddMovieToStarDir
from app.db.models import session
session= session

class MovieNormalLoop:

     def run(self,obj):
         filenames = os.listdir(obj.dir_location_value)
         for files in filenames:
             dir=ManageDir(files,obj)
             dir.set()


class MoviesIsStarName:

    def run(self, obj):
        filenames = os.listdir(obj.dir_location_value)
        MoviesIsStarNameDir(filenames)

class AddMovieToStar:
    objects_stars=[]

    def run(self,obj):
        star=self.faind_last_elment(obj.dir_location_value)
        filenames = os.listdir(obj.dir_location_value)
        AddMovieToStarDir(filenames,star,obj)

    def faind_last_elment(self,dir):
        path=dir.split('\\')
        value=path[len(path)-1]
        return value

class MovieAddLoop:

    def __init__(self,base_view):
        self.base_view=base_view

    def return_obj(self):

        switcher = {
            'normal'           : MovieNormalLoop(),
            'movieisstarname'  : MoviesIsStarName(),
            'addmovietostar'   : AddMovieToStar()
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