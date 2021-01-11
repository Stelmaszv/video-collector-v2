from abc import ABC,abstractmethod

class WindowSize:
    type = 'defult'

    def __init__(self,QWidget):
        self.Obj_QWidget=QWidget;
        self.width =  self.Obj_QWidget.frameGeometry().width()
        self.height = self.Obj_QWidget.frameGeometry().height()
        self.window_size = self.set_window_type()
        self.size_data = self.window_size.defult()

    def set_window_size(self):

        if self.width > 1250 and self.width < 1679:
            self.type='defult'
            self.size_data=self.window_size.defult()

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
    def defult(self):
        pass

    @abstractmethod
    def small(self):
        pass

class StarWindowSize(AbstractWindowType):

    def big(self):
        pass

    def defult(self):
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
            "avatar": ['0', '0']
        }
