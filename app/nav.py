
class BaseNav:
    def __init__(self,BaseAction):
        self.BaseActions =  BaseAction

    def set_nav(self):
          return  [
                {
                    "name": "Add to favorits",
                    "item_name": "add_to_favorits",
                    "button": self.add_favorits
                },
                {
                    "name": "Add like",
                    "item_name": "add_like",
                    "button": self.add_like
                },
                {
                    "name": "Edit",
                    "item_name": "edit",
                    "button": self.edit
                },
                {
                    "name": "Reset",
                    "item_name": "reset",
                    "button": self.reset
                },
            ]

    def add_favorits(self):
        self.BaseActions.add_favourite()

    def add_like(self):
        self.BaseActions.add_like()

    def edit(self):
        self.BaseActions.edit()

    def reset(self):
        self.BaseActions.reset()

class StarNav(BaseNav):

    pass

class SeriesNav(BaseNav):

    pass


