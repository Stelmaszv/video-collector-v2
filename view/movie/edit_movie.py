from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from core.view import AbstractBaseView
from app.forms import MovieEditForm
from app.model_view import MoviesModelView

class EditMovieView(QWidget,AbstractBaseView):
    model = Movies
    resolution_index = 'EditSeries'
    submit_view = 'movies-config'
    FormSchema = MovieEditForm
    ModelView = MoviesModelView
    show_elemnts = ['Info', 'Galery', 'Nav', 'Avatar','List','Description','Tags']
    methods = ['add_star','add_tag', 'submit_click']

    def add_tag(self,values):
        self.BaseView.load_view('movies_add_tag_view', self.data)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

    def edit_galery(self,value):
        self.BaseView.load_view('edit_galery_movie_view', self.data)

    def add_star(self,values):
        self.BaseView.load_view('movie_add_star_to_model_view', self.data)