from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies
from core.view import AbstractBaseView
from app.info import InfoForMovie
from app.nav import MovieNav
from core.setings import data_JSON

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
        self.galery_from_array(self.data.stars,'stars_galery','stars_galery_size','stars_row')
        self.custum_galery=self.set_dir()

    def set_dir(self):
        if len(self.data.series):
            dir=data_JSON['movies_photos']+'\\series\\'+self.data.series[0].name
            dir=dir+'\\'+str(self.data.sezon)+'\\'+self.data.name
        else:
            dir=data_JSON['movies_photos']+'\\movies\\'+self.data.name
        return dir





