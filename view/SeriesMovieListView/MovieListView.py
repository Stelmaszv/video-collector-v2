from PyQt5.QtWidgets import QWidget

from app.db.models import Stars
from app.info import MovisWithStar
from core.view import AbstractBaseView


class MovieListView(QWidget, AbstractBaseView):
    resolution_index   = 'MovieListView'
    show_elemnts       = ['Tags','Description','Galery','Nav']
    reset_view         = 'movie_list'
    edit_view          = 'edit_star'
    Info               = MovisWithStar
    model              = Stars
    list_view          = 'Movie_List'
    show_list          = 'full'

    def  set_up(self):
        self.set_list_view_data(self.list['movies'])
