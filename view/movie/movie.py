from PyQt5.QtWidgets import QWidget

from app.db.models import Movies
from app.info import InfoForMovie
from app.nav import MovieNav
from core.view import AbstractBaseView


class MovieView(QWidget,AbstractBaseView):
    model = Movies
    show_elemnts = ['Tags','List']
    resolution_index='Movie'
    Info = InfoForMovie
    Nav  = MovieNav
    reset_view = 'movies'
    edit_view = 'edit_movie'

    def set_galery(self):
        self.custom_title('Stars', 'star_title')
        self.galery_from_array(self.data.stars, 'stars_galery', 'stars_galery_size', 'stars_row')
        self.custum_galery=self.data.dir