from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.db.models import Movies
class LoadingView(QWidget,AbstractBaseView):
    show_elemnts = ['Info', 'Galery', 'Avatar', 'Description', 'Tags','Nav','List']
    resolution_index = 'Loading'
    list_view   = 'Custom_list'
    reset_view  = 'edit_galery'
    text=[]

    def set_up(self):
        self.window_title='Please Wait ...'
        print(self.text)
