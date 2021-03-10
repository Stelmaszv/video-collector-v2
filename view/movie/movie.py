from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies
from core.view import AbstractBaseView

class MovieView(QWidget,AbstractBaseView):
    show_elemnts = ['Tags','Description','Title','Info','Galery','Nav','List','Avatar']
    resolution_index='Movie'


