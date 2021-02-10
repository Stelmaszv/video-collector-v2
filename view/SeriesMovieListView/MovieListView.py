from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies
from core.rezolution import SetResolution

class MovieListView(QWidget):
    model = Movies

    def __init__(self):
        super().__init__()
        self.BaseView= BaseView([], self)
        self.SetResolution = SetResolution()
        self.left = self.SetResolution.menu_set['MovieListView']['position']['left']
        self.top = self.SetResolution.menu_set['MovieListView']['position']['top']
        self.width = self.SetResolution.menu_set['MovieListView']['position']['width']
        self.height = self.SetResolution.menu_set['MovieListView']['position']['height']
        self.WindowSize = self.SetResolution.menu_set['MovieListView']['window']

    def title(self):
        data = [
            self.WindowSize['title_size'][0],
            self.WindowSize['title_size'][1],
            self.WindowSize['title_size'][2],
            self.WindowSize['title_size'][3]
        ]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: underline;\">" + self.title_var + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def set_window_title(self):
        self.window_title = self.title_var

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()

    def show_series(self):
        self.close()
        self.BaseView.load_view('series', self.data)

    def back_to_star(self):
        self.close()
        self.BaseView.load_view('stars', self.data['star'])

    def buttons(self):
        self.BaseView.button(
            [
                self.WindowSize['button_series'][0],
                self.WindowSize['button_series'][1],
                self.WindowSize['button_series'][2],
                self.WindowSize['button_series'][3]
            ],
            {
                'item_name' :'head to',
                'name': str(self.data['name']),
                'button':self.show_series
            }

        )
        self.BaseView.button(
            [
                self.WindowSize['button_star'][0],
                self.WindowSize['button_star'][1],
                self.WindowSize['button_star'][2],
                self.WindowSize['button_star'][3]
            ],
            {
                'item_name' :'head to',
                'name': str(self.data['star']),
                'button':self.back_to_star
            }

        )

    def initUI(self):
        self.title_var = str(self.data['name']) + " movies with " + str(self.data['star'])
        self.set_window_title()
        self.title()
        self.buttons()
        data=[
            self.WindowSize['avatar_size'][0],
            self.WindowSize['avatar_size'][1],
            self.WindowSize['avatar_size'][2],
            self.WindowSize['avatar_size'][3]
        ]
        self.BaseView.avatar(data,None,self.data['avatar'])
        data = [
            self.WindowSize['list_view_size'][0],
            self.WindowSize['list_view_size'][1],
            self.WindowSize['list_view_size'][2],
            self.WindowSize['list_view_size'][3]
        ]
        self.BaseView.listView(data,self.data['movies'], 'Movie_List')

    def run_window(self):
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.left, self.top, self.width, self.height)