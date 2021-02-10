from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Series
from core.rezolution import SetResolution

class SerieView(QWidget):

    def __init__(self):
        super().__init__()
        self.model = Series
        self.BaseView= BaseView([], self)
        self.SetResolution = SetResolution()
        self.left = self.SetResolution.menu_set['Series']['position']['left']
        self.top = self.SetResolution.menu_set['Series']['position']['top']
        self.width = self.SetResolution.menu_set['Series']['position']['width']
        self.height = self.SetResolution.menu_set['Series']['position']['height']
        self.WindowSize = self.SetResolution.menu_set['Series']['window']


    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data=self.BaseView.data
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def info(self):

        data   = [
            self.WindowSize['info_size'][0],
            self.WindowSize['info_size'][1],
            self.WindowSize['info_size'][2],
            self.WindowSize['info_size'][3]
        ]

        rows = ['itemNmae','itemName2']

        inf_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.BaseView.info(inf_data, data, rows)

    def title(self):
        data = [
            self.WindowSize['title_size'][0],
            self.WindowSize['title_size'][1],
            self.WindowSize['title_size'][2],
            self.WindowSize['title_size'][3]
        ]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def galery(self):
        data = [
            self.WindowSize['galery_size'][0],
            self.WindowSize['galery_size'][1],
            self.WindowSize['galery_size'][2],
            self.WindowSize['galery_size'][3]
        ]
        data_size = [
            self.WindowSize['galery_photo_size'][0],
            self.WindowSize['galery_photo_size'][1]
        ]
        self.BaseView.galery(data, data_size, self.WindowSize['galery_item_show'])

    def list_view(self):
        data= [
            self.WindowSize['list_view_size'][0],
            self.WindowSize['list_view_size'][1],
            self.WindowSize['list_view_size'][2],
            self.WindowSize['list_view_size'][3]
        ]
        self.BaseView.listView(data, self.data.movies, 'Series',self)

    def initUI(self):
        self.info()
        self.title()
        self.galery()
        data = [
            self.WindowSize['avatar_size'][0],
            self.WindowSize['avatar_size'][1],
            self.WindowSize['avatar_size'][2],
            self.WindowSize['avatar_size'][3]
        ]
        self.BaseView.avatar(data, self, self.data.avatar)
        self.window_title=self.data.name
        self.list_view()

