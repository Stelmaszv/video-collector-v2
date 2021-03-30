import os
import random
from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
from core.view import AbstractBaseView
from app.nav import MovieGaleryNav
from core.setings import photo_ext,data_JSON
from app.db.models import session
from core.dir import PhotoMeaker

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
    list_view    = 'EditGaleryMovies'
    resolution_index = 'EditMovieGalery'
    Nav          = MovieGaleryNav
    procent_limt = 96
    array         = []

    def set_up(self):
        super().set_up()
        self.window_title='Editing galery for '+str(self.data.name)

    def remove_all_photos_create_new(self,values):
        for dir in os.listdir(self.data.dir):
            if dir.endswith(photo_ext):
                os.remove(self.data.dir+'\\'+dir)
        self.create_missing_photos(values)

    def create_missing_photos(self,values):
        Movie = session.query(Movies).filter(Movies.id == self.data.id).first()
        PM = PhotoMeaker(Movie, data_JSON['movies_photos'],self)
        PM.make()
        self.BaseActions.reset()
