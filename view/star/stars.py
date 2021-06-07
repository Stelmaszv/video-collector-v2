from app.db.models import Stars
from core.view import AbstractBaseView
from core.creator import SeriesCreator
from PyQt5.QtWidgets import QWidget
from app.nav import StarNav
from app.info import StarInfoSection

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
