from app.db.models import Stars
from core.view import BaseView,AbstractBaseView
from core.datamanipulation import Data
from core.creator import SeriesCreator
from PyQt5.QtWidgets import QWidget
from core.rezolution import SetResolution
from core.strings import stringManipupations
from core.BaseActions import ViewBaseAction
from app.nav import StarNav
from app.nav import SeriesNav
from app.info import StarInfoSection
from app.model_view import StarModelView

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
        self.list = []
        self.list = SeriesCreator(self.data).return_obj()
        self.set_list_view_data(self.list)
