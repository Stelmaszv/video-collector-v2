from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import TagsForm
from app.db.models import Series
from view.menu.advande_search import AdvanceSearch
class AddTagToModelNoSave(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add tag for search criterion'
    show_elemnts = ['Info','Galery','Nav','Avatar','Description','Tags','List']
    FormSchema = TagsForm
    model_view_off = True
    methods = ['submit_click']
    criterions=['new data']

    def set_up(self):
        print(self.criterions)

    def submit_click(self, values):
        self.close()
        ATNS = AdvanceSearch()
        ATNS.criterions = ['new data']
        print(ATNS.criterions)
        ATNS.run_window()
