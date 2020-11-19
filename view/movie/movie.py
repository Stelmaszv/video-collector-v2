from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies
class Movie(QWidget):
    def __init__(self):
        super().__init__()
        self.window_title = 'PyQt5 button - pythonspot.com'
        self.model = Movies
        self.base_view= BaseView([],self)


    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.base_view.title(data,text)

    def run_window(self):
        self.base_view.set_data(self.id)
        self.data = self.base_view.data
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)

    def initUI(self):
        self.title()
        self.base_view.get_nav([850, -100, 400, 400])
        self.window_title=self.data.name

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()
