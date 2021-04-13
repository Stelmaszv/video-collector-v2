from PyQt5.QtWidgets import QWidget
from core.view import AbstractBaseView
from app.db.models import Series,Movies
from app.nav import SeriesNav
from app.info import InfoSection
from app.db.models import session
from sqlalchemy import desc


class SerieView(QWidget,AbstractBaseView):

    Info               =  InfoSection
    Nav                =  SeriesNav
    model              =  Series
    reset_view         = 'series'
    edit_view          = 'edit_series'
    resolution_index   = 'Series'
    list_view          = 'Series'
    show_elemnts      =   ['Tags']

    def  set_up(self):
        def return_Movies_in_series():
            return session.query(Movies)\
                .filter(Movies.series.any(Series.id.in_(("",self.data.id))))\
                .order_by(desc('year'))\
                .all()
        print(return_Movies_in_series())
        self.set_list_view_data(return_Movies_in_series())



