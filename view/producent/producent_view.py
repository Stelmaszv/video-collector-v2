from PyQt5.QtWidgets import QWidget

from app.db.models import Producent
from app.info import PrducentInfo
from app.nav import NavPoducent
from core.view import AbstractBaseView


class ProducentView(QWidget,AbstractBaseView):
    model            = Producent
    Nav              = NavPoducent
    Info             = PrducentInfo
    list_view        = 'Producent'
    show_elemnts     = ['Tags']
    resolution_index = 'Producent'
    reset_view       = 'producent'

    def  set_up(self):
        self.set_list_view_data(self.data.series)
