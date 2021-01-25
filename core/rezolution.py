from abc import ABC,abstractmethod
from core.setings import window_type

class SetResolution:
    windows_type=window_type

    def __init__(self):
        self.menu_set=self.set_menu_type()

    def set_menu_type(self):
        switcher = {
            'half-smal': MenuHalfSmal(),
            'half-big': MenuHalfbig()
        }
        obj=switcher.get(self.windows_type, "Invalid data");
        return obj.show()

class MenuType(ABC):

    @abstractmethod
    def show(self):
        pass

class MenuHalfbig(MenuType):

    def show(self):
        return {
            "Menu": {
                "position":{
                    "left"            : -2,
                    "top"             : 25,
                    "width"           : 400,
                    "height"          : 1400
                }
            },

            "Stars": {
                "position": {
                    "left"              : 400,
                    "top"               : 25,
                    "width"             : 2155,
                    "height"            : 1400
                },
                "window": {
                    "avatar_size"       : [150, 80, 300, 300],
                    "title_size"        : [700, 0, 300, 100],
                    "info_size"         : [700, 50, 800, 400],
                    "galery_size"       : [1250, 70, 700, 361],
                    "list_view_size"    : [150, 430, 1800, 920],
                    "galery_photo_size" : [250, 250],
                    "description": [330, 150, 450, 200],
                    'galery_item_show'  : 3,
                    "section": {
                        "left"          : 50,
                        "left_add"      : 220,
                        "top"           : 0,
                        "top_add"       : 250,
                        "per_row"       : 8,
                        "per_page"      : 32
                    }
                }
            }
        }

class MenuHalfSmal(MenuType):

    def show(self):
        return {
            "Menu": {
                "position": {
                    "left"             : 2562,
                    "top"              : 400,
                    "width"            : 400,
                    "height"           : 985
                }
            },

            "Stars": {
                "position":  {
                    "left"              : 2562+400,
                    "top"               : 400,
                    "width"             : 1280,
                    "height"            : 985
                },
                "window":{
                    "avatar_size"       : [50, 80, 250, 300],
                    "title_size"        : [400, 0, 300, 100],
                    "info_size"         : [330, 100, 700, 100],
                    "galery_size"       : [750, 70, 581, 361],
                    "list_view_size"    : [50, 430, 1200, 550],
                    "galery_photo_size" : [150, 150],
                    "galery_item_show"  : 2,
                    "description"       : [330,150,450,200,500], # 5 String limit
                    "section": {
                        "left"         : 15,
                        "left_add"     : 250,
                        "top"          : 0,
                        "top_add"      : 250,
                        "per_row"      : 6,
                        "per_page"     : 12
                    }
                }

            }
        }
