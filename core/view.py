import os
from PyQt5 import QtGui,QtCore, QtWidgets
from core.BaseActions import ViewBaseAction
from app.db.models import session
from core.setWindow import Router
from core.rezolution import SetResolution
from core.arraymanipulation import ArrayManipulation
from core.custum_errors import Error
from core.db.config import Base as BaseModel
from app.nav import BaseNav
from app.info import BaseInfo
from core.BaseActions import FormSection,Submit,Form
from app.model_view import BaseModelViewSet
from core.strings import stringManipupations
import json

class BaseFormShema:
    from_section=[]
    def __init__(self, BaseView,methods=[]):
        self.BaseView = BaseView
        self.chcek_nethods(methods)
        self.methods=methods
        self.form()

    def chcek_nethods(self,methods):
        for method in methods:
            Error.throw_error_bool(str(method)+' not exist in Baseview ',self.is_method(method))

    def form(self):
        pass

    def get_files_in_dir(self,defult):
        dir=self.BaseView.data.dir + '' +str('/photo')
        dir_loop=[]
        dir_loop.append(defult)
        for item in os.listdir(dir):
            dir_loop_elment=dir + '/' +str(item)
            dir_loop.append(dir_loop_elment)
        return dir_loop

    def set_value_if_exist(self,value,empty):
        if value is None :
            return empty
        return str(value)

    def return_from_section(self):
        return self.from_section

    def add_method(self,method,method_str):

        if method_str in self.methods is not True:
            return  method
        else:
            Error.throw_error_bool(str(method_str) + ' not exist in Baseview ', False)

    def is_method(self, method):
        return callable(getattr(self.BaseView, method, None))

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

    def load_view(self,view,item=False,list=False):
        self.menu.search_In=view
        self.menu.open(item,list)

    def clear(self):
        self.avatar_photo.clear()
        self.galeryGrid.close()
        self.infoWidget.close()


    def upadete(self):
        self.avatar_photo.show()

    def listView(self, data, data_list,obj_name,QWidget=False,page=False):
        from .section import SeriesSection, StarsSection, MenuSection,MovieListSection,TagsListSection,CustomListSection
        switcher = {
            'Stars'      : StarsSection(self,QWidget),
            'Series'     : SeriesSection(self,QWidget),
            'Menu'       : MenuSection(self,QWidget),
            'Movie_List' : MovieListSection(self,QWidget),
            'Tags'       : TagsListSection(self, QWidget),
            'Custom_list': CustomListSection(self,QWidget)
        }
        classObj = switcher.get(obj_name, "Invalid data");
        section_obj=classObj.run(data, data_list,page)
        return section_obj

    def title(self,data,text):
        title = QtWidgets.QLabel(self.obj)
        title.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        title.setObjectName(text)
        title.setText(text)

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

    def set_nav(self,data,buttons=[]):
        self.nav_widget = QtWidgets.QWidget(self.obj)
        self.nav_widget.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.nav_widget.setObjectName("movie-navbar")
        self.nav_grid = QtWidgets.QGridLayout(self.nav_widget)
        self.nav_grid.setContentsMargins(0, 0, 0, 0)
        self.nav_grid.setObjectName("movie-grid")
        for button in buttons:
            self.Form.button(button,self.nav_grid)

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

    def description(self,text,data,grid=None,obj=None):
        if obj==None:
            obj=self.obj
        description = QtWidgets.QLabel(self.obj)
        description.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        description.setText(text)
        description.setWordWrap(True)
        if grid is not None:
            grid.addWidget(description, data[0],data[1], data[2], data[3])

    def set_data(self,id):
        if self.model:
            self.data = session.query(self.model).get(id)

    def galery(self,data,size,inRow,obj=None):
        def faind_in_galery_skip(photo):
            with open(self.data.config) as json_file:
                json_pars = json.load(json_file)
                if 'galery_skip' in json_pars:
                    if photo in json_pars['galery_skip']:
                        return False
            return True
        if obj == None:
            obj = self.obj
        photos = os.listdir(self.data.dir + '/photo')
        self.galeryGrid = QtWidgets.QWidget(obj)
        self.galeryGrid.setGeometry(QtCore.QRect(data[0],data[1],data[2],data[3]))
        self.galeryGrid.setObjectName("galeryGrid")

        self.galeryGrid2 = QtWidgets.QGridLayout(self.galeryGrid)
        self.galeryGrid2.setContentsMargins(0, 0, 0, 0)
        self.galeryGrid2.setObjectName("galeryGrid2")
        row = 0
        col = 0
        for photo in photos:
            if faind_in_galery_skip(photo):
                item = QtWidgets.QLabel(self.galeryGrid)
                item.setMaximumSize(QtCore.QSize(size[0], size[1]))
                item.setText("")
                item.setPixmap(QtGui.QPixmap(self.data.dir+'/photo/'+photo))
                item.setScaledContents(True)
                item.setObjectName("galeryItem")
                self.galeryGrid2.addWidget(item, col, row, 1, 1)
                row = row + 1
                if row > inRow:
                    row = 0
                    col = col + 1

