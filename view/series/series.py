from core.view import AbstractView
from app.db.models import Series

from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Series
class Serie(QWidget):

    def __init__(self):
        super().__init__()
        self.window_title = 'PyQt5 button - pythonspot.com'
        self.model = Series
        self.base_view= BaseView([],self)


    def run_window(self):
        self.base_view.set_data(self.id)
        self.data=self.base_view.data
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)

    def closeEvent(self, QCloseEvent):
        self.Router.close_window('series', self.data.id)

    def info(self):

        data   = [150,320,300,200]

        rows = ['itemNmae','itemName2']

        inf_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.base_view.info(inf_data,data,rows)

    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.base_view.title(data,text)

    def galery(self):
        data = [100, 500, 250, 300]
        self.base_view.galery(data, [100, 100], 3)

    def list_view(self):
        self.base_view.listView([500,100,1200,900],self.data.movies,'Series')

    def initUI(self):
        self.info()
        self.title()
        self.galery()
        self.base_view.avatar([100, 100, 250, 250],self,self.data.avatar)
        self.window_title=self.data.name
        self.list_view()


""""
class series(AbstractView):
    model = Series

    def info(self):

        data   = [150,320,300,200]

        rows = ['itemNmae','itemName2']

        inf_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.baseView.info(inf_data,data,rows)

    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.baseView.title(data,text)

    def galery(self):
        data= [100, 500, 250, 300]
        self.baseView.galery(data,[100,100],3)

    def list_view(self):
        self.baseView.listView([500,100,1200,900],self.data.movies,'Series')

    def changelabeltext(self):
        print('from view')

    def setupUi(self):
        self.title()
        self.baseView.avatar([100, 100, 250, 250])
        self.info()
        self.galery()
        self.list_view()
"""
