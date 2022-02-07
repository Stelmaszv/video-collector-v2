from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMainWindow, QWidget, qApp

from app.forms import MenuFormSchena, MenuPaginationForm
from core.helper import QueryCounter
from core.search import SetFactory
from core.setings import menu_per_page, search_faze_defult, search_in_defult
from core.view import AbstractBaseView

from .AdvanceSearchCriteria import AdvanceSearchCriteria


class Menu(QMainWindow,QWidget,AbstractBaseView):

    FormSchema                 =  MenuFormSchena
    resolution_index           = 'Menu'
    window_title               = 'Manu'
    list_view                  = 'Menu'
    list_model_off             = True
    model_view_off             = True
    AdvandeSearchCriteria      = AdvanceSearchCriteria()
    reset_view                 = 'menu'
    show_elemnts               = ['Title','Info','Galery','Nav','Avatar']
    search_in                  = search_in_defult
    search_faze                = search_faze_defult
    page = 0

    def __init__(self,page=0):
        super().__init__()
        self.page=page

        jsonConfig = QAction(QIcon('exit.png'), '&Change Json File', self)
        jsonConfig.setStatusTip('Change Json File')
        jsonConfig.triggered.connect(self.json_config)

        raportConfig = QAction(QIcon('exit.png'), '&Raport', self)
        raportConfig.setStatusTip('Raport')
        raportConfig.triggered.connect(self.raport)

        scanformovies = QAction(QIcon('exit.png'), '&Scan for Movies', self)
        scanformovies.setStatusTip('Scan for Movies')
        scanformovies.triggered.connect(self.load_movie_scan)

        scanforconfig = QAction(QIcon('exit.png'), '&Scan for config', self)
        scanforconfig.setStatusTip('Scan for config')
        scanforconfig.triggered.connect(self.load_config)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Actions')
        fileMenu.addAction(jsonConfig)
        fileMenu.addAction(raportConfig)
        VCSCAN = menubar.addMenu('&VCSCAN')
        VCSCAN.addAction(scanformovies)
        VCSCAN.addAction(scanforconfig)
        VCSCAN.addAction(scanforconfig)


    def json_config(self):
        self.BaseView.load_view('JSONCONFIG')

    def load_config(self):
        self.BaseView.load_view('ConfigScan')

    def raport(self):
        self.BaseView.load_view('raport')

    def load_movie_scan(self):
        self.BaseView.load_view('MovieScanInfo')


    def resizeEvent(self, event):
        self.SetResolution.return_abstrat_view()

    def  set_up(self):
        factory = SetFactory(self)
        self.list = factory.get_factory(self.search_in)
        self.set_list_view_data(self.list)
        self.QC = QueryCounter(self.list, menu_per_page)
        self.previous=self.QC.if_previous_page_exist(self.page)
        self.next=self.QC.if_page_exist(self.page)
        self.cunter=self.QC.counter
        self.custum_form(MenuPaginationForm,'pagination_form')

    def previous_page(self,value):
        self.close()
        M=Menu(self.page-1)
        M.search_in =self.search_in
        M.run_window()

    def next_page(self, value):
        self.close()
        M=Menu(self.page+1)
        M.search_in = self.search_in
        M.run_window()

    def set_search(self,values):
        self.close()
        self.search_faze = values[0]['value']
        self.search_in   = values[1]['value']
        self.run_window()

    def submit_click(self,values):
        self.close()
        self.set_search(values)

    def advance(self,advance):
        from .advande_search import AdvanceSearch

        #self.BaseView.load_view('advance_search')
        self.run_window()
        AS=AdvanceSearch()
        AS.Menu=self
        AS.run_window()

    def reset(self,value):
        self.close()
        M = Menu(self.page)
        M.search_in = self.search_in
        M.run_window()