class BaseNav:
    def __init__(self,BaseAction):
        self.BaseActions =  BaseAction

    def set_nav(self):
          return  [
                {
                    "name": "Add to favorits",
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

    pass

class StarNav(BaseNav):

    pass

class SeriesNav(BaseNav):

    pass


