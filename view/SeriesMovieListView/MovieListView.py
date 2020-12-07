from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from app.db.models import Movies

class MovieListView(QWidget):
    model = Movies

    def __init__(self):
        super().__init__()
        self.BaseView= BaseView([], self)
        self.left = 2562+400
        self.top =400
        self.width = 1280
        self.height = 985

    def title(self):
        data = [self.width/2-100, 0, 391, 91]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: underline;\">" + self.title_var + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)

    def info(self):

        data   = [100, 500, 250, 350]

        rows = ['itemNmae','itemName2']

        infData=[
            {"itemNmae" : "anser","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

        self.BaseView.info(infData, data, rows)

    def set_window_title(self):
        self.window_title = self.title_var

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()

    def initUI(self):
        self.title_var = str(self.data['name']) + " movies with " + str(self.data['star'])
        self.set_window_title()
        self.title()
        self.BaseView.avatar([100, 80, 250, 350],None,self.data['avatar'])
        self.info()
        self.BaseView.listView([80, 430, 1571, 581], self.data['movies'], 'Movie_List')

    def run_window(self):
        self.initUI()
        self.show()
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.left, self.top, self.width, self.height)