from app.db.models import Stars
from core.view import BaseView
from core.creator import SeriesCreator
from core.strings import stringManipupations
from PyQt5.QtWidgets import QWidget

class StarView(QWidget):

    model = Stars

    def __init__(self):
        super().__init__()
        self.BaseView= BaseView([], self)

    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.seriesResult()
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)

    def title(self):
        data = [530, 60, 391, 91]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: underline;\">" + self.data.name + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def galery(self):
        data= [1040, 50, 581, 361]
        size=[100,100]
        self.BaseView.galery(data, size, 2)

    def info(self):

        data   = [650, 180, 391, 161]

        rows = ['itemNmae','itemName2']

        infData=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.BaseView.info(infData, data, rows)

    def seriesResult(self):
        self.list = SeriesCreator(self.data).return_obj()
        #self.base_view.listView([80, 430, 1571, 581], self.list , 'Stars')

    def initUI(self):
        self.BaseView.avatar([100, 80, 400, 400])
        self.title()
        self.galery()
        self.info()
        self.window_title=self.data.name

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()


