from PyQt5.QtWidgets import QWidget

from app.db.models import Movies, Series
from app.forms import AddStarToModelForm
from core.BaseActions import AddStar
from core.view import AbstractBaseView


class BaseAddStarToModelView(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add star'
    show_elemnts = ['Info','Galery','Nav','Avatar','Tags','Description']
    model_view_off = True
    FormSchema   = AddStarToModelForm
    list_view = 'Tags'
    methods = ['submit_click']
    reset_view = 'movie_add_star_to_model_view'

    def  set_up(self):
        self.model=self.obj.model
        self.BaseView.set_data(self.id)
        self.set_list_view_data(self.data.stars)

    def set_data_on_init(self):
        self.model=self.obj.model

    def submit_click(self,values):
        AT = AddStar(values, self)
        AT.add()
        self.BaseActions.reset()

    def delete(self,Star):
        AT = AddStar([], self)
        AT.remove(Star)
        self.BaseActions.reset()
        return True

class MovieAddStarToModelView(BaseAddStarToModelView):
    model = Movies
    reset_view = 'movie_add_star_to_model_view'

class SeriesAddStarToModelView(BaseAddStarToModelView):
    model = Series
    reset_view = 'series_add_star_to_model_view'