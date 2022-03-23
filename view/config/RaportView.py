from PyQt5.QtWidgets import QWidget

from app.info import RaportInfo
from app.model_view import ConfigAddDataModel
from core.view import AbstractBaseView


class RaportView(QWidget, AbstractBaseView):
    ModelView = ConfigAddDataModel
    Info = RaportInfo
    search_in = 'search_in'
    window_title = 'Collector Raport'
    resolution_index = 'Menu'
    show_elemnts = ['Title', 'Galery', 'Nav', 'Avatar', 'List', 'Form']
