from app.db.models import Stars
from PyQt5 import QtCore, QtWidgets
from core.view import AbstractView
from app.db.models import Stars

from PyQt5.QtWidgets import QWidget
class stars(QWidget):

    def __init__(self):
        super().__init__()
        self.window_title = 'PyQt5 button - pythonspot.com'
        self.model = Stars

    def run_window(self):

        self.show()


"""
class stars(AbstractView):

    model = Stars
    seriesList=[]

    id=None

    def title(self):
        data = [530, 60, 391, 91]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: underline;\">" + self.data.name + \
               "</span></p></body></html>"
        self.baseView.title(data,text)

    def galery(self):
        data= [1040, 50, 581, 361]
        size=[100,100]
        self.baseView.galery(data,size,2)

    def info(self):

        data   = [650, 180, 391, 161]

        rows = ['itemNmae','itemName2']

        infData=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.baseView.info(infData,data,rows)

    def seriesResult(self):
        self.seriesList=[]
        self.seriesList = seriesCreator(self.data).returnObj()
        self.baseView.listView([80, 430, 1571, 581], self.seriesList, 'Stars')

    def setupUi(self):
        self.baseView.avatar([100, 80,400,400])
        self.title()
        self.galery()
        self.info()
        self.seriesResult()
"""

