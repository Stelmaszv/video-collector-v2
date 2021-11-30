from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.model_view import ConfigAddDataModel
from app.info import MovieScanInfoSection


class MovieScanInfo(QWidget, AbstractBaseView):
    ModelView = ConfigAddDataModel
    Info = MovieScanInfoSection
    window_title = 'Found Items to add!'
    resolution_index = 'VCSCAN'
    show_elemnts = ['Title', 'Galery', 'Nav', 'Avatar', 'List', 'Form']
