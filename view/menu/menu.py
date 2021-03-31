from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import MenuFormSchena,MenuPaginationForm
from core.search import SetFactory
from core.setings import search_in_defult,search_faze_defult,menu_per_page
from core.helper import QueryCounter
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
    page = 0

    def __init__(self,page=0):
        super().__init__()
        self.page=page

    def  set_up(self):
        factory = SetFactory(self)
        self.list = factory.get_factory(self.search_in)
        self.set_list_view_data(self.list)
        QC = QueryCounter(self.list, menu_per_page)
        self.previous=QC.if_previous_page_exist(self.page)
        self.next=QC.if_page_exist(self.page)
        self.custum_form(MenuPaginationForm,'pagination_form')

    def previous_page(self,value):
        self.close()
        M=Menu(self.page-1)
        M.run_window()

    def next_page(self, value):
        self.close()
        M=Menu(self.page+1)
        M.run_window()

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