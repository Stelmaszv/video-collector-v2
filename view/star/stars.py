from PyQt5 import QtGui
from app.db.models import Stars
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget
from app.db.models import session

class stars(QWidget):
    model = Stars
    id = 1
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
    def __init__(self,):
        super().__init__()

    def getOne(self):
        self.data=session.query(self.model).get(self.id)

    def show(self):
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
        self.Title.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">"+self.data.name+"</span></p></body></html>")
        self.Title.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">"+self.data.name+"</span></p></body></html>")

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

    def seriesResult(self):
        left=5
        top=0
        seriesElment=1
        self.starPage = QtWidgets.QWidget()
        self.starPage.setObjectName("tabWidgetPage1")
        self.addPage=self.starPage
        self.tabWidget.addTab(self.addPage, "")

        series = self.data.series

        for item in series:

            grid = QtWidgets.QWidget(self.addPage)
            grid.setGeometry(QtCore.QRect(left,top, 390, 300))
            grid.setObjectName("gridLayoutWidget_15")
            seriesItem = QtWidgets.QGridLayout(grid)
            seriesItem.setContentsMargins(2, 2, 2, 2)
            seriesItem.setObjectName("seriesItem")
            title = QtWidgets.QLabel(grid)
            title.setObjectName("seriesTitle")
            title.setText("<html><head/><body><p align=\"center\";><span style=\" font-size:18pt; font-weight:600; \">"+item.name+"</span></p></body></html>")
            seriesItem.addWidget(title, 0, 0, 1, 0)

            self.seriesPhoto_35 = QtWidgets.QLabel(grid)
            self.seriesPhoto_35.setMaximumSize(QtCore.QSize(100, 100))
            self.seriesPhoto_35.setText("")
            self.seriesPhoto_35.setPixmap(QtGui.QPixmap(item.avatar))
            self.seriesPhoto_35.setScaledContents(True)
            self.seriesPhoto_35.setObjectName("seriesPhoto_35")
            seriesItem.addWidget(self.seriesPhoto_35, 1, 0, 5, 1)

            row=1

            for el in item.movies:
                name = QtWidgets.QLabel(grid)
                name.setMinimumSize(QtCore.QSize(30, 0))
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

            if len(item.movies) > 4:
                self.commandLinkButton_35 = QtWidgets.QCommandLinkButton(grid)
                self.commandLinkButton_35.setObjectName("commandLinkButton_35")
                self.commandLinkButton_35.setText("show more")
                seriesItem.addWidget(self.commandLinkButton_35, 6, 0, 1, 4)
            left = left + 390


            if seriesElment % 4 == 0:
                top=250
                left=5

            if seriesElment % 8==0:
                top=0
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

    def retranslateUi(self, StarList):
        _translate = QtCore.QCoreApplication.translate
        StarList.setWindowTitle(_translate("StarList", "Form"))
        self.label_225.setText(_translate("StarList", "TextLabel"))
        self.label_8.setText(_translate("StarList", "TextLabel"))
        self.label_11.setText(_translate("StarList", "TextLabel"))
        self.label_10.setText(_translate("StarList", "TextLabel"))
        self.label_13.setText(_translate("StarList", "TextLabel"))
        self.label_25.setText(_translate("StarList", "TextLabel"))
        self.label_224.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton.setText(_translate("StarList", "CommandLinkButton"))
        self.label_214.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_368.setText(_translate("StarList", "PushButton"))
        self.pushButton_369.setText(_translate("StarList", "PushButton"))
        self.pushButton_370.setText(_translate("StarList", "PushButton"))
        self.pushButton_371.setText(_translate("StarList", "PushButton"))
        self.pushButton_372.setText(_translate("StarList", "PushButton"))
        self.pushButton_373.setText(_translate("StarList", "PushButton"))
        self.pushButton_374.setText(_translate("StarList", "PushButton"))
        self.pushButton_375.setText(_translate("StarList", "PushButton"))
        self.pushButton_376.setText(_translate("StarList", "PushButton"))
        self.label_215.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_35.setText(_translate("StarList", "info"))
        self.item_35.setText(_translate("StarList", "TextLabel"))
        self.label_216.setText(_translate("StarList", "TextLabel"))
        self.label_217.setText(_translate("StarList", "TextLabel"))
        self.label_218.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_35.setText(_translate("StarList", "CommandLinkButton"))
        self.label_219.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_377.setText(_translate("StarList", "PushButton"))
        self.pushButton_378.setText(_translate("StarList", "PushButton"))
        self.pushButton_379.setText(_translate("StarList", "PushButton"))
        self.pushButton_380.setText(_translate("StarList", "PushButton"))
        self.pushButton_381.setText(_translate("StarList", "PushButton"))
        self.pushButton_382.setText(_translate("StarList", "PushButton"))
        self.pushButton_383.setText(_translate("StarList", "PushButton"))
        self.pushButton_384.setText(_translate("StarList", "PushButton"))
        self.pushButton_385.setText(_translate("StarList", "PushButton"))
        self.label_220.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_36.setText(_translate("StarList", "info"))
        self.item_36.setText(_translate("StarList", "TextLabel"))
        self.label_221.setText(_translate("StarList", "TextLabel"))
        self.label_222.setText(_translate("StarList", "TextLabel"))
        self.label_223.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_36.setText(_translate("StarList", "CommandLinkButton"))
        self.label_226.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_386.setText(_translate("StarList", "PushButton"))
        self.pushButton_387.setText(_translate("StarList", "PushButton"))
        self.pushButton_388.setText(_translate("StarList", "PushButton"))
        self.pushButton_389.setText(_translate("StarList", "PushButton"))
        self.pushButton_390.setText(_translate("StarList", "PushButton"))
        self.pushButton_391.setText(_translate("StarList", "PushButton"))
        self.pushButton_392.setText(_translate("StarList", "PushButton"))
        self.pushButton_393.setText(_translate("StarList", "PushButton"))
        self.pushButton_394.setText(_translate("StarList", "PushButton"))
        self.label_227.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_37.setText(_translate("StarList", "info"))
        self.item_37.setText(_translate("StarList", "TextLabel"))
        self.label_228.setText(_translate("StarList", "TextLabel"))
        self.label_229.setText(_translate("StarList", "TextLabel"))
        self.label_230.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_37.setText(_translate("StarList", "CommandLinkButton"))
        self.label_231.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_395.setText(_translate("StarList", "PushButton"))
        self.pushButton_396.setText(_translate("StarList", "PushButton"))
        self.pushButton_397.setText(_translate("StarList", "PushButton"))
        self.pushButton_398.setText(_translate("StarList", "PushButton"))
        self.pushButton_399.setText(_translate("StarList", "PushButton"))
        self.pushButton_400.setText(_translate("StarList", "PushButton"))
        self.pushButton_401.setText(_translate("StarList", "PushButton"))
        self.pushButton_402.setText(_translate("StarList", "PushButton"))
        self.pushButton_403.setText(_translate("StarList", "PushButton"))
        self.label_232.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_38.setText(_translate("StarList", "info"))
        self.item_38.setText(_translate("StarList", "TextLabel"))
        self.label_233.setText(_translate("StarList", "TextLabel"))
        self.label_234.setText(_translate("StarList", "TextLabel"))
        self.label_235.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_38.setText(_translate("StarList", "CommandLinkButton"))
        self.label_236.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_404.setText(_translate("StarList", "PushButton"))
        self.pushButton_405.setText(_translate("StarList", "PushButton"))
        self.pushButton_406.setText(_translate("StarList", "PushButton"))
        self.pushButton_407.setText(_translate("StarList", "PushButton"))
        self.pushButton_408.setText(_translate("StarList", "PushButton"))
        self.pushButton_409.setText(_translate("StarList", "PushButton"))
        self.pushButton_410.setText(_translate("StarList", "PushButton"))
        self.pushButton_411.setText(_translate("StarList", "PushButton"))
        self.pushButton_412.setText(_translate("StarList", "PushButton"))
        self.label_237.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_39.setText(_translate("StarList", "info"))
        self.item_39.setText(_translate("StarList", "TextLabel"))
        self.label_238.setText(_translate("StarList", "TextLabel"))
        self.label_239.setText(_translate("StarList", "TextLabel"))
        self.label_240.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_39.setText(_translate("StarList", "CommandLinkButton"))
        self.label_241.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_413.setText(_translate("StarList", "PushButton"))
        self.pushButton_414.setText(_translate("StarList", "PushButton"))
        self.pushButton_415.setText(_translate("StarList", "PushButton"))
        self.pushButton_416.setText(_translate("StarList", "PushButton"))
        self.pushButton_417.setText(_translate("StarList", "PushButton"))
        self.pushButton_418.setText(_translate("StarList", "PushButton"))
        self.pushButton_419.setText(_translate("StarList", "PushButton"))
        self.pushButton_420.setText(_translate("StarList", "PushButton"))
        self.pushButton_421.setText(_translate("StarList", "PushButton"))
        self.label_242.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_40.setText(_translate("StarList", "info"))
        self.item_40.setText(_translate("StarList", "TextLabel"))
        self.label_243.setText(_translate("StarList", "TextLabel"))
        self.label_244.setText(_translate("StarList", "TextLabel"))
        self.label_245.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_40.setText(_translate("StarList", "CommandLinkButton"))
        self.label_246.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_422.setText(_translate("StarList", "PushButton"))
        self.pushButton_423.setText(_translate("StarList", "PushButton"))
        self.pushButton_424.setText(_translate("StarList", "PushButton"))
        self.pushButton_425.setText(_translate("StarList", "PushButton"))
        self.pushButton_426.setText(_translate("StarList", "PushButton"))
        self.pushButton_427.setText(_translate("StarList", "PushButton"))
        self.pushButton_428.setText(_translate("StarList", "PushButton"))
        self.pushButton_429.setText(_translate("StarList", "PushButton"))
        self.pushButton_430.setText(_translate("StarList", "PushButton"))
        self.label_247.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_41.setText(_translate("StarList", "info"))
        self.item_41.setText(_translate("StarList", "TextLabel"))
        self.label_248.setText(_translate("StarList", "TextLabel"))
        self.label_249.setText(_translate("StarList", "TextLabel"))
        self.label_250.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_41.setText(_translate("StarList", "CommandLinkButton"))
        self.label_251.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_431.setText(_translate("StarList", "PushButton"))
        self.pushButton_432.setText(_translate("StarList", "PushButton"))
        self.pushButton_433.setText(_translate("StarList", "PushButton"))
        self.pushButton_434.setText(_translate("StarList", "PushButton"))
        self.pushButton_435.setText(_translate("StarList", "PushButton"))
        self.pushButton_436.setText(_translate("StarList", "PushButton"))
        self.pushButton_437.setText(_translate("StarList", "PushButton"))
        self.pushButton_438.setText(_translate("StarList", "PushButton"))
        self.pushButton_439.setText(_translate("StarList", "PushButton"))
        self.label_252.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_42.setText(_translate("StarList", "info"))
        self.item_42.setText(_translate("StarList", "TextLabel"))
        self.label_253.setText(_translate("StarList", "TextLabel"))
        self.label_254.setText(_translate("StarList", "TextLabel"))
        self.label_255.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_42.setText(_translate("StarList", "CommandLinkButton"))
        self.label_256.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_440.setText(_translate("StarList", "PushButton"))
        self.pushButton_441.setText(_translate("StarList", "PushButton"))
        self.pushButton_442.setText(_translate("StarList", "PushButton"))
        self.pushButton_443.setText(_translate("StarList", "PushButton"))
        self.pushButton_444.setText(_translate("StarList", "PushButton"))
        self.pushButton_445.setText(_translate("StarList", "PushButton"))
        self.pushButton_446.setText(_translate("StarList", "PushButton"))
        self.pushButton_447.setText(_translate("StarList", "PushButton"))
        self.pushButton_448.setText(_translate("StarList", "PushButton"))
        self.label_257.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_43.setText(_translate("StarList", "info"))
        self.item_43.setText(_translate("StarList", "TextLabel"))
        self.label_258.setText(_translate("StarList", "TextLabel"))
        self.label_259.setText(_translate("StarList", "TextLabel"))
        self.label_260.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_43.setText(_translate("StarList", "CommandLinkButton"))
        self.label_261.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_449.setText(_translate("StarList", "PushButton"))
        self.pushButton_450.setText(_translate("StarList", "PushButton"))
        self.pushButton_451.setText(_translate("StarList", "PushButton"))
        self.pushButton_452.setText(_translate("StarList", "PushButton"))
        self.pushButton_453.setText(_translate("StarList", "PushButton"))
        self.pushButton_454.setText(_translate("StarList", "PushButton"))
        self.pushButton_455.setText(_translate("StarList", "PushButton"))
        self.pushButton_456.setText(_translate("StarList", "PushButton"))
        self.pushButton_457.setText(_translate("StarList", "PushButton"))
        self.label_262.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_44.setText(_translate("StarList", "info"))
        self.item_44.setText(_translate("StarList", "TextLabel"))
        self.label_263.setText(_translate("StarList", "TextLabel"))
        self.label_264.setText(_translate("StarList", "TextLabel"))
        self.label_265.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_44.setText(_translate("StarList", "CommandLinkButton"))
        self.label_266.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_458.setText(_translate("StarList", "PushButton"))
        self.pushButton_459.setText(_translate("StarList", "PushButton"))
        self.pushButton_460.setText(_translate("StarList", "PushButton"))
        self.pushButton_461.setText(_translate("StarList", "PushButton"))
        self.pushButton_462.setText(_translate("StarList", "PushButton"))
        self.pushButton_463.setText(_translate("StarList", "PushButton"))
        self.pushButton_464.setText(_translate("StarList", "PushButton"))
        self.pushButton_465.setText(_translate("StarList", "PushButton"))
        self.pushButton_466.setText(_translate("StarList", "PushButton"))
        self.label_267.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_45.setText(_translate("StarList", "info"))
        self.item_45.setText(_translate("StarList", "TextLabel"))
        self.label_268.setText(_translate("StarList", "TextLabel"))
        self.label_269.setText(_translate("StarList", "TextLabel"))
        self.label_270.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_45.setText(_translate("StarList", "CommandLinkButton"))
        self.label_271.setText(_translate("StarList", "<html><head/><body><p align=\"center\">Series List</p></body></html>"))
        self.pushButton_467.setText(_translate("StarList", "PushButton"))
        self.pushButton_468.setText(_translate("StarList", "PushButton"))
        self.pushButton_469.setText(_translate("StarList", "PushButton"))
        self.pushButton_470.setText(_translate("StarList", "PushButton"))
        self.pushButton_471.setText(_translate("StarList", "PushButton"))
        self.pushButton_472.setText(_translate("StarList", "PushButton"))
        self.pushButton_473.setText(_translate("StarList", "PushButton"))
        self.pushButton_474.setText(_translate("StarList", "PushButton"))
        self.pushButton_475.setText(_translate("StarList", "PushButton"))
        self.label_272.setText(_translate("StarList", "TextLabel"))
        self.buttonInfo_46.setText(_translate("StarList", "info"))
        self.item_46.setText(_translate("StarList", "TextLabel"))
        self.label_273.setText(_translate("StarList", "TextLabel"))
        self.label_274.setText(_translate("StarList", "TextLabel"))
        self.label_275.setText(_translate("StarList", "TextLabel"))
        self.commandLinkButton_46.setText(_translate("StarList", "CommandLinkButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = stars()
    ui.show()
    sys.exit(app.exec_())
