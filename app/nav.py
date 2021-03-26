import os

class BaseNav:
    def __init__(self,AbstractBaseView):
        self.BaseActions =  AbstractBaseView.BaseActions
        self.data        =  AbstractBaseView.data
        self.AbstractBaseView = AbstractBaseView

    def set_name_for_favorits(self):
        name= 'Add to favorits'
        if self.data.favourite:
            name= 'Remove from favorits'
        return name

    def set_data(self,data):
        self.data = data
        self.set_base_nav()

    def set_nav(self):
        return self.base_nav

    def set_base_nav(self):
          self.base_nav= [
                {
                    "name": self.set_name_for_favorits(),
                    "obj_name": "add_to_favorits",
                    "grid_data": [0,0,1,1],
                    "click": self.add_favorits,
                    'arguments':[],
                },
                {
                    "name": "Add like",
                    "obj_name": "add_like",
                    "grid_data": [0, 1, 1, 1],
                    "click": self.add_like,
                    'arguments': [],
                },
                {
                    "name": "Edit",
                    "obj_name": "edit",
                    "grid_data": [0, 2, 1, 1],
                    "click": self.edit,
                    'arguments': [],
                },
                {
                    "name": "Reset",
                    "obj_name": "reset",
                    "grid_data": [0, 3, 1, 1],
                    "click": self.reset,
                    'arguments': [],
                },
            ]

    def add_favorits(self,argumants):
        self.BaseActions.add_favourite()

    def add_like(self,argumants):
        self.BaseActions.add_like()

    def edit(self,argumants):
        self.BaseActions.edit()

    def reset(self,argumants):
        self.BaseActions.reset()

class MovieNav(BaseNav):

    def set_nav(self):
        new={
            "name": 'Open',
            "obj_name": "add_to_favorits",
            "grid_data": [0, 4, 1, 1],
            "click": self.open,
            'arguments': [],
        }
        self.base_nav.append(new)
        return self.base_nav


    def open(self,argumants):
        self.AbstractBaseView.BaseView.load_view('play', self.data)

class MovieGaleryNav(BaseNav):

    pass

class StarNav(BaseNav):

    pass

class SeriesNav(BaseNav):

    pass