class AbstractBaseView:

    session            = session
    Nav                = None
    Info               = None
    model              = None
    FormSchema         = None
    ModelView          = None
    data               = None
    list_data          = None
    list_model_off     = False
    model_view_off     = False
    debug_mode         = True
    window_title=''
    resolution_index=''
    list_view=''
    show_elemnts=[]
    methods =  []
    list=[]

    def __init__(self):
        if self.model is not None:
            Error.throw_error_bool('class self.model is not subclass of BaseModel', issubclass(self.model, BaseModel))
        self.BaseView = BaseView([], self)
        self.FormSection = FormSection(self)
        self.BaseActions = ViewBaseAction(self)
        self.SetResolution = SetResolution()
        self.__set_resolution()

        if self.Info is not None:
            Error.throw_error_bool('class self.Info is not subclass of BaseInfo', issubclass(self.Info, BaseInfo))
            self.InfoObj=self.Info(self)

        if self.Nav is not None:
            Error.throw_error_bool('class self.Nav is not subclass of BaseNav', issubclass(self.Nav, BaseNav))
            self.NavObj = self.Nav(self.BaseActions)

    def up_date_views(self):
        if self.data is not None:
            self.data.views=self.data.views+1
            session.commit()

    def form_section(self):
        Error.throw_error_bool('class self.FormSchema is not subclass of BaseFormSection', issubclass(self.FormSchema, BaseFormShema))
        if self.model_view_off is False:
            Error.throw_error_is_none('self.ModelView is required for form section !', self.ModelView)
            Error.throw_error_bool('class self.ModelView is not subclass of BaseModelViewSet',
                               issubclass(self.ModelView, BaseModelViewSet))
        self.FormSchemaObj = self.FormSchema(self, self.methods)
        data_line = self.WindowSize['form_section']
        buttons = self.FormSchemaObj.return_from_section()
        if self.model_view_off is False:
            self.Submit = Submit(self.ModelView, self.data, self)
        self.FormSection.form_section(data_line,buttons)


    def __set_resolution(self):

        if self.resolution_index in self.SetResolution.menu_set:
            if 'position' in self.SetResolution.menu_set[self.resolution_index]:
                self.left = self.SetResolution.menu_set[self.resolution_index]['position']['left']
                self.top = self.SetResolution.menu_set[self.resolution_index]['position']['top']
                self.width = self.SetResolution.menu_set[self.resolution_index]['position']['width']
                self.height = self.SetResolution.menu_set[self.resolution_index]['position']['height']
            else:
                Error.throw_error('position not found in resolution index ('+self.resolution_index+')')
            if 'window' in self.SetResolution.menu_set[self.resolution_index]:
                self.WindowSize = self.SetResolution.menu_set[self.resolution_index]['window']
            else:
                Error.throw_error('window not found in resolution index ('+self.resolution_index+')')
        else:
            Error.throw_error('Resolution index "' + self.resolution_index + '" menu not found')

    def ___set_data(self):
        if self.model is not None:
            self.BaseView.set_data(self.id)
            self.data = self.BaseView.data

    def set_model(self,model):
        self.model=model

    def set_data(self,data):
        self.data=data

    def  set_up(self):
        pass

    def galery(self):
        data = self.WindowSize['galery_size']
        data_size = self.WindowSize['galery_photo_size']
        self.BaseView.galery(data, data_size, self.WindowSize['galery_item_show'])

    def get_nav(self):
        data = self.WindowSize['navbar']
        self.BaseView.set_nav(
            data,
            self.NavObj.set_nav()
        )

    def check_model(self,error):
        Error.throw_error_is_none(error,self.model)

    def check_nav(self):
        Error.throw_error_is_none('self.Nav is required for navbar!', self.Nav)

    def check_info(self):
        Error.throw_error_is_none('self.Info is required for info Section!', self.Info)
        Error.throw_error_bool('class self.Info is not subclass of BaseInfo', issubclass(self.Info, BaseInfo))

    def description(self):
        description_stan = 'description' in self.WindowSize and 'description_limit' in self.WindowSize
        Error.throw_error_bool('description or description_limit not found in WindowSize ', description_stan)
        data = self.WindowSize['description']
        limit = self.WindowSize['description_limit']
        self.BaseView.description(stringManipupations.short(self.data.description, limit), data);

    def tags(self):
        tag_stan='tags' in self.WindowSize and 'tags_limit' in self.WindowSize
        Error.throw_error_bool('tags or tags_limit not found in WindowSize ', tag_stan)
        data = self.WindowSize['tags']
        limit = self.WindowSize['tags_limit']
        tags_list=stringManipupations.array_to_string(self.data.tags)
        self.BaseView.description(stringManipupations.short(tags_list, limit), data);


    def init(self):
        self.up_date_views()
        if ArrayManipulation.faind_index_in_array(self.show_elemnts, 'Tags'):
            if self.data is not None:
                self.tags()
        if ArrayManipulation.faind_index_in_array(self.show_elemnts, 'Description'):
            if self.data is not None:
                self.description()
        if ArrayManipulation.faind_index_in_array(self.show_elemnts,'Title') or self.window_title:
            if len(self.window_title)==0:
                self.check_model('self.model is required for Title Section !')
            self.title()
            self.setWindowTitle(self.window_title)
        if ArrayManipulation.faind_index_in_array(self.show_elemnts, 'Info'):
            self.check_info()
            self.info()
        if ArrayManipulation.faind_index_in_array(self.show_elemnts, 'Galery'):
            self.check_model('self.model is required for Galery Section !')
            self.galery()
        if ArrayManipulation.faind_index_in_array(self.show_elemnts, 'Nav'):
            self.check_nav()
            self.get_nav()
        if ArrayManipulation.faind_index_in_array(self.show_elemnts, 'List'):
            if self.list_model_off is False:
                self.check_model('self.model is required for List Section !')
            self.list_view_def()
        if ArrayManipulation.faind_index_in_array(self.show_elemnts, 'Avatar'):
            self.check_model('self.model is required for Avatar Section !')
            self.BaseView.avatar(self.WindowSize['avatar_size'], self, self.data.avatar)
        if self.FormSchema is not None:
            self.form_section()

    def set_list_view_data(self,data):
        self.list_data=data

    def list_view_def(self):
        if len(self.list_view):
            data= self.WindowSize['list_view_size']
            Error.throw_error_is_none("List_data is None 'use method set_list_view_data'", self.list_data)
            self.BaseView.listView(data, self.list_data,self.list_view,self)

    def custom_title(self,title,rezolution):
        data = self.WindowSize[rezolution]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + title + \
               "</span></p></body></html>"

        self.BaseView.title(data, text)

    def custom_list(self,list,rezolution,list_item):
        data = self.WindowSize[rezolution]
        self.BaseView.listView(data, list, list_item, self)

    def info(self):
        data   = self.WindowSize['info_size']
        rows = ['itemNmae','itemName2']
        inf_data=self.InfoObj.return_data()
        self.BaseView.info(inf_data, data, rows)


    def title(self):
        title =''
        if self.data is not None:
            title = self.data.name
        if len(self.window_title)>0:
            title=self.window_title
        data = self.WindowSize['title_size']
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + title + \
               "</span></p></body></html>"

        self.BaseView.title(data, text)

    def run_window(self):
        self.___set_data()
        self.set_up()
        self.init()
        self.show()
        self.setGeometry(self.left, self.top, self.width, self.height)
