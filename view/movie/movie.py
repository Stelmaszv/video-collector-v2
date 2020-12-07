from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies

class MovieView(QWidget):

    def __init__(self):
        super().__init__()
        self.window_title = 'PyQt5 button - pythonspot.com'
        self.model = Movies
        self.BaseView= BaseView([], self)


    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)


    def initUI(self):
        self.title()
        self.BaseView.get_nav([850, -100, 400, 400], [self.open_movie, self.add_favorits, self.show_edit, self.delete])
        self.window_title=self.data.name

    def open_movie(self):
        self.BaseView.load_view('play', self)

    def add_favorits(self):
        print('faforits')

    def show_edit(self):
        print('show edit')

    def delete(self):
        print('delete')

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()
