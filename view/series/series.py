from PyQt5.QtWidgets import QWidget

from app.db.models import Movies, Series, session
from app.info import InfoSection
from app.nav import SeriesNav
from core.view import AbstractBaseView


class SerieView(QWidget,AbstractBaseView):

    Info               =  InfoSection
    Nav                =  SeriesNav
    model              =  Series
    reset_view         = 'series'
    edit_view          = 'edit_series'
    resolution_index   = 'Series'
    list_view          = 'Series'
    show_list          = 'normal'
    show_elemnts      =   ['Tags']

    def  set_up(self):
        self.set_list_view_data(session.query(Movies).all())



