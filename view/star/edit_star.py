from PyQt5.QtWidgets import QWidget
from app.db.models import Stars
from core.view import AbstractBaseView
from app.forms import StarsForm
from app.model_view import StarModelView

class EditStarView(QWidget,AbstractBaseView):
    model = Stars
    resolution_index = 'EditStars'
    submit_view = 'stars'
    FormSchema = StarsForm
    ModelView = StarModelView
    show_elemnts = ['Info', 'Galery', 'Nav', 'Avatar','List','Description','Tags']
    methods = ['add_tag', 'submit_click']

    def add_tag(self,values):
        self.BaseView.load_view('add_tags', self.data)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

