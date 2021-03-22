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
        self.galery_for_stars()
        self.title_for_stars()
        self.custum_galery=self.set_dir()

    def set_dir(self):
        if len(self.data.series):
            dir=data_JSON['movies_photos']+'\\series\\'+self.data.series[0].name
            dir=dir+'\\'+str(self.data.sezon)+'\\'+self.data.name
        else:
            dir=data_JSON['movies_photos']+'\\movies\\'+self.data.name
            print(dir)
        return dir

    def galery_for_stars(self):
        def stars_array():
            stars=[]
            for star in self.data.stars:
                stars.append(star.avatar)
            return stars
        self.BaseView.galery_from_array([850,0,400,400],[150,150],2,stars_array())

    def title_for_stars(self):
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: none;\">Stars</span></p></body></html>"
        self.BaseView.title([750, 35, 580, 100],text)




