from core.view import AbstractView
from app.db.models import Series
from PyQt5 import QtWidgets
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

