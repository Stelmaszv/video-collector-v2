from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from core.view import AbstractBaseView
class EditGaleryView(QWidget,AbstractBaseView):
    show_elemnts = ['Info', 'Galery', 'Nav', 'Avatar', 'List', 'Description', 'Tags']
    resolution_index = 'EditSeries'
    model = Movies

    def set_up(self):
        self.window_title='Editing galery for '+str(self.data.name)