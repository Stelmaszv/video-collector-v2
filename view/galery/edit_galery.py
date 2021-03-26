from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from core.view import AbstractBaseView
from app.nav import MovieGaleryNav
class EditGaleryView(QWidget,AbstractBaseView):
    show_elemnts = ['Info', 'Galery', 'Avatar', 'List', 'Description', 'Tags']
    resolution_index = 'EditGalery'
    Nav = MovieGaleryNav
    model = Movies

    def set_up(self):
        self.window_title='Editing galery for '+str(self.data.name)