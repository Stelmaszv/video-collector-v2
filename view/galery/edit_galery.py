from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from core.view import AbstractBaseView
from app.nav import MovieGaleryNav
class EditGaleryView(QWidget,AbstractBaseView):
    show_elemnts = ['Info', 'Galery', 'Avatar', 'Description', 'Tags','Nav']
    resolution_index = 'EditGalery'
    model = Movies
    list_view   = 'EditGalery'
    reset_view  = 'edit_galery'

    def set_up(self):
        self.window_title='Editing galery for '+str(self.data.name)
        self.set_list_view_data(self.data.dir)