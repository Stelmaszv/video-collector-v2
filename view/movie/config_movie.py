from app.db.models import Movies
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.info import RaportInfo

class ConfigMoviesView(QWidget, AbstractBaseView):
    model = Movies
    Info = RaportInfo
    resolution_index = 'ConfigMoviesView'
    show_elemnts = ['Galery', 'Nav', 'Avatar', 'List', 'Form','Tags','Description','Info']