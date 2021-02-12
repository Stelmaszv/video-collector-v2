from PyQt5 import QtGui,QtCore, QtWidgets
from core.BaseActions import ViewBaseAction
from app.db.models import session
from core.setWindow import Router
from core.rezolution import SetResolution
class Form:

    buttons_loop=[]

    def __init__(self,obj):
        self.obj = obj

    def combo_box(self,data,list):
        combo_box = QtWidgets.QComboBox(self.obj)
        combo_box.setGeometry(data[0], data[1], data[2], data[3])
        combo_box.addItems(list)
        return combo_box

    def label(self,info,data,grid,el=None):
        if el is not None:
            el=self.obj

        label = QtWidgets.QLabel(el)
        label.setObjectName(info[0])
        label.setText(info[1])
        grid.addWidget(label, data[0], data[1], data[2], data[3])
        return label

    def buttom_genarator(self,list,fuction,id):
        for button in list.buttons():
            if button is list.button(id):
                fuction(list.button(id).data)

    def buttom_genarator2(self,list,fuction,id):
        for button in list.buttons():
            if button is list.button(id):
                fuction(list.button(id).data)

    def button_loop(self, el, grid, item, data, info, index):
        button = QtWidgets.QPushButton(el)
        button.setMinimumSize(QtCore.QSize(30, 0))
        button.setMaximumSize(QtCore.QSize(10, 16777215))
        button.setObjectName("InfoButton")
        button.setText(info[0])
        button.data = item
        grid.addWidget(button, data[0], data[1], data[2], data[3])
        self.buttons_loop[index]['obejct'].addButton(button)
        self.buttons_loop[index]['obejct'].buttonClicked[int].connect(self.buttons_loop[index]['button'])

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
        from .helper import Message, Pagination, Scroller
        self.obj=obj
        self.menu=Router(self.obj)
        self.data=data
        if obj.model is not None:
            self.model=obj.model
        self.Form = Form(self.obj)
        self.Massage=Message()
        self.pagination = Pagination(self.obj)
        self.Scroller=Scroller(self.obj)

    def load_view(self,view,item=False):
        self.menu.searchIn=view
        self.menu.open(item)

    def clear(self):
        self.avatar_photo.clear()
        self.galeryGrid.close()
        self.infoWidget.close()
        self.title.clear()

    def upadete(self):
        self.avatar_photo.show()

    def button(self,data,button):
        self.Form.button(
            [button['item_name'], button['name']],
            data,
            button['button'],
            None,
            [],
            []
        )

    def listView(self, data, data_list,obj_name,QWidget=False,page=False):
        from .section import SeriesSection, StarsSection, MenuSection,MovieListSection,TagsListSection

        switcher = {
            'Stars'      : StarsSection(self,QWidget),
            'Series'     : SeriesSection(self,QWidget),
            'Menu'       : MenuSection(self,QWidget),
            'Movie_List' : MovieListSection(self,QWidget),
            'Tags'       : TagsListSection(self, QWidget)
        }

        classObj = switcher.get(obj_name, "Invalid data");
        section_obj=classObj.run(data, data_list,page)
        return section_obj

    def get_nav2(self,data,buttons=[]):
        self.nav_widget = QtWidgets.QWidget(self.obj)
        self.nav_widget.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.nav_widget.setObjectName("movie-navbar")
        self.nav_grid = QtWidgets.QGridLayout(self.nav_widget)
        self.nav_grid.setContentsMargins(0, 0, 0, 0)
        self.nav_grid.setObjectName("movie-grid")
        self.Form.button(['open', 'Open'], [], buttons[0], self.nav_grid, [0, 0, 2, 2], [100, 0, 10, 16777215])
        self.Form.button(['favirite', 'Favirite'], [], buttons[1], self.nav_grid, [0, 1, 2, 2], [100, 0, 10, 16777215])
        self.Form.button(['edit', 'Edit'], [], buttons[2], self.nav_grid, [0, 2, 2, 2], [100, 0, 10, 16777215])
        self.Form.button(['Delete', 'Delete'], [], buttons[3], self.nav_grid, [0, 3, 2, 2], [100, 0, 10, 16777215])

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
        return self.avatar_photo

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

    def get_nav(self,data,buttons=[]):
        self.nav_widget = QtWidgets.QWidget(self.obj)
        self.nav_widget.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.nav_widget.setObjectName("movie-navbar")
        self.nav_grid = QtWidgets.QGridLayout(self.nav_widget)
        self.nav_grid.setContentsMargins(0, 0, 0, 0)
        self.nav_grid.setObjectName("movie-grid")
        row=0
        for button in buttons:
            self.Form.button([button['item_name'], button['name']], [],button['button'], self.nav_grid, [0, row, 2, 2], [100, 0, 10, 16777215])
            row=row+1

    def description(self,text,data,obj=None):
        if obj==None:
            obj=self.obj
        self.description = QtWidgets.QWidget(obj)
        self.description_Grid = QtWidgets.QGridLayout(self.description)
        self.description_Grid.setContentsMargins(0, 0, 0, 0)
        self.description_Grid.setObjectName("infoGrid")
        col2 = QtWidgets.QLabel(self.description)
        self.description.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        col2.setObjectName("col2")
        col2.setText(text)
        col2.setWordWrap(True)
        self.description_Grid.addWidget(col2,0, 0, 2, 2)

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
class AbstractBaseView:

    Nav    = None
    model  = None
    resolution_index=''
    list_view=''
    show_elemnts=[]

    def __init__(self):
        self.BaseView = BaseView([], self)
        self.BaseActions = ViewBaseAction(self)
        self.SetResolution = SetResolution()
        self.__set_resolution()
        if self.Nav is not None:
            self.NavObj = self.Nav(self.BaseActions)

    def __set_resolution(self):
        self.left = self.SetResolution.menu_set[self.resolution_index]['position']['left']
        self.top = self.SetResolution.menu_set[self.resolution_index]['position']['top']
        self.width = self.SetResolution.menu_set[self.resolution_index]['position']['width']
        self.height = self.SetResolution.menu_set[self.resolution_index]['position']['height']
        self.WindowSize = self.SetResolution.menu_set[self.resolution_index]['window']

    def ___set_data(self):
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data

    def  set_up(self):
        pass

    def galery(self):
        data = self.WindowSize['galery_size']
        data_size = self.WindowSize['galery_photo_size']
        self.BaseView.galery(data, data_size, self.WindowSize['galery_item_show'])

    def get_nav(self):
        data = self.WindowSize['navbar']
        self.BaseView.get_nav(
            data,
            self.NavObj.set_nav()
        )

    def init(self):
        self.title()
        self.setWindowTitle(self.window_title)
        self.info()
        self.galery()
        self.get_nav()
        self.def_list_view()
        self.BaseView.avatar(self.WindowSize['avatar_size'], self, self.data.avatar)

    def def_list_view(self):
        data= self.WindowSize['list_view_size']
        self.BaseView.listView(data, self.data.movies,self.list_view,self)


    def info(self):

        data   = self.WindowSize['info_size']

        rows = ['itemNmae','itemName2']

        inf_data=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.BaseView.info(inf_data, data, rows)

    def title(self):
        data = self.WindowSize['title_size']
        self.window_title=self.data.name
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def run_window(self):
        self.___set_data()
        self.set_up()
        self.init()
        self.show()
        self.setGeometry(self.left, self.top, self.width, self.height)
