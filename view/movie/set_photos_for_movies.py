from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from app.forms import SetPhotosForMoviesForm
from app.model_view import MoviesModelView
from core.view import AbstractBaseView

class SetPhotosForMovies(QWidget, AbstractBaseView):
    model = Movies
    resolution_index = 'set_photos_for_movies'
    reset_view = 'movies-config'
    FormSchema = SetPhotosForMoviesForm
    ModelView = MoviesModelView
    submit_view = 'movies-config'
    show_elemnts = ['Galery', 'Avatar', 'List', 'Form','Tags','Description','Info','Nav']
    methods = ['submit_click']

    def after_init(self):
        data = {
            'src':self.data.avatar,
            'res':self.WindowSize['avatar_custum']
        }
        self.BaseView.custum_avatar(data)
        data = {
            'src':self.data.poster,
            'res':self.WindowSize['poster']
        }
        self.BaseView.custum_avatar(data)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

