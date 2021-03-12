from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from core.view import AbstractBaseView
from app.forms import MovieEditForm
from app.model_view import StarModelView

class EditMovieView(QWidget,AbstractBaseView):
    model = Movies
    resolution_index = 'EditSeries'
    submit_view = 'movies'
    FormSchema = MovieEditForm
    ModelView = StarModelView
    show_elemnts = ['Info', 'Galery', 'Nav', 'Avatar','List','Description','Tags']
    methods = ['add_star','add_tag', 'submit_click']

    def add_tag(self,values):
        self.BaseView.load_view('add_tags', self.data)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

    def add_star(self,values):
        self.BaseView.load_view('movie_add_star_to_model_view', self.data)