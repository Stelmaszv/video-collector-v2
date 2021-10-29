from abc import ABC,abstractmethod
from PyQt5 import QtGui,QtCore, QtWidgets
from .list import List
from core.strings import stringManipupations
from .helper import Pagination, Scroller
from core.setings import series_avatar_defult
from core.BaseActions import Form
from app.info import SingleSectionInfo
from core.setings import photo_ext,data_JSON,menu_per_page
from core.dir import PhotoMeaker
import os
import json

class AbstractSection(ABC):

    @abstractmethod
    def run(self,data,data_list,page):
        pass

class CustomListSection(AbstractSection):

    def __init__(self, BaseView, QWidget):
        self.BaseView = BaseView
        self.OBJ_QWidget = QWidget
        self.obj = BaseView.obj

    def run(self,data,data_list,page):
        self.widget_edit_section = QtWidgets.QWidget(self.obj)
        self.widget_edit_section.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.widget_edit_section.setObjectName("widget_edit_section")
        self.edit_section_grid = QtWidgets.QGridLayout(self.widget_edit_section)
        self.edit_section_grid.setContentsMargins(0, 0, 0, 0)
        self.edit_section_grid.setObjectName("edit_section_grid")
        row = 0
        for item in data_list:
            label = QtWidgets.QLabel()
            label.setObjectName('test')
            label.setText(item)
            self.edit_section_grid.addWidget(label, row, 0, 1, 1)
            row = row + 1

class ProducentSection(AbstractSection):

    def __init__(self, BaseView, QWidget):
        self.BaseView = BaseView
        self.OBJ_QWidget = QWidget
        self.obj = BaseView.obj
        self.pagination = Pagination(self.obj)
        self.Form = Form(self.BaseView.obj)
        self.button_group_info = QtWidgets.QButtonGroup()
        self.Form.buttons_loop= [
            {'button': self.on_info_button, 'obejct': self.button_group_info },
        ]

    def on_info_button(self,id):
        self.Form.buttom_genarator(self.button_group_info , self.info_button, id)

    def info_button(self, item):
        self.BaseView.load_view('series', item)
        return True;

    def grid(self,left,top,page):
        grid = QtWidgets.QWidget(page)
        grid.setGeometry(QtCore.QRect(left, top, 0, 0))
        grid.setMinimumSize(QtCore.QSize(390, 200))
        grid.setMaximumSize(QtCore.QSize(380, 200))
        grid.setObjectName("gridLayoutWidget_15")
        return grid

    def seriesItem(self,grid):
        seriesItem = QtWidgets.QGridLayout(grid)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def title(self,grid,seriesItem,item,Obj):
        font=Obj['section']['font']
        strings_in_title=Obj['section']['strings_in_title']
        title = QtWidgets.QLabel(grid)
        title.setObjectName("seriesTitle")
        title.setText("<html><head/><body><span style=\" font-size:"+str(font)+" px; font-weight:600; \">" ""
                      + stringManipupations.short(item.name, strings_in_title) +
                      "</span></body></html>")
        seriesItem.addWidget(title, 0, 0, 1, 2)

    def more(self,item,left,top,page,Obj):
        button_with=Obj['section']['button_with']
        button_height = Obj['section']['button_height']
        button = QtWidgets.QPushButton(page)
        button.setObjectName("show-movies")
        button.setText('Show Movies')
        button.setGeometry(left+20,top+200, button_with, button_height)
        button.data = item
        self.Form.buttons_loop[0]['obejct'].addButton(button)
        self.Form.buttons_loop[0]['obejct'].buttonClicked[int].connect(self.Form.buttons_loop[0]['button'])

    def avatar(self,grid,seriesItem,item,Obj):
        avatar_with=Obj['section']['avatar_with']
        avatar_height = Obj['section']['avatar_height']
        seriesAvatar = QtWidgets.QLabel(grid)
        seriesAvatar.setMaximumSize(QtCore.QSize(avatar_with, avatar_height))
        seriesAvatar.setText("")
        seriesAvatar.setPixmap(QtGui.QPixmap(item.avatar))
        seriesAvatar.setScaledContents(True)
        seriesAvatar.setObjectName("seriesAvatar")
        seriesItem.addWidget(seriesAvatar, 1, 0, 5, 1)

    def run(self,data,data_list,page):
        self.tabWidget = self.pagination.tabs([data[0], data[1], data[2], data[3]])
        self.page = self.pagination.tab()
        left = self.OBJ_QWidget.WindowSize['section']['left']
        top = self.OBJ_QWidget.WindowSize['section']['top']
        el = 0;
        pages = []
        pages.append(self.page)
        self.add_page = self.page
        tab_name = 1

        for item in data_list:
            el = el + 1;
            grid = self.grid(left, top, self.add_page)
            seriesItem = self.seriesItem(grid)
            self.title(grid, seriesItem, item,self.OBJ_QWidget.WindowSize)
            self.avatar(grid, seriesItem, item,self.OBJ_QWidget.WindowSize)
            self.more(item, left, top, self.add_page,self.OBJ_QWidget.WindowSize)
            left = left + self.OBJ_QWidget.WindowSize['section']['left_add']

            if el % self.OBJ_QWidget.WindowSize['section']['per_row'] == 0:
                left = self.OBJ_QWidget.WindowSize['section']['left']
                top = top + self.OBJ_QWidget.WindowSize['section']['top_add']

            if el % self.OBJ_QWidget.WindowSize['section']['per_page'] == 0:
                self.next_page = self.pagination.tab()
                self.add_page = self.next_page
                pages.append(self.next_page)
                top = 0

        for page_tap in pages:
            self.tabWidget.addTab(page_tap, str(tab_name))
            tab_name = tab_name + 1

