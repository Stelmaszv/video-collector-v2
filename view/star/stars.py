from app.db.models import Stars
from PyQt5 import QtCore, QtWidgets
from core.creator import seriesCreator
from core.view import abstractView

class stars(abstractView):

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
        data=[80, 430, 1571, 581]
        self.tab=self.baseView.pagination.tabs(data)
        self.starPage = QtWidgets.QWidget()
        self.starPage.setObjectName("tabWidgetPage1")
        self.grid = QtWidgets.QWidget(self.starPage)
        self.addPage=self.starPage
        self.tab.addTab(self.addPage, "")
        self.seriesList = seriesCreator(self.data).returnObj()
        self.baseView.pagination.paginate('seriesPaginator',self)

    def setupUi(self):
        self.baseView.avatar([100, 80,400,400])
        self.title()
        self.galery()
        self.info()
        self.seriesResult()
        self.tab.setCurrentIndex(1)

