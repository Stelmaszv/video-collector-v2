from PyQt5.QtWidgets import QWidget
from app.db.models import Stars
from core.view import BaseView
class EditStarView(QWidget):

    model = Stars

    def __init__(self):
        super().__init__()
        self.window_title = 'Edit star window'
        self.BaseView= BaseView([], self)

    def run_window(self):
        self.setWindowTitle(self.window_title)
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.show()
        return True