class EditGalerySection(AbstractSection):

    def __init__(self, BaseView, QWidget):
        self.BaseView = BaseView
        self.OBJ_QWidget = QWidget
        self.obj = BaseView.obj
        self.remove_buttons = QtWidgets.QButtonGroup()
        self.skip_buttons = QtWidgets.QButtonGroup()
        self.replece_buttons = QtWidgets.QButtonGroup()
        self.Form = Form(self.BaseView.obj)
        self.Form.buttons_loop= [
            {'button': self.on_remove_button, 'obejct': self.remove_buttons},
            {'button': self.on_marks_as_skip, 'obejct': self.skip_buttons}
        ]

    def on_remove_button(self, id):
        self.Form.buttom_genarator(self.remove_buttons, self.info_button, id)

    def on_marks_as_skip(self, id):
        self.Form.buttom_genarator(self.skip_buttons, self.marks_as_skip, id)

    def info_button(self,photo):
        os.remove(self.galery_url+'/'+photo)
        self.obj.BaseActions.reset()

    def marks_as_skip(self,photo):
        def update():
            os.remove(galery)
            string=str(galery_skip).replace("'",'"')
            f = open(galery, "x")
            f.write(""+str(string)+"\n")
            f.close()

        galery = self.BaseView.data.dir + '\\skip_galery.JSON'
        if self.galery_action_name(photo) is False:
            with open(galery) as sg:
                json_pars = json.load(sg)
                galery_skip=json_pars
            galery_skip.append(photo)
        else:
            with open(galery) as sg:
                json_pars = json.load(sg)
                galery_skip = json_pars
                for item in galery_skip:
                    if item == photo:
                        galery_skip.remove(item)
        update()
        self.obj.BaseActions.reset()

    def galery_action_name(self,photo):
        galery=self.BaseView.data.dir+'\\skip_galery.JSON'
        with open(galery) as sg:
            json_pars = json.load(sg)
            if photo in json_pars:
                return True
        return False

    def return_show(self,photo):
        show = 'Do not show in galery'
        if self.galery_action_name(photo):
            show = 'Show in galery'
        return show

    def set_run(self,data,data_list):
        self.galery_url=data_list;
        self.galery_loop = os.listdir(data_list)
        self.widget_edit_section = QtWidgets.QWidget(self.obj)
        self.widget_edit_section.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.edit_section_grid = QtWidgets.QGridLayout(self.widget_edit_section)

    def run(self,data,data_list,page):
        self.set_run(data,data_list)
        row = 0
        col = 0
        for photo in self.galery_loop:
            if photo.endswith(photo_ext):
                self.Form.photo([row, col, 1, 1],self.edit_section_grid,data_list + '/' + photo,[150,150],self.obj)
                self.Form.label(['', photo], [row, col+1, 1, 1], self.edit_section_grid, self.obj)
                self.Form.button_loop(self.obj, self.edit_section_grid, photo, [row, col+2, 1, 1], ['remove'], 0,[50,50])
                self.Form.button_loop(self.obj, self.edit_section_grid, photo, [row, col + 3, 1, 1], [self.return_show(photo)], 1,[50,50])
                col=0
                row = row + 1

