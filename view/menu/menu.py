from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget,QMainWindow,qApp,QAction
from PyQt5.QtGui import QIcon
from app.forms import MenuFormSchena,MenuPaginationForm
from core.search import SetFactory
from core.setings import search_in_defult,search_faze_defult,menu_per_page
from core.helper import QueryCounter
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
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('ESC')
        exitAct.setStatusTip('Exit application')

        jsonConfig = QAction(QIcon('exit.png'), '&Exit', self)
        jsonConfig.setShortcut('Ctrl+C')
        jsonConfig.setStatusTip('Json')
        jsonConfig.triggered.connect(self.json_config)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&JSON')
        fileMenu.addAction(jsonConfig)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        exitAct.triggered.connect(qApp.quit)

    def json_config(self):
        self.BaseView.load_view('JSONCONFIG')

    def resizeEvent(self, event):
        self.set_resolution()

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