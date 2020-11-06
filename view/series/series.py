from core.view import abstractView
from app.db.models import Series
from core.strings import stringManipupations
from core.strings import stringManipupations
class series(abstractView):
    model = Series

    def info(self):

        data   = [150,320,300,200]

        rows = ['itemNmae','itemName2']

        infData=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.baseView.info(infData,data,rows)

    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + stringManipupations.short(self.data.name, 100) + \
               "</span></p></body></html>"
        self.baseView.title(data,text)

    def galery(self):
        data= [100, 500, 250, 361]

        self.baseView.galery(data,[100,100],3)



    def setupUi(self):
        self.baseView.avatar([100, 100,250,250])
        self.title()
        self.info()
        self.galery()

