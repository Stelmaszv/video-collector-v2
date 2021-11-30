from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.model_view import ConfigAddDataModel

class ConfigScan(QWidget, AbstractBaseView):
    ModelView = ConfigAddDataModel
    window_title = 'Config Scan'
    resolution_index = 'VCSCAN'
    show_elemnts = ['Title', 'Galery', 'Nav', 'Avatar', 'List', 'Form','Info']