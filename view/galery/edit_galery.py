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

class EditGaleryMovieView(EditGaleryView):
    show_elemnts = ['Info', 'Galery', 'Avatar', 'Description', 'Tags']
    reset_view = 'edit_galery_movie_view'
    list_view    = 'EditGalery'
    resolution_index = 'EditMovieGalery'
    Nav          = MovieGaleryNav

    def remove_all_photos_create_new(self,values):
        print('ok')

    def create_missing_photos(self,values):
        print('ok')

