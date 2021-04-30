from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.db.models import Producent
from app.nav import NavPoducent

class ProducentView(QWidget,AbstractBaseView):
    model            = Producent
    Nav              = NavPoducent
    show_elemnts     = ['Tags', 'List','Info','Description']
    resolution_index = 'Producent'
    reset_view       = 'producent'
