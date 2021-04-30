from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.db.models import Producent
from app.nav import NavPoducent
from app.info import PrducentInfo

class ProducentView(QWidget,AbstractBaseView):
    model            = Producent
    Nav              = NavPoducent
    Info             = PrducentInfo
    show_elemnts     = ['Tags', 'List']
    resolution_index = 'Producent'
    reset_view       = 'producent'
