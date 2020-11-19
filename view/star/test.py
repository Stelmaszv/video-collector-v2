from app.db.models import Stars
from PyQt5.QtWidgets import QWidget
class StarView(QWidget):

    def __init__(self):
        super().__init__()
        self.window_title = 'PyQt5 button - pythonspot.com'
        self.model = Stars

    def run_window(self):

        self.show()

