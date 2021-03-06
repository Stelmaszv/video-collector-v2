from PyQt5.QtWidgets import QAction,QMainWindow
from PyQt5.QtCore import pyqtSlot
from core.view import BaseView
from core.search import setFactory
from app.db.seaders import initSeader
from core.helper import QueryCounter
from core.rezolution import SetResolution

#initSeader().initNow()
class Menu(QMainWindow):
    deepSearch = False
    searchFaze = ''
    searchIn = 'stars'
    page=0

    def __init__(self,data=False):
        super().__init__()
        self.SetResolution=SetResolution()
        self.window_title = 'Menu'
        self.left = self.SetResolution.menu_set['Menu']['position']['left']
        self.top =self.SetResolution.menu_set['Menu']['position']['top']
        self.width = self.SetResolution.menu_set['Menu']['position']['width']
        self.height = self.SetResolution.menu_set['Menu']['position']['height']
        self.model=''
        self.BaseView=BaseView([], self)
        self.initUI(data)

    def search_box(self):
        data = [0, 150, 200, 50]
        list = ['stars','movies','series']
        self.search_in_combo_box=self.BaseView.Form.combo_box(data, list)
        data_search_button = [200,150,200,50]
        data_button_info=['serch003','search']
        self.BaseView.Form.button(data_button_info, data_search_button, self.click_search)
        data_line = [0,100,400,50]
        self.search_button_edit_line=self.BaseView.Form.edit_line(data_line, 'search Faze')
        QC=QueryCounter(self.list,50)
        if QC.if_page_exist(self.page+1):
            next_page_button = [200, 1100, 200, 50]
            next_page_info = ['next_page', 'next']
            self.BaseView.Form.button(next_page_info, next_page_button, self.next_page)
        if QC.if_page_exist(self.page -1):
            previous_page_button = [0, 1100, 200, 50]
            previous_page_info = ['previous_pag', 'previous']
            self.BaseView.Form.button(previous_page_info, previous_page_button, self.previous_page)

    def previous_page(self):
        self.close()
        M=Menu
        M.page=self.page-1
        M([self.searchIn, self.searchFaze])

    def next_page(self):
        self.close()
        M = Menu
        M.page = self.page+1
        M([self.searchIn, self.searchFaze])

    def click_search(self):
        self.close()
        self.searchIn = self.search_in_combo_box.currentText()
        self.searchFaze = self.search_button_edit_line.text()
        Menu([self.searchIn,self.searchFaze])

    def title(self):
        data = [0, 0, 400 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">search</span></p></body></html>"
        self.BaseView.title(data, text)

    def list_view(self):
        data = [0, 200, 400, 900]
        self.BaseView.menu.searchIn=self.searchIn
        factory=setFactory(self)
        self.list = factory.getFactory(self.BaseView.menu.searchIn)
        self.BaseView.listView(data, self.list, 'Menu',self.page)

    def set_up(self,data):
        self.searchIn=data[0]
        self.searchFaze=data[1]

    def initUI(self,data=False):
        if data:
            self.set_up(data)
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.list_view()
        self.search_box()
        self.title()
        self.menu()
        self.show()

    def menu(self):
        menubar = self.menuBar()
        action_menu = menubar.addMenu('Add')
        new_movie_menu_item = QAction('new movie', self)
        new_movie_menu_item.triggered.connect(self.add_new_movie)
        new_menu_object = QAction('new menu', self)
        new_menu_object.triggered.connect(self.new_menu_object_button)
        action_menu.addAction(new_movie_menu_item)
        action_menu.addAction(new_menu_object)

    def new_menu_object_button(self):
        Menu([self.searchIn, self.searchFaze])

    def add_new_movie(self):
        self.BaseView.load_view('add_movie')
        self.close()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        print(self.BaseView)