from app.db.models import Stars
from core.creator import SeriesCreator
from core.view import BaseView

from PyQt5.QtWidgets import QWidget
class StarView(QWidget):

    model = Stars

    def __init__(self):
        super().__init__()
        self.base_view= BaseView([],self)

    def run_window(self):
        self.base_view.set_data(self.id)
        self.data = self.base_view.data
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
        self.base_view.title(data,text)

    def galery(self):
        data= [1040, 50, 581, 361]
        size=[100,100]
        self.base_view.galery(data,size,2)

    def info(self):

        data   = [650, 180, 391, 161]

        rows = ['itemNmae','itemName2']

        infData=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.base_view.info(infData,data,rows)

    def seriesResult(self):
        self.base_view.listView([80, 430, 1571, 581], self.list , 'Stars')

    def initUI(self):
        self.list = SeriesCreator(self.data).return_obj()
        self.base_view.avatar([100, 80, 400, 400])
        self.title()
        self.galery()
        self.info()
        #self.seriesResult()
        self.window_title=self.data.name

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()


