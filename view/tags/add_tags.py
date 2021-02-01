from PyQt5.QtWidgets import QWidget
from core.view import BaseView
class AddTagView(QWidget):

    def run_window(self):
        self.init()
        print(self.data.tags)
        self.show()

    def init(self):
        self.model=self.obj.model
        self.BaseView = BaseView([], self)
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
