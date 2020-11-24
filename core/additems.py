import os
from core.dir import ManageDir,MoviesIsStarNameDir
class MovieNormalLoop:

     def run(self,obj):
         filenames = os.listdir(obj.dir_location_value)
         for files in filenames:
             dir=ManageDir(files,obj)
             dir.set()


class MoviesIsStarName:

    def run(self, obj):
        filenames = os.listdir(obj.dir_location_value)
        MoviesIsStarNameDir(obj,filenames)


class MovieAddLoop:

    def __init__(self,base_view):
        self.base_view=base_view

    def return_obj(self):

        switcher = {
            'normal': MovieNormalLoop(),
            'movieisstarname': MoviesIsStarName()
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