from core.view import AbstractView
from app.db.models import Movies
class Movie(AbstractView):
    model = Movies

    def title(self):
        data = [0, 0, 2000 ,100]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">" + self.data.name + \
               "</span></p></body></html>"
        self.baseView.title(data,text)

    def info(self):

        data = [925, 100, 300, 200]

        rows = ['itemNmae', 'itemName2']

        inf_data = [
            {"itemNmae": "anser", "itemName2": "anser1"},
            {"itemNmae": "anser2", "itemName2": "anser2"},
            {"itemNmae": "anser3", "itemName2": "anser2"}
        ]

        self.baseView.info(inf_data, data, rows)

    def get_menu(self):
        self.baseView.get_nav([ 850, -100,400,400])

    def setupUi(self):
        self.info()
        self.title()
        self.get_menu()
