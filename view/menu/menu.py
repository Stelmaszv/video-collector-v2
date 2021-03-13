from PyQt5.QtWidgets import QAction,QMainWindow
from core.view import BaseView
from app.db.seaders import initSeader
from core.helper import QueryCounter
from core.rezolution import SetResolution
from core.setings import data_JSON
from core.dir import LoadFilesFromJson
from app.forms import StarsForm
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import MenuFormSchena
from core.search import SetFactory
from core.setings import search_in_defult,search_faze_defult
class Menu(QWidget,AbstractBaseView):
    FormSchema         = MenuFormSchena
    resolution_index   = 'Menu'
    window_title       = 'Manu'
    list_view          = 'Menu'
    list_model_off     = True
    model_view_off     = True
    reset_view         = 'menu'
    show_elemnts       = ['Title','Info','Galery','Nav','Avatar']
    search_in           = search_in_defult
    search_faze         = search_faze_defult

    def  set_up(self):
        factory = SetFactory(self)
        self.list = factory.get_factory(self.search_in)
        self.set_list_view_data(self.list)

    def set_search(self,values):

        MenuObj = Menu()
        MenuObj.search_faze = values[0]['value']
        MenuObj.search_in   = values[1]['value']
        MenuObj.run_window()

    def submit_click(self,values):
        self.close()
        self.set_search(values)

    def advance(self,advance):
        self.BaseView.load_view('advance_search')

    def reset(self,value):
        self.BaseActions.reset()