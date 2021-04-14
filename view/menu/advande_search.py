from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import AdvanceSearchForm
from view.menu.menu import Menu
from  .add_tag_advance_search import AddTagAdvnaceSearchView,AddStarsAdvnaceSearchView
class AdvanceSearch(QWidget,AbstractBaseView):
    FormSchema = AdvanceSearchForm
    model_view_off = True
    show_elemnts = ['Title', 'Info', 'Galery', 'Nav', 'Avatar','List']
    resolution_index = 'advande_search'
    window_title = 'Advance Search'
    reset_view = 'advance_search'
    criterions = {'Tags':[],'Stars':[]}

    def add_star(self,values):
        self.close()
        ATASV = AddStarsAdvnaceSearchView()
        ATASV.data_array = self.criterions['Stars']
        ATASV.run_window()

    def add_tag(self,values):
        self.close()
        ATASV=AddTagAdvnaceSearchView()
        ATASV.data_array=self.criterions['Tags']
        ATASV.run_window()

    def set_up(self):
        self.custom_title('Tags','tags_name')
        self.custom_list(self.criterions['Tags'],'tags','Custom_list')
        self.custom_title('Stars', 'star_name')
        self.custom_list(self.criterions['Stars'],'stars','Custom_list')

    def submit_click(self,values):
        self.close()
        M = Menu(0)
        M.search_in = 'movies'
        M.AdvandeSearchCriteria.stars = tuple(self.criterions['Stars'])
        M.AdvandeSearchCriteria.tags=tuple(self.criterions['Tags'])
        M.run_window()

