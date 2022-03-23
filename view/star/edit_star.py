from PyQt5.QtWidgets import QWidget

from app.db.models import Stars
from app.forms import StarsForm
from app.model_view import StarModelView
from core.view import AbstractBaseView


class EditStarView(QWidget,AbstractBaseView):
    model = Stars
    resolution_index = 'EditSeries'
    submit_view = 'stars'
    FormSchema = StarsForm
    ModelView = StarModelView
    show_elemnts = ['Info', 'Galery', 'Nav', 'Avatar','List','Description','Tags']

    def add_tag(self,values):
        self.BaseView.load_view('stars_add_tag_view', self.data)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

