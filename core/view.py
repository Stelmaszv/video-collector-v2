from PyQt5 import QtGui,QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget,QPushButton
from app.db.models import session
from core.setWindow import Router
from .helper import Message,Pagination,Scroller

class Form:

    def __init__(self,obj):
        self.obj = obj

    def combo_box(self,data,list):
        combo_box = QtWidgets.QComboBox(self.obj)
        combo_box.setGeometry(data[0], data[1], data[2], data[3])
        combo_box.addItems(list)
        return combo_box

    def button(self,info,data=[],click=None,gird=None,grid_pos=[],size=[]):
        button = QtWidgets.QPushButton(self.obj)
        button.setObjectName(info[0])
        button.setText(info[1])

        if len(data):
            button.setGeometry(data[0], data[1], data[2], data[3])

        if len(size):
            button.setMinimumSize(QtCore.QSize(size[0], size[1]))
            button.setMaximumSize(QtCore.QSize(size[2], size[3]))

        if click is not None:
            button.clicked.connect(click)
        if gird is not None and len(grid_pos):
            gird.addWidget(button, grid_pos[0], grid_pos[1], grid_pos[2], grid_pos[3])

    def edit_line(self,data,placeholder):
        line = QtWidgets.QLineEdit(self.obj)
        line.setPlaceholderText(placeholder)
        line.setGeometry(data[0], data[1], data[2], data[3])
        return line

class BaseView:

    def __init__(self,data,obj):
        self.obj=obj
        self.menu=Router(self.obj)
        self.data=data
        if obj.model is not None:
            self.model=obj.model
        self.form = Form(self.obj)
        self.Massage=Message()
        self.pagination = Pagination(self.obj)
        self.Scroller=Scroller(self.obj)

    def load_view(self,view,item=False):
        self.menu.searchIn=view
        self.menu.open(item)

    def listView(self, data, data_list,obj_name):

        from .section import SeriesSection, StarsSection, MenuSection

        switcher = {
            'Stars'    : StarsSection(self),
            'Series'   : SeriesSection(self),
            'Menu'     : MenuSection(self)
        }
        classObj = switcher.get(obj_name, "Invalid data");
        classObj.run(data, data_list)

    def get_nav(self,data,buttons=[]):
        self.ManuWidget = QtWidgets.QWidget(self.obj)
        self.ManuWidget.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.ManuWidget.setObjectName("movie-navbar")
        self.ManuGrid = QtWidgets.QGridLayout(self.ManuWidget)
        self.ManuGrid.setContentsMargins(0, 0, 0, 0)
        self.ManuGrid.setObjectName("movie-grid")
        self.form.button(['open', 'open'],[],buttons[0],self.ManuGrid,[0,0,2,2],[100,0,10,16777215])
        self.form.button(['favirite', 'favirite'], [], buttons[1], self.ManuGrid,[0,1,2,2], [100, 0, 10, 16777215])
        self.form.button(['edit', 'edit'], [], buttons[2], self.ManuGrid, [0, 2, 2, 2], [100, 0, 10, 16777215])
        self.form.button(['Delete', 'Delete'], [], buttons[3], self.ManuGrid, [0, 3, 2, 2], [100, 0, 10, 16777215])

    def title(self,data,text):
        self.title = QtWidgets.QLabel(self.obj)
        self.title.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.title.setObjectName("title")
        self.title.setText(text)

    def avatar(self,data,obj=None,src=None):
        if obj == None:
            obj = self.obj
        if src == None:
            src = self.data.avatar
        self.avatar_photo = QtWidgets.QLabel(obj)
        self.avatar_photo.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.avatar_photo.setText("")
        self.avatar_photo.setPixmap(QtGui.QPixmap(src))
        self.avatar_photo.setScaledContents(True)
        self.avatar_photo.setObjectName("avatar")

    def info(self,infoData,data,rows,obj=None):
        if obj==None:
            obj=self.obj
        self.infoWidget = QtWidgets.QWidget(obj)
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

    def set_data(self,id):
        if self.model:
            self.data = session.query(self.model).get(id)

    def galery(self,data,size,inRow,obj=None,photos=None):
        if photos == None:
            photos = self.data.photos
        if obj == None:
            obj = self.obj

        self.galeryGrid = QtWidgets.QWidget(obj)
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

class AbstractView(QWidget):

    width_val=1920
    height_val= 1080

    def __init__(self):
        super(AbstractView, self).__init__()

    def setupUi(self):
        pass

    def createObj(self):
        self.obj = QtWidgets.QMainWindow()
        self.obj.setObjectName("StarList")
        self.obj.resize(self.width_val, self.height_val)

    def show(self,data=None):
        if data is not None:
            self.id = data.id

        self.createObj()

        self.setBaseView(data,self)
        self.getOne()
        self.setupUi()
        QtCore.QMetaObject.connectSlotsByName(self.obj)
        self.obj.show()

    def setBaseView(self,data,obj):
        self.baseView = BaseView(data, obj)

