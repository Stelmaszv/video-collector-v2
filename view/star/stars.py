from PyQt5.QtWidgets import QWidget

from app.db.models import Stars
from app.info import StarInfoSection
from app.nav import StarNav
from core.creator import SeriesCreator
from core.view import AbstractBaseView


class StarView(QWidget,AbstractBaseView):
    model              =  Stars
    Nav                =  StarNav
    Info               =  StarInfoSection
    reset_view         = 'stars'
    edit_view          = 'edit_star'
    resolution_index   = 'Stars'
    list_view          = 'Stars'
    show_elemnts       = ['Tags']

    def  set_up(self):
        self.list = None
        self.list = SeriesCreator(self.data).return_obj()
        self.set_list_view_data(self.list)
