from PyQt5.QtWidgets import QWidget

from app.db.models import Series
from app.forms import SeriesForm
from app.model_view import SeriesModelView
from core.view import AbstractBaseView


class EditSeries(QWidget,AbstractBaseView):

    model              = Series
    ModelView          = SeriesModelView
    resolution_index   = 'EditSeries'
    show_elemnts       = ['Avatar','Info','Galery','Nav','List','Tags','Description']
    FormSchema        = SeriesForm
    submit_view       = 'series'

    def  set_up(self):
        self.window_title='Editing '+str(self.data.name)

    def add_star(self,values):
        self.BaseView.load_view('series_add_star_to_model_view', self.data)

    def set_photo_for_series(self,values):
        self.BaseView.load_view('set_photo_to_series', self.data)

    def add_tag(self,values):
        self.BaseView.load_view('series_add_tag_view', self.data)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()
