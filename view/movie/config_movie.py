from app.db.models import Movies
from app.forms import ConfigMoviesViewForm
from app.model_view import MoviesModelView
from app.nav import MovieConfigNav
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.info import RaportInfo

class ConfigMoviesView(QWidget, AbstractBaseView):
    model = Movies
    Info = RaportInfo
    resolution_index = 'ConfigMoviesView'
    ModelView = MoviesModelView
    Nav = MovieConfigNav
    FormSchema = ConfigMoviesViewForm
    reset_view = 'movies-config'
    edit_view = 'edit_movie'
    show_elemnts = ['Galery', 'Avatar', 'List', 'Form','Tags','Description','Info']
    methods = ['add_star', 'add_tag', 'submit_click']

    def add_tag(self,values):
        self.BaseView.load_view('movies_add_tag_view', self.data)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

    def edit_galery(self,value):
        self.BaseView.load_view('edit_galery_movie_view', self.data)

    def add_star(self,values):
        self.BaseView.load_view('movie_add_star_to_model_view', self.data)

    def base_edit(self, values):
        self.BaseView.load_view('edit_movie', self.data)