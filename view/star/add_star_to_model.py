from PyQt5.QtWidgets import QWidget
from core.view import AbstractBaseView
from core.BaseActions import AddStar
from app.forms import AddStarToModelForm
from app.db.models import Series,Movies

class BaseAddStarToModelView(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add star'
    show_elemnts = ['Info','Galery','Nav','Avatar','Tags','Description']
    model_view_off = True
    FormSchema   = AddStarToModelForm
    list_view = 'Tags'
    methods = ['submit_click']
    reset_view = 'movies'

    def  set_up(self):
        self.model=self.obj.model
        self.BaseView.set_data(self.id)
        self.set_list_view_data(self.data.stars)

    def set_data_on_init(self):
        self.model=self.obj.model

    def submit_click(self,values):
        AT = AddStar(values, self)
        AT.add()

    def delete(self,Star):
        AT = AddStar([], self)
        AT.remove(Star)
        self.BaseActions.reset()
        return True

class MovieAddStarToModelView(BaseAddStarToModelView):
    model = Movies
    reset_view = 'movies'

class SeriesAddStarToModelView(BaseAddStarToModelView):
    model = Series
    reset_view = 'series_add_star_to_model_view'