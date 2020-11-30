from PyQt5 import QtGui,QtCore, QtWidgets
from PyQt5.QtWidgets import  QWidget,QPushButton,QMessageBox
from app.db.models import session
from core.setWindow import Router
from .list import List

class Pagination:

    def __init__(self,obj):
        self.obj=obj

    def tabs(self,data):
        tab = QtWidgets.QTabWidget(self.obj)
        tab.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        tab.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        tab.setObjectName("tabWidget")
        return tab

    def tab(self):
        tab = QtWidgets.QWidget()
        tab.setObjectName("tab")
        return tab

class Scroller:

    def __init__(self,obj):
        self.obj=obj
        self.List=List

    def scroll_area(self,data,obj=None):
        if self.obj == None:
            obj=self.obj

        scroll_area_obj = QtWidgets.QScrollArea(obj)
        scroll_area_obj.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        scroll_area_obj.setWidgetResizable(True)
        scroll_area_obj.setObjectName("scrollArea")
        return  scroll_area_obj

    def scroll_area_widget_contents(self):
        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 499))
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        return scrollAreaWidgetContents

    def grid_for_scroll (self):
        grid_for_scroll_obj = QtWidgets.QGridLayout()
        grid_for_scroll_obj.setObjectName("gridLayout")
        return grid_for_scroll_obj

    def vertical_layout(self,obj):
        vertical_Layout_grid = QtWidgets.QVBoxLayout(obj)
        vertical_Layout_grid.setObjectName("verticalLayout")
        return vertical_Layout_grid

    def run(self,data,obj):
        self.scrollArea = self.scroll_area([400, 10, 780, 850], obj)
        self.scrollAreaWidgetContents = self.scroll_area_widget_contents()
        self.verticalLayout = self.vertical_layout(self.scrollAreaWidgetContents)
        self.grid_for_scroll = self.grid_for_scroll()

    def movie_list(self,list,menu):
        List(menu).generate_list(
            'movies',
            list,
            self.scrollAreaWidgetContents,
            self.grid_for_scroll,
            1,
        )
        self.verticalLayout.addLayout(self.grid_for_scroll)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

class Form:

    def __init__(self,obj):
        self.obj = obj

    def combo_box(self,data,list):
        combo_box = QtWidgets.QComboBox(self.obj)
        combo_box.setGeometry(data[0], data[1], data[2], data[3])
        combo_box.addItems(list)
        return combo_box

    def button(self,info,data,click=None,grid=None):
        button = QtWidgets.QPushButton(self.obj)
        button.setGeometry(data[0], data[1], data[2], data[3])
        button.setObjectName(info[0])
        button.setText(info[1])
        if click is not None:
            button.clicked.connect(click)
        if grid is not None:
            grid.addWidget(button)

    def edit_line(self,data,placeholder):
        line = QtWidgets.QLineEdit(self.obj)
        line.setPlaceholderText(placeholder)
        line.setGeometry(data[0], data[1], data[2], data[3])
        return line

class Message:

    def show(self,data):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(data[0])
        msg.setInformativeText(data[1])
        msg.setWindowTitle(data[2])
        msg.exec_()

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

    def get_nav(self,data,obj=None):
        if obj==None:
            obj=self.obj

        self.ManuWidget = QtWidgets.QWidget(obj)
        self.ManuWidget.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.ManuWidget.setObjectName("infoWidget")
        self.ManuGrid = QtWidgets.QGridLayout(self.ManuWidget)
        self.ManuGrid.setContentsMargins(0, 0, 0, 0)
        self.ManuGrid.setObjectName("infoGrid")

        open = QtWidgets.QPushButton(self.ManuWidget)
        open.setMinimumSize(QtCore.QSize(100, 0))
        open.setMaximumSize(QtCore.QSize(10, 16777215))
        open.setObjectName("col1")
        open.setText('Open')
        self.ManuGrid.addWidget(open, 0, 0, 2, 2)

        favirite = QtWidgets.QPushButton(self.ManuWidget)
        favirite.setMinimumSize(QtCore.QSize(100, 0))
        favirite.setMaximumSize(QtCore.QSize(10, 16777215))
        favirite.setObjectName("col1")
        favirite.setText('favirite')
        self.ManuGrid.addWidget(favirite, 0, 1, 2, 2)

        edit = QtWidgets.QPushButton(self.ManuWidget)
        edit.setMinimumSize(QtCore.QSize(100, 0))
        edit.setMaximumSize(QtCore.QSize(10, 16777215))
        edit.setObjectName("col1")
        edit.setText('edit')
        self.ManuGrid.addWidget(edit, 0, 2, 2, 2)

        delete = QtWidgets.QPushButton(self.ManuWidget)
        delete.setObjectName("col1")
        delete.setText('Delete')
        delete.setMinimumSize(QtCore.QSize(100, 0))
        delete.setMaximumSize(QtCore.QSize(10, 16777215))
        self.ManuGrid.addWidget(delete, 0, 2, 2, 2)

    def n_title(self,obj):
        button = QPushButton('PyQt5 button', obj)
        button.setToolTip('This is an example button')
        button.move(100, 70)


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

    def closeEvent(self, event):
        print(event)

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

    def close(self):
        print('dqwd')
