from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.db.models import Producent

class ProducentView(QWidget,AbstractBaseView):
    model = Producent
    show_elemnts = ['Tags', 'List','Info','Galery','Nav','Avatar','Description']
    resolution_index = 'Producent'
