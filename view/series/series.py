from PyQt5.QtWidgets import QWidget
from core.view import AbstractBaseView
from app.db.models import Series
from app.nav import SeriesNav
from app.info import InfoSection

class SerieView(QWidget,AbstractBaseView):

    Info               =  InfoSection
    Nav                =  SeriesNav
    model              =  Series
    reset_view         = 'series'
    edit_view          = 'edit_series'
    resolution_index   = 'Serie'
    list_view          = 'Series'



"""
class SerieView(QWidget):

    reset_view = 'series'
    edit_view = 'edit_series'

    def __init__(self):
        super().__init__()
        self.model = Series
        self.BaseView= BaseView([], self)
        self.BaseActions = ViewBaseAction(self)
        self.Nav = SeriesNav(self.BaseActions)
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

        data   = self.WindowSize['info_size']

        rows = ['itemNmae','itemName2']

        inf_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.BaseView.info(inf_data, data, rows)

    def title(self):
        data = self.WindowSize['title_size']
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def galery(self):
        data = self.WindowSize['galery_size']
        data_size = self.WindowSize['galery_photo_size']
        self.BaseView.galery(data, data_size, self.WindowSize['galery_item_show'])

    def list_view(self):
        data= self.WindowSize['list_view_size']
        self.BaseView.listView(data, self.data.movies, 'Series',self)

    def get_nav(self):
        data = self.WindowSize['navbar']
        self.BaseView.get_nav(
            data,
            self.Nav.set_nav()
        )

    def initUI(self):
        self.get_nav()
        self.info()
        self.title()
        self.galery()
        data = self.WindowSize['avatar_size']
        self.BaseView.avatar(data, self, self.data.avatar)
        self.window_title=self.data.name
        self.list_view()
"""

