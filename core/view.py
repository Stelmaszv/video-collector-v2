import os
import json
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
from app.forms import BaseFormShema
from core.setings import photo_ext,show_list_defult

class BaseView:

    rezolution = []
    list_view_type=''

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

    def listView(self, data, data_list,obj_name,QWidget=None):
        from .section import SeriesSection, StarsSection, MenuSection,MovieListSection,\
            TagsListSection,CustomListSection,EditGalerySection,EditGaleryMoviesSection,\
            ProducentSection
        page=False
        if QWidget:
            if hasattr(QWidget,'page'):
                page = QWidget.page
        switcher = {
            'Producent'  : ProducentSection(self,QWidget),
            'Stars'      : StarsSection(self,QWidget),
            'Series'     : SeriesSection(self,QWidget),
            'Menu'       : MenuSection(self,QWidget),
            'Movie_List' : MovieListSection(self,QWidget),
            'Tags'       : TagsListSection(self, QWidget),
            'Custom_list': CustomListSection(self,QWidget),
            'EditGalery' : EditGalerySection(self,QWidget),
            'EditGaleryMovies': EditGaleryMoviesSection(self, QWidget),
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
            self.Form.button(
                [button['item_name'], button['name']],
                [],button['button'], self.nav_grid,
                [0, row, 2, 2], [100, 0, 10, 16777215])
            row=row+1

    def description(self,text,data,grid=None,obj=None):
        if obj==None:
            obj=self.obj
        description = QtWidgets.QLabel(obj)
        description.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\"" \
               "text-decoration: none;\">" + text + \
               "</span></p></body></html>"

        description.setText(text)
        description.setWordWrap(True)
        if grid is not None:
            grid.addWidget(description, data[0],data[1], data[2], data[3])

    def set_data(self,id):
        if self.model:
            self.data = session.query(self.model).get(id)

    def galery_from_array(self,data,size,inRow,array,obj=None):
        if obj == None:
            obj = self.obj

        self.galeryGrid = QtWidgets.QWidget(obj)
        self.galeryGrid.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.galeryGrid.setObjectName("galeryGrid")

        self.galeryGrid2 = QtWidgets.QGridLayout(self.galeryGrid)
        self.galeryGrid2.setContentsMargins(0, 0, 0, 0)
        self.galeryGrid2.setObjectName("galeryGrid2")
        row = 0
        col = 0
        for photo in array:
            item = QtWidgets.QLabel(self.galeryGrid)
            item.setMaximumSize(QtCore.QSize(size[0], size[1]))
            item.setText("")
            item.setPixmap(QtGui.QPixmap(photo))
            item.setScaledContents(True)
            item.setObjectName("galeryItem")
            self.galeryGrid2.addWidget(item, col, row, 1, 1)
            row = row + 1
            if row > inRow:
                row = 0
                col = col + 1

    def galery(self,data,size,inRow,dir='',obj=None):
        def faind_in_galery_skip(photo):
            stan=True
            skip_galery=self.data.dir+'\\skip_galery.JSON'
            if os.path.isfile(skip_galery):
                with open(skip_galery) as sg:
                    json_pars = json.load(sg)
                    for photo_item in json_pars:
                        if photo == photo_item:
                            stan=False
            return stan

        if len(dir) == 0:
            dir = self.data.dir + '/photo'
        row = 0
        col = 0

        if obj == None:
            obj = self.obj

        photos = os.listdir(dir)

        self.galeryGrid = QtWidgets.QWidget(obj)
        self.galeryGrid.setGeometry(QtCore.QRect(data[0],data[1],data[2],data[3]))
        self.galeryGrid.setObjectName("galeryGrid")

        self.galeryGrid2 = QtWidgets.QGridLayout(self.galeryGrid)
        self.galeryGrid2.setContentsMargins(0, 0, 0, 0)
        self.galeryGrid2.setObjectName("galeryGrid2")
        for photo in photos:
            if photo.endswith(photo_ext) and faind_in_galery_skip(photo):
                item = QtWidgets.QLabel(self.galeryGrid)
                item.setMaximumSize(QtCore.QSize(size[0], size[1]))
                item.setText("")
                item.setPixmap(QtGui.QPixmap(dir + '/' + photo))
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
    custum_galery      = ''
    show_list          = show_list_defult
    window_title=''
    resolution_index=''
    list_view=''
    show_elemnts=[]
    methods =  []
    list=[]

    def __init__(self):
        if self.model is not None:
            Error.throw_error_bool(Error.get_error(3), issubclass(self.model, BaseModel))
        self.BaseView = BaseView([], self)
        self.BaseView.list_view_type=self.show_list
        self.FormSection = FormSection(self)
        self.BaseActions = ViewBaseAction(self)
        self.SetResolution = SetResolution(self)
        self._set_resolution()

        if self.Info is not None:
            Error.throw_error_bool(Error.get_error(4), issubclass(self.Info, BaseInfo))
            self.InfoObj=self.Info(self)

        if self.Nav is not None:
            Error.throw_error_bool(Error.get_error(5), issubclass(self.Nav, BaseNav))
            self._NavObj = self.Nav(self)

    def set_data_on_init(self):
        pass

    def up_date_views(self):
        if self.data is not None:
            self.data.views=self.data.views+1
            session.commit()

    @property
    def return_mesage_obj(self):
        Error.throw_error_bool(
            'Dialog not exist in '+self.resolution_index,
            'dialog' in self.SetResolution.menu_set[self.resolution_index])
        self.BaseView.Massage.set_resolution(self.SetResolution.menu_set[self.resolution_index]['dialog'])
        return self.BaseView.Massage

    def custum_form(self,FormSchema,index,ModelView=None):
        Error.throw_error_bool(Error.get_error(6),
                               issubclass(FormSchema, BaseFormShema))
        FormSchemaObj = FormSchema(self)
        buttons = FormSchemaObj.return_from_section()
        Error.throw_error_bool('Index '+index+' not found in '+self.resolution_index,index in self.WindowSize)
        data_line = self.WindowSize[index]
        if ModelView:
            self.Submit = Submit(ModelView, self.data, self)
        self.FormSection.form_section(data_line, buttons)

    def form_section(self):
        Error.throw_error_bool('class self.FormSchema is not subclass of BaseFormSection', issubclass(self.FormSchema, BaseFormShema))
        if self.model_view_off is False:
            Error.throw_error_is_none('self.ModelView is required for form section !', self.ModelView)
            Error.throw_error_bool('class self.ModelView is not subclass of BaseModelViewSet',
                               issubclass(self.ModelView, BaseModelViewSet))
        self.FormSchemaObj = self.FormSchema(self)
        Error.throw_error_bool('Index form_section not found in ' + self.resolution_index,'form_section' in self.WindowSize)
        data_line = self.WindowSize['form_section']
        buttons = self.FormSchemaObj.return_from_section()
        if self.model_view_off is False:
            self.Submit = Submit(self.ModelView, self.data, self)
        self.FormSection.form_section(data_line,buttons)

    def _set_resolution(self):

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

    def set_data(self,data):
        self.data=data

    def set_up(self):
        pass

    def set_galery(self):
        pass

    def galery(self):
        if 'galery_size' in self.WindowSize:
            if 'galery_photo_size' in self.WindowSize:
                data = self.WindowSize['galery_size']
                data_size = self.WindowSize['galery_photo_size']
                if 'galery_photo_size' in self.WindowSize:
                    self.set_galery()
                    if len(self.custum_galery)==0:
                        self.BaseView.galery(data, data_size, self.WindowSize['galery_item_show'])
                    else:
                        if os.path.isdir(self.custum_galery):
                            self.BaseView.galery(data, data_size, self.WindowSize['galery_item_show'], self.custum_galery)
                        else:
                            Error.throw_error('self.custum_galery must be dir ! ')
                else:
                    Error.throw_error('galery_item_show not found in resolution index (' + self.resolution_index + ')')
            else:
                Error.throw_error('galery_photo_size not found in resolution index (' + self.resolution_index + ')')
        else:
            Error.throw_error('galery_size not found in resolution index (' + self.resolution_index + ')')

    def get_nav(self):
        self._NavObj.set_data(self.data)
        if 'navbar' in self.WindowSize:
            data = self.WindowSize['navbar']
            self.BaseView.set_nav(
                data,
                self._NavObj.set_nav()
            )
        else:
            Error.throw_error('navbar not found in resolution index (' + self.resolution_index + ')')

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

    def custum_description(self,index,limit_index,text):
        description_stan = index in self.WindowSize and limit_index in self.WindowSize
        Error.throw_error_bool(index+" or "+limit_index+" not found in WindowSize ", description_stan)
        data = self.WindowSize[index]
        limit = self.WindowSize[limit_index]
        self.BaseView.description(stringManipupations.short(text, limit), data);

    def tags(self):
        tag_stan='tags' in self.WindowSize and 'tags_limit' in self.WindowSize
        Error.throw_error_bool('tags or tags_limit not found in WindowSize ', tag_stan)
        data = self.WindowSize['tags']
        limit = self.WindowSize['tags_limit']
        Error.throw_error_bool('self.data do not have tags ', hasattr(self.data,'tags'))
        tags_list=stringManipupations.array_to_string(self.data.tags)
        self.BaseView.description(stringManipupations.short(tags_list, limit), data);

    def set_avatar(self):
        if 'avatar_size' in self.WindowSize:
            self.BaseView.avatar(self.WindowSize['avatar_size'], self, self.data.avatar)
        else:
            Error.throw_error('avatar_size not found in resolution index (' + self.resolution_index + ')')

    def _init(self):
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
            self.set_avatar()
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
        Error.throw_error_bool(rezolution+' do not have tags ',rezolution in self.WindowSize)
        data = self.WindowSize[rezolution]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">" + title + \
               "</span></p></body></html>"

        self.BaseView.title(data, text)

    def galery_from_array(self,array,index,index_size,row):
        Error.throw_error_bool('Index "'+index+'" not found!', index in self.WindowSize)
        Error.throw_error_bool('Index "'+index_size+'" not found!', index_size in self.WindowSize)
        Error.throw_error_bool('Index "' + row + '" not found!', row in self.WindowSize)
        def stars_array():
            new_code = []
            for star in array:
                new_code.append(star.avatar)
            return new_code

        self.BaseView.galery_from_array(self.WindowSize[index], self.WindowSize[index_size], self.WindowSize[row], stars_array())

    def custom_list(self,list,rezolution,list_item):
        data = self.WindowSize[rezolution]
        self.BaseView.listView(data, list, list_item, self)

    def info(self):
        if "info_size" in self.WindowSize:
            data   = self.WindowSize['info_size']
            rows = ['itemNmae','itemName2']
            inf_data=self.InfoObj.return_data()
            self.info_data_array=self.InfoObj.return_counter()
            self.BaseView.info(inf_data, data, rows)
        else:
            Error.throw_error('info_size not found in resolution index (' + self.resolution_index + ')')

    def get_dialog_location(self):
        Error.throw_error_bool(
            "Dialog not exist in resolution index "+self.resolution_index,
            "dialog" in self.SetResolution.menu_set[self.resolution_index]
        )
        return self.SetResolution.menu_set[self.resolution_index]['dialog']

    def title(self):
        title =''
        if self.data is not None:
            title = self.data.show_name
        if len(self.window_title)>0:
            title=self.window_title
        if "title_size" in self.WindowSize:
            data = self.WindowSize['title_size']
            text = "<html><head/><body>" \
                   "<p align=\"center\">" \
                   "<span style=\" font-size:18pt;font-weight:600; " \
                   "text-decoration: none;\">" + title + \
                   "</span></p></body></html>"
            self.BaseView.title(data, text)
            self.setWindowTitle(self.window_title)
        else:
            Error.throw_error('title_size not found in resolution index (' + self.resolution_index + ')')

    def after_init(self):
        pass

    def run_window(self):
        self.set_data_on_init()
        self.___set_data()
        self.set_up()
        self._init()
        self.after_init()
        self.show()
        self.setGeometry(self.left, self.top, self.width, self.height)