class EditGaleryMoviesSection(EditGalerySection):

    def __init__(self, BaseView, QWidget):
        super().__init__(BaseView, QWidget)
        self.Form.buttons_loop.append({'button': self.replece_buttons_generator, 'obejct': self.replece_buttons})

    def replece_buttons_generator(self, id):
        self.Form.buttom_genarator(self.replece_buttons, self.replece, id)

    def replece(self,photo):
        PM=PhotoMeaker(self.BaseView.data,data_JSON['movies_photos'],self.obj)
        PM.replace(photo)
        self.obj.BaseActions.reset()

    def run(self,data,data_list,page):
        self.set_run(data,data_list)
        row = 0
        col = 0
        for photo in self.galery_loop:
            if photo.endswith(photo_ext):
                self.Form.photo([row, col, 1, 1],self.edit_section_grid,data_list + '/' + photo,[150,150],self.obj)
                self.Form.label(['', photo], [row, col+1, 1, 1], self.edit_section_grid, self.obj)
                self.Form.button_loop(self.obj, self.edit_section_grid, photo, [row, col+2, 1, 1],
                                      ['remove'], 0,[50,50])
                self.Form.button_loop(self.obj, self.edit_section_grid, photo, [row, col + 3, 1, 1],
                                      [self.return_show(photo)], 1,[50,50])
                self.Form.button_loop(self.obj, self.edit_section_grid, photo, [row, col + 4, 1, 1],
                                      ['replace'], 2, [50, 50])
                col=0
                row = row + 1

class TagsListSection(AbstractSection):

    def __init__(self, BaseView, QWidget):
        self.BaseView = BaseView
        self.OBJ_QWidget  =QWidget
        self.obj = BaseView.obj
        self.Form = Form(self.BaseView.obj)
        self.buttons = QtWidgets.QButtonGroup()
        self.Form.buttons_loop= [
            {'button': self.on_info_button, 'obejct': self.buttons},
        ]

    def on_info_button(self,id):
        self.Form.buttom_genarator(self.buttons, self.info_button, id)

    def info_button(self,item):
        self.obj.delete(item)

    def run(self, data, data_list, page):
        self.widget_edit_section = QtWidgets.QWidget(self.obj)
        self.widget_edit_section.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.widget_edit_section.setObjectName("widget_edit_section")
        self.edit_section_grid = QtWidgets.QGridLayout(self.widget_edit_section)
        self.edit_section_grid.setContentsMargins(0, 0, 0, 0)
        self.edit_section_grid.setObjectName("edit_section_grid")
        row=0
        for item in data_list:

            label = QtWidgets.QLabel()
            label.setObjectName('test')
            if hasattr(item,'name'):
                label.setText(item.name)
            else:
                label.setText(item)
            self.edit_section_grid.addWidget(label, row, 0, 1, 1)

            button = QtWidgets.QPushButton(self.obj)
            button.setObjectName('obj_name')
            button.setText('Remowe')
            button.data=item

            self.edit_section_grid.addWidget(button, row, 2, 1, 1)

            self.Form.buttons_loop[0]['obejct'].addButton(button)
            self.Form.buttons_loop[0]['obejct'].buttonClicked[int].connect(self.Form.buttons_loop[0]['button'])

            row=row+1

