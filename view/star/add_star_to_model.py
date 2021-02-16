from PyQt5.QtWidgets import QWidget
from core.view import BaseView,AbstractBaseView
from core.BaseActions import FormSection,AddStar,ViewBaseAction
from core.rezolution import SetResolution
from app.forms import AddStarToModelForm
from app.db.models import Series

class AddStarToModelView(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add tag'
    show_elemnts = ['Info','Galery','Nav','Avatar']
    model = Series
    reset_view = 'add_star_to_model'
    model_view_off = True
    FormSchema   = AddStarToModelForm
    list_view = 'Tags'
    methods = ['submit_click']

    def  set_up(self):
        self.model=self.obj.model
        self.set_list_view_data(self.data.stars)

    def submit_click(self,values):
        AT = AddStar(values, self)
        AT.add()

    def delete(self,star):
        AT=AddStar([],self)
        AT.remove_star(star)
        self.BaseActions.reset()
        return True