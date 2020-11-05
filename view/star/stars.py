from PyQt5 import QtGui
from app.db.models import Stars
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget
from app.db.models import session
from core.strings import stringManipupations
from core.creator import seriesCreator

class pagination:
    def __init__(self,obj):
        self.obj=obj

    def tabs(self,data):
        tab = QtWidgets.QTabWidget(self.obj)
        tab.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        tab.setObjectName("tabWidget")
        return tab



class baseView:

    def __init__(self,data,obj):
        self.data=data
        self.obj=obj
        self.pagination = pagination(obj)

    def title(self,data,text):
        self.title = QtWidgets.QLabel(self.obj)
        self.title.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.title.setObjectName("title")
        self.title.setText(text)

    def avatar(self,data):
        self.avatar = QtWidgets.QLabel(self.obj)
        self.avatar.setGeometry(QtCore.QRect(data[0],data[1],data[2],data[3]))
        self.avatar.setText("")
        self.avatar.setPixmap(QtGui.QPixmap(self.data.avatar))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")

    def info(self,infoData,data,rows):
        self.infoWidget = QtWidgets.QWidget(self.obj)
        self.infoWidget.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.infoWidget.setObjectName("infoWidget")
        self.infoGrid = QtWidgets.QGridLayout(self.infoWidget)
        self.infoGrid.setContentsMargins(0, 0, 0, 0)
        self.infoGrid.setObjectName("infoGrid")

        row=0

        for item in infoData:

            col1 = QtWidgets.QLabel(self.infoWidget)
            col1.setObjectName("col1")
            col1.setText(item[rows[0]])
            self.infoGrid.addWidget(col1, row, 0,2, 2)

            col2 = QtWidgets.QLabel(self.infoWidget)
            col2.setObjectName("col2")
            col2.setText(item[rows[1]])
            self.infoGrid.addWidget(col2, row, 1, 2, 2)

            row=row+1

    def galery(self,data,size,inRow):
        photos = self.data.photos
        self.galeryGrid = QtWidgets.QWidget(self.obj)
        self.galeryGrid.setGeometry(QtCore.QRect(data[0],data[1],data[2],data[3]))
        self.galeryGrid.setObjectName("galeryGrid")

        self.galeryGrid2 = QtWidgets.QGridLayout(self.galeryGrid)
        self.galeryGrid2.setContentsMargins(0, 0, 0, 0)
        self.galeryGrid2.setObjectName("galeryGrid2")
        row = 0
        col = 0
        for photo in photos:
            item = QtWidgets.QLabel(self.galeryGrid)
            item.setMaximumSize(QtCore.QSize(size[0], size[1]))
            item.setText("")
            item.setPixmap(QtGui.QPixmap(photo.src))
            item.setScaledContents(True)
            item.setObjectName("galeryItem")
            self.galeryGrid2.addWidget(item, col, row, 1, 1)
            row = row + 1
            if row > inRow:
                row = 0
                col = col + 1

class abstractView(QWidget):

    def __init__(self):
        super(abstractView, self).__init__()


    def getOne(self):
        self.data=session.query(self.model).get(self.id)

    def setupUi(self):
        pass

    def createObj(self):
        self.obj = QtWidgets.QMainWindow()
        self.obj.setObjectName("StarList")
        self.obj.resize(1707, 1036)

    def show(self,data):
        self.id = data.id
        self.createObj()
        self.setBaseView(data,self.obj)
        self.getOne()
        self.setupUi()
        self.obj.show()

    def setBaseView(self,data,obj):
        self.baseView = baseView(data,obj)

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

        left=5
        top=50
        seriesElment=1

        for item in self.seriesList:
            grid = QtWidgets.QWidget(self.addPage)
            grid.setGeometry(QtCore.QRect(left, top, 0, 0))
            grid.setMinimumSize(QtCore.QSize(390, 200))
            grid.setMaximumSize(QtCore.QSize(380, 200))
            grid.setObjectName("gridLayoutWidget_15")
            seriesItem = QtWidgets.QGridLayout(grid)
            seriesItem.setObjectName("seriesItem")
            title = QtWidgets.QLabel(grid)
            title.setObjectName("seriesTitle")

            title.setText("<html><head/><body><span style=\" font-size:12pt; font-weight:600; \">" ""
                          + stringManipupations.short(item['name'], 35) +
                          "</span></body></html>")
            seriesItem.addWidget(title, 0, 0, 1, 2)

            if len(item['movies']) > 4:
                more = QtWidgets.QPushButton(grid)
                more.setMinimumSize(QtCore.QSize(30, 0))
                more.setObjectName("InfoButton")
                more.setText("more")
                more.clicked.connect(lambda :self.open(item))
                seriesItem.addWidget(more, 0, 2, 1, 2)

            self.seriesPhoto_35 = QtWidgets.QLabel(grid)
            self.seriesPhoto_35.setMaximumSize(QtCore.QSize(100, 100))
            self.seriesPhoto_35.setText("")
            self.seriesPhoto_35.setPixmap(QtGui.QPixmap(item['avatar']))
            self.seriesPhoto_35.setScaledContents(True)
            self.seriesPhoto_35.setObjectName("seriesPhoto_35")
            seriesItem.addWidget(self.seriesPhoto_35, 1, 0, 5, 1)

            row = 1
            for el in item['movies']:
                if row < 6:
                    name = QtWidgets.QLabel(grid)
                    name.setMaximumSize(QtCore.QSize(10000000, 16777215))
                    name.setObjectName("nameLabel")
                    name.setText(el.name)
                    seriesItem.addWidget(name, row, 1, 1, 1)

                    info = QtWidgets.QPushButton(grid)
                    info.setMinimumSize(QtCore.QSize(30, 0))
                    info.setMaximumSize(QtCore.QSize(10, 16777215))
                    info.setObjectName("InfoButton")
                    info.setText("Info")
                    seriesItem.addWidget(info, row, 3, 1, 1)

                    play = QtWidgets.QPushButton(grid)
                    play.setMinimumSize(QtCore.QSize(30, 0))
                    play.setMaximumSize(QtCore.QSize(10, 16777215))
                    play.setObjectName("playButton")
                    play.setText("play")
                    seriesItem.addWidget(play, row, 2, 1, 1)

                    row = row + 1


            left = left + 390

            if seriesElment % 4 == 0:
                top=280
                left=5

            if seriesElment % 8==0:
                top=50
                left = 5
                self.newPage = QtWidgets.QWidget()
                self.newPage.setObjectName("tabWidgetPage1")
                self.addPage = self.newPage
                self.tab.addTab(self.addPage, "")

            seriesElment = seriesElment + 1

    def open(self,item):
        print(item)

    def setupUi(self):
        self.baseView.avatar([100, 80, 341, 331])
        self.title()
        self.galery()
        self.info()
        self.seriesResult()
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self.obj)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = stars()
    ui.show()
    sys.exit(app.exec_())
