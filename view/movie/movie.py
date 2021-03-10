from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies
from core.view import AbstractBaseView
from app.info import InfoForMovie
from app.nav import MovieNav
from core.setings import data_JSON

class MovieView(QWidget,AbstractBaseView):
    model = Movies
    show_elemnts = ['Tags','Description','List']
    resolution_index='Movie'
    Info = InfoForMovie
    Nav  = MovieNav
    reset_view = 'movies'
    edit_view = 'edit_star'

    def set_galery(self):
        self.custum_galery=str(data_JSON['movies_photos'])+'\\'+str(self.data.id)


