from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from core.view import AbstractBaseView
from app.info import InfoForMovie
from app.nav import MovieNav

class MovieView(QWidget,AbstractBaseView):
    model = Movies
    show_elemnts = ['Tags','List']
    resolution_index='Movie'
    Info = InfoForMovie
    Nav  = MovieNav
    reset_view = 'movies'
    edit_view = 'edit_movie'

    def set_galery(self):
        self.custum_galery=self.data.dir