class StarsSection(AbstractSection):

    def __init__(self, BaseView,QWidget):
        self.BaseView = BaseView
        self.OBJ_QWidget  =QWidget
        self.obj =BaseView.obj
        self.Scroller = Scroller(self.obj)
        self.List= List(self.BaseView,25)
        self.pagination = Pagination(self.obj)
        self.button_group_info = QtWidgets.QButtonGroup()
        self.Form = Form(self.BaseView.obj)
        self.Form.buttons_loop= [
            {'button': self.on_info_button, 'obejct': self.button_group_info },
        ]

    def on_info_button(self,id):
        self.Form.buttom_genarator(self.button_group_info , self.info_button, id)

    def info_button(self,data):
        self.BaseView.load_view('movie_list',self.BaseView.data,data)
        return True;

    def more(self,item,left,top,page,Obj):
        button_with=Obj['section']['button_with']
        button_height = Obj['section']['button_height']
        button = QtWidgets.QPushButton(page)
        button.setObjectName("show-movies")
        button.setText('Show Movies')
        button.setGeometry(left+20,top+200, button_with, button_height)
        button.data = item
        self.Form.buttons_loop[0]['obejct'].addButton(button)
        self.Form.buttons_loop[0]['obejct'].buttonClicked[int].connect(self.Form.buttons_loop[0]['button'])

    def avatar(self,grid,seriesItem,item,Obj):
        avatar_with=Obj['section']['avatar_with']
        avatar_height = Obj['section']['avatar_height']
        seriesAvatar = QtWidgets.QLabel(grid)
        seriesAvatar.setMaximumSize(QtCore.QSize(avatar_with, avatar_height))
        seriesAvatar.setText("")
        seriesAvatar.setPixmap(QtGui.QPixmap(item['avatar']))
        seriesAvatar.setScaledContents(True)
        seriesAvatar.setObjectName("seriesAvatar")
        seriesItem.addWidget(seriesAvatar, 1, 0, 5, 1)

    def seriesItem(self,grid):
        seriesItem = QtWidgets.QGridLayout(grid)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def grid(self,left,top,page):
        grid = QtWidgets.QWidget(page)
        grid.setGeometry(QtCore.QRect(left, top, 0, 0))
        grid.setMinimumSize(QtCore.QSize(390, 200))
        grid.setMaximumSize(QtCore.QSize(380, 200))
        grid.setObjectName("gridLayoutWidget_15")
        return grid

    def title(self,grid,seriesItem,item,Obj):
        font=Obj['section']['font']
        strings_in_title=Obj['section']['strings_in_title']
        title = QtWidgets.QLabel(grid)
        title.setObjectName("seriesTitle")
        title.setText("<html><head/><body><span style=\" font-size:"+str(font)+" px; font-weight:600; \">" ""
                      + stringManipupations.short(item['name'], strings_in_title) +
                      "</span></body></html>")
        seriesItem.addWidget(title, 0, 0, 1, 2)

    def show_empty_movies(self,data):
        empty_movies = QtWidgets.QLabel(self.obj)
        empty_movies.setObjectName("empty_movies")
        empty_movies.setText("<html><head/><body><span style=\" font-size:25pt; font-weight:1000; \">"
                      "No Movies found !"
                      "</span></body></html>")
        empty_movies.setGeometry(data[0]+350, data[1]-200, data[2], data[3])


    def run(self, data, data_list, page):
        if len(data_list)==0:
            self.show_empty_movies(data)
        else:
            self.return_series_list(data,data_list)

    def return_series_list(self, data, data_list):
        self.tabWidget = self.pagination.tabs([data[0], data[1], data[2], data[3]])
        self.page = self.pagination.tab()
        left = self.OBJ_QWidget.WindowSize['section']['left']
        top = self.OBJ_QWidget.WindowSize['section']['top']
        el = 0;
        pages = []
        pages.append(self.page)
        self.add_page = self.page
        tab_name = 1

        for item in data_list:
            el = el + 1;

            grid = self.grid(left, top, self.add_page)
            seriesItem = self.seriesItem(grid)
            self.title(grid, seriesItem, item,self.OBJ_QWidget.WindowSize)
            self.avatar(grid, seriesItem, item,self.OBJ_QWidget.WindowSize)
            self.more(item, left, top, self.add_page,self.OBJ_QWidget.WindowSize)
            left = left + self.OBJ_QWidget.WindowSize['section']['left_add']

            if el % self.OBJ_QWidget.WindowSize['section']['per_row'] == 0:
                left = self.OBJ_QWidget.WindowSize['section']['left']
                top = top + self.OBJ_QWidget.WindowSize['section']['top_add']

            if el % self.OBJ_QWidget.WindowSize['section']['per_page'] == 0:
                self.next_page = self.pagination.tab()
                self.add_page = self.next_page
                pages.append(self.next_page)
                top = 0

        for page_tap in pages:
            self.tabWidget.addTab(page_tap, str(tab_name))
            tab_name = tab_name + 1

