from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies

class AddMovieView(QWidget):

    def __init__(self):
        super().__init__()
        self.window_title = 'Add new Movie'
        self.model = Movies
        self.base_view = BaseView([], self)

    def run_window(self):
        self.initUI()
        self.setWindowTitle(self.window_title)
        self.show()

    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">Add new movie</span></p></body></html>"
        self.base_view.title(data,text)

    def form(self):
        data = [100, 150, 200, 50]
        list = ['normal']
        self.base_view.form.combo_box(data, list)
        data_line = [100,100,400,50]
        self.base_view.form.edit_line(data_line,'dir location')
        data_search_button = [300,150,200,50]
        data_button_info=['add_item','add']
        self.base_view.form.button(data_button_info,data_search_button,self.click_search)

    def click_search(self):
        print('add item')

    def initUI(self):
        self.title()
        self.form()

