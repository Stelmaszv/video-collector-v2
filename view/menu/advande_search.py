from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import AdvanceSearchForm
class AdvanceSearch(QWidget,AbstractBaseView):
    FormSchema = AdvanceSearchForm
    model_view_off = True
    show_elemnts = ['Title', 'Info', 'Galery', 'Nav', 'Avatar','List']
    resolution_index = 'advande_search'
    window_title = 'Advance Search'
    reset_view = 'advance_search'
    methods = ['submit_click','add_tag','add_star']
    tags= []
    stars= []
    criterions = {'Tags':[],'Stars':[]}

    def add_star(self,values):
        self.close()
        from view.star.add_star_to_model_no_save import AddStarToModelNoSave
        A = AddStarToModelNoSave()
        A.criterions = self.criterions
        A.run_window()

    def add_tag(self,values):
        self.close()
        from view.tags.add_tag_to_model_no_save import AddTagToModelNoSave
        A=AddTagToModelNoSave()
        A.criterions=self.criterions
        A.run_window()

    def set_up(self):
        self.custom_title('Tags','tags_name')
        self.custom_list(self.criterions['Tags'],'tags','Custom_list')
        self.custom_title('Stars', 'star_name')
        self.custom_list(self.criterions['Stars'],'stars','Custom_list')

    def submit_click(self,values):
        print(values)