class SeriesSection(AbstractSection):

    per_page = 5

    def __init__(self, BaseView,QWidget):
        self.obj = BaseView.obj
        self.OBJ_QWidget = QWidget
        self.data= BaseView.data
        self.BaseView=BaseView
        self.List = List(self.BaseView, self.per_page)
        self.Scroller = Scroller(self.obj)
        self.Pagination = Pagination(self.obj)
        self.Section=SingleSectionInfo()

    def single_title(self,tab,item):
        title = QtWidgets.QLabel(tab)
        title.setObjectName("seriesTitle")
        title_name = ''
        for el in self.obj.data.sezons:
            if int(el.name) == item:
                title_name=el.sezon_name

        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:28pt;font-weight:800; " \
               "text-decoration: none;\">" + title_name+ \
               "</span></p></body></html>"

        title.setText(text)

        title.setGeometry(
            self.BaseView.obj.WindowSize['single_title'][0],
            self.BaseView.obj.WindowSize['single_title'][1],
            self.BaseView.obj.WindowSize['single_title'][2],
            self.BaseView.obj.WindowSize['single_title'][3]
        )

    def info(self,tab,info,item,single=False):
        data = self.BaseView.obj.WindowSize[info]
        rows = ['itemNmae', 'itemName2']
        if single:
            self.single_title(tab, item)
        self.Section.set_obj(self.obj.data,item)
        info_data=self.Section.return_data()
        self.BaseView.info(info_data,data,rows,tab)

    def seriesItem(self,grid):
        seriesItem = QtWidgets.QGridLayout(grid)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def click_play(self,movies):
        self.BaseView.load_view('play', movies[0])

    def click_info(self, movies):
        self.BaseView.load_view('info', movies[0])

    def show_movie_buttons(self,tab,movies):
        self.Form = Form(tab)
        info={
            "obj_name":'play',
            "disabled" : True,
            "name"    :'Play',
            "grid_data":self.BaseView.obj.WindowSize['single_play_button'],
            'click'   :self.click_play
        }
        self.Form.button(info,None,movies)
        info={
            "obj_name":'info',
            "name"    :'Info',
            "disabled": True,
            "grid_data":self.BaseView.obj.WindowSize['single_info_button'],
            'click'   :self.click_info
        }
        self.Form.button(info,None,movies)

    def run(self, data, data_list, page):
        pages = self.data.number_of_sezons
        self.tabWidget = self.Pagination.tabs([data[0], data[1], data[2], data[3]])
        for item in range(1, pages + 1):
            movies = self.faind_movies_with_sezon(data_list, item)
            tab = self.Pagination.tab()
            src = self.set_src(item)
            if len(movies)>1:
                self.BaseView.avatar(self.BaseView.obj.WindowSize['section_avatar'], tab, src)
                self.info(tab,'section_info',item)
                self.Scroller.run(self.BaseView.obj.WindowSize['section_scroller'], tab)
                self.Scroller.movie_list(
                    movies,
                    self,
                    'movies'
                )
                self.tabWidget.addTab(tab, str(item))
            else:
                self.BaseView.avatar(self.BaseView.obj.WindowSize['section_avatar_single_movie'], tab, src)
                self.info(tab, 'section_info_single_info', item, True)
                self.show_movie_buttons(tab, movies)
                self.tabWidget.addTab(tab, str(item))
        return self.tabWidget

    def set_src(self,item):
        for item_in_sezon in self.obj.data.sezons:
            if item_in_sezon.name == str(item):
                return item_in_sezon.src
        return series_avatar_defult


    def faind_movies_with_sezon(self,arry,page):
        movies_in_sezon=[]
        for movie in arry:
            if movie.sezon == page:
                movies_in_sezon.append(movie)
        return movies_in_sezon

class MovieListSection(AbstractSection):

    def __init__(self, BaseView,QWidget):
        self.obj = BaseView.obj
        self.OBJ_QWidget = QWidget
        self.BaseView = BaseView
        self.Scroller = Scroller(self.obj)
        self.List = List(self.BaseView)

    def run(self, data, data_list, page):
        self.Scroller.run([data[0], data[1], data[2], data[3]],self.obj)
        self.Scroller.movie_list(
            data_list,
            self,
            'movies'
        )

class MenuSection(AbstractSection):

    per_page=menu_per_page

    def __init__(self, BaseView,QWidget):

        self.obj = BaseView.obj
        self.OBJ_QWidget = QWidget
        self.BaseView = BaseView
        self.Scroller = Scroller(self.obj)
        self.List = List(self.BaseView,self.per_page)
        self.Pagination = Pagination(self.obj)

    def scroll_area_widget_contents(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.obj)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

    def grid_for_scroll(self):
        self.grid_for_scroll_obj = QtWidgets.QGridLayout(self.obj)
        self.grid_for_scroll_obj.setObjectName("gridLayout")

    def grid(self,tab):
        seriesItem = QtWidgets.QGridLayout(tab)
        seriesItem.setObjectName("seriesItem")
        return seriesItem

    def run(self, data, data_list,page):
        start = self.return_start_page(page)
        end = self.return_end_page(start,page)
        self.Scroller.run([data[0], data[1], data[2], data[3]], self.obj)
        self.Scroller.movie_list(
            data_list[start:end],
            self,
            self.obj.search_in
        )

    def return_start_page(self,page):
        if page<0:
            return 0
        else:
            return page*menu_per_page

    def return_end_page(self,start,page):
        if page>0:
            return start+self.per_page;
        return self.per_page
