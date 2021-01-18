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
                    "left": -2,
                    "top": 25,
                    "width": 400,
                    "height": 1400
                }
            },

            "Stars": {
                "position": {
                    "left": 400,
                    "top": 25,
                    "width": 2155,
                    "height": 1400
                },
                "window": {
                    "avatar_size": [150, 80, 300, 300],
                    "title_size": [700, 0, 300, 100],
                    "info_size": [700, 50, 800, 400],
                    "galery_size": [1200, 70, 581, 361],
                    "list_view_size": [150, 430, 1800, 920],
                    "galery_photo_size": [150, 150],
                    "section": {
                        "left": 50,
                        "left_add": 220,
                        "top": 0,
                        "top_add": 250,
                        "per_row": 8,
                        "per_page": 32
                    }
                }
            }
        }

class MenuHalfSmal(MenuType):

    def show(self):
        return {
            "Menu": {
                "position":{
                    "left": 2562,
                    "top": 400,
                    "width": 400,
                    "height": 985
                }
            },

            "Stars": {
                "position": {
                    "left": 2562+400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window":{
                    "avatar_size": [50, 80, 300, 300],
                    "title_size": [400, 0, 300, 100],
                    "info_size": [370, 50, 800, 400],
                    "galery_size": [700, 70, 581, 361],
                    "list_view_size": [50, 430, 1200, 550],
                    "galery_photo_size": [150, 150],
                    "section": {
                        "left": 15,
                        "left_add": 250,
                        "top": 0,
                        "top_add": 250,
                        "per_row": 6,
                        "per_page": 12
                    }
                }

            }
        }


class WindowSize:
    type = ''

    def __init__(self,QWidget):
        self.Obj_QWidget=QWidget;
        self.width =  self.Obj_QWidget.frameGeometry().width()
        self.height = self.Obj_QWidget.frameGeometry().height()


    def set_window_size(self):
        self.window_size = self.set_window_type()
        self.size_data = self.window_size.half_smal()

        if self.width > 1250 and self.width < 1679:
            self.type='half_smal'
            self.size_data=self.window_size.half_smal()

        if self.width > 1680 and self.width < 2559:
            self.type = 'small'
            self.size_data=self.window_size.small()

        if self.width > 2560:
            self.type = 'big'
            self.size_data=self.window_size.big()

    def set_window_type(self):
        switcher = {
            'star'  : StarWindowSize()
        }
        return  switcher.get(self.Obj_QWidget.window_type, "Invalid data");

class AbstractWindowType(ABC):

    @abstractmethod
    def big(self):
        pass

    @abstractmethod
    def half_smal(self):
        pass

    @abstractmethod
    def small(self):
        pass

class StarWindowSize(AbstractWindowType):

    def big(self):
        pass

    def half_smal(self):
        return {
            "avatar_size"       : [50, 80, 300, 300],
            "title_size"        : [400, 0, 300, 100],
            "info_size"         : [370, 50, 800, 400],
            "galery_size"       : [700, 70, 581, 361],
            "list_view_size"    : [50, 430, 1200, 550],
            "galery_photo_size" : [150, 150],
            "section"           : {
                "left"     : 15,
                "left_add" : 250,
                "top"      : 0,
                "top_add"  : 250,
                "per_row"  : 6,
                "per_page" : 12
            }
        }

    def small(self):

        return {
            "avatar_size": [100, 80, 300, 300],
            "title_size": [600, 0, 300, 100],
            "info_size": [570, 50, 800, 400],
            "galery_size": [1000, 70, 581, 361],
            "list_view_size": [105, 430, 1450, 550],
            "galery_photo_size": [150, 150],
            "section": {
                "left": 35,
                "left_add": 200,
                "top": 0,
                "top_add": 250,
                "per_row": 7,
                "per_page": 14
            }
        }
