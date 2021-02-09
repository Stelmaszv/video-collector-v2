from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Series

class SerieView(QWidget):

    def __init__(self):
        super().__init__()
        self.model = Series
        self.BaseView= BaseView([], self)


    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data=self.BaseView.data
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)

    def info(self):

        data   = [150,320,300,200]

        rows = ['itemNmae','itemName2']

        inf_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.BaseView.info(inf_data, data, rows)

    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def galery(self):
        data = [100, 500, 250, 300]
        self.BaseView.galery(data, [100, 100], 3)

    def list_view(self):
        self.setParent(None)
        self.BaseView.listView([500, 100, 1200, 900], self.data.movies, 'Series',self)

    def initUI(self):
        self.info()
        self.title()
        self.galery()
        self.BaseView.avatar([100, 100, 250, 250], self, self.data.avatar)
        self.window_title=self.data.name
        self.list_view()

