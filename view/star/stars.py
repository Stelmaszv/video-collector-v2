from PyQt5 import QtGui
from app.db.models import Stars
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget
from app.db.models import session
from core.strings import stringManipupations
from core.creator import seriesCreator

class stars(QWidget):

    model = Stars
    seriesList=[]
    """
    seriesList = [
        #page1
        {
            'name':"1",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "2",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "3",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "4",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "5",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "6",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "7",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "8",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        #page2
        {
            'name': "9",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "10",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        },
        {
            'name': "11",
            'avatar': "C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg",
            'movies': [
                "fajny  ",
                "fajny2",
                "fajny3",
                "fajny5",
                'fajny6'
            ]
        }
    ]
    """
    id=None

    def __init__(self,):
        super().__init__()

    def getOne(self):
        self.data=session.query(self.model).get(self.id)

    def show(self,id):
        self.id=id
        self.getOne()
        self.setupUi()
        self.obj.show()

    def createObj(self):
        self.obj = QtWidgets.QMainWindow()
        self.obj.setObjectName("StarList")
        self.obj.resize(1707, 1036)

    def avatar(self):
        self.label = QtWidgets.QLabel(self.obj)
        self.label.setGeometry(QtCore.QRect(100, 80, 341, 331))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.data.avatar))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

    def title(self):
        self.Title = QtWidgets.QLabel(self.obj)
        self.Title.setGeometry(QtCore.QRect(530, 60, 391, 91))
        self.Title.setObjectName("Title")

        self.Title.setToolTip("<html><head/><body>"
                              "<p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">"
                              ""+self.data.name+"</span></p></body></html>")

        self.Title.setText("<html><head/><body>"
                           "<p align=\"center\"><span style=\" font-size:18pt; "
                           "font-weight:600; text-decoration: underline;\">"
                           ""+self.data.name+"</span></p></body></html>")

    def galery(self):
        photos=self.data.photos
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.obj)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1040, 50, 581, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        row=0
        col=0
        for photo in photos:
            label = QtWidgets.QLabel(self.gridLayoutWidget_2)
            label.setMaximumSize(QtCore.QSize(100, 100))
            label.setText("")
            label.setPixmap(QtGui.QPixmap(photo.src))
            label.setScaledContents(True)
            label.setObjectName("label_9")
            self.gridLayout_5.addWidget(label, col, row, 1, 1)
            row=row+1
            if row > 3:
                row=0
                col=col+1

    def info(self):
        self.label_225 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_225.setObjectName("label_225")
        self.gridLayout_8.addWidget(self.label_225, 4, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("TextLabel")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("TextLabel")
        self.gridLayout_8.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.label_10.setText("TextLabel")
        self.gridLayout_8.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.label_13.setText("TextLabel")
        self.gridLayout_8.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.label_25.setText("TextLabel")
        self.gridLayout_8.addWidget(self.label_25, 2, 0, 1, 1)
        self.label_224 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_224.setObjectName("label_224")
        self.label_224.setText("TextLabel")
        self.gridLayout_8.addWidget(self.label_224, 2, 1, 1, 1)
        self.label_224 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_224.setObjectName("label_224")
        self.label_224.setText("TextLabel")
        self.gridLayout_8.addWidget(self.label_224, 4, 0, 1, 2)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.setText("dqwd")
        self.gridLayout_8.addWidget(self.commandLinkButton, 5, 0, 1, 2)

    def paginationForSeries(self):
        self.tabWidget = QtWidgets.QTabWidget(self.obj)
        self.tabWidget.setGeometry(QtCore.QRect(80, 430, 1571, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.starPage = QtWidgets.QWidget()
        self.starPage.setObjectName("tabWidgetPage1")
        self.grid = QtWidgets.QWidget(self.starPage)

    def series(self):

        self.gridLayoutWidget = QtWidgets.QWidget(self.obj)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(560, 180, 391, 161))

        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")

    def setSeries(self):
        self.seriesList= seriesCreator(self.data).returnObj()

    def seriesResult(self):
        self.setSeries()
        left=5
        top=50
        seriesElment=1
        self.starPage = QtWidgets.QWidget()
        self.starPage.setObjectName("tabWidgetPage1")
        self.addPage=self.starPage
        self.tabWidget.addTab(self.addPage, "")

        series = self.data.series
        for item in series:

            grid = QtWidgets.QWidget(self.addPage)
            grid.setGeometry(QtCore.QRect(left,top, 0,0))
            grid.setMinimumSize(QtCore.QSize(390, 200))
            grid.setMaximumSize(QtCore.QSize(380, 200))
            grid.setObjectName("gridLayoutWidget_15")
            seriesItem = QtWidgets.QGridLayout(grid)
            seriesItem.setObjectName("seriesItem")
            title = QtWidgets.QLabel(grid)
            title.setObjectName("seriesTitle")

            title.setText("<html><head/><body><span style=\" font-size:12pt; font-weight:600; \">" ""
                +stringManipupations.short(item.name,35)+
            "</span></body></html>")
            seriesItem.addWidget(title, 0, 0, 1, 2)

            if len(item.movies) > 4:
                more = QtWidgets.QPushButton(grid)
                more.setMinimumSize(QtCore.QSize(30, 0))
                more.setObjectName("InfoButton")
                more.setText("more")
                seriesItem.addWidget(more, 0, 2, 1, 2)

            self.seriesPhoto_35 = QtWidgets.QLabel(grid)
            self.seriesPhoto_35.setMaximumSize(QtCore.QSize(100, 100))
            self.seriesPhoto_35.setText("")
            self.seriesPhoto_35.setPixmap(QtGui.QPixmap(item.avatar))
            self.seriesPhoto_35.setScaledContents(True)
            self.seriesPhoto_35.setObjectName("seriesPhoto_35")
            seriesItem.addWidget(self.seriesPhoto_35, 1, 0, 5, 1)

            row=1


            for el in item.movies:
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

                    row=row+1

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
                self.tabWidget.addTab(self.addPage, "")

            seriesElment = seriesElment + 1

    def setupUi(self):
        self.createObj()
        self.avatar()
        self.title()
        self.galery()
        self.series()
        self.info()
        self.paginationForSeries()
        self.seriesResult()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self.obj)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = stars()
    ui.show()
    sys.exit(app.exec_())
