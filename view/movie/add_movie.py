from PyQt5.QtWidgets import QWidget,QApplication
from core.view import BaseView
from app.db.models import Movies
import sys
from core.additems import AddItems
class AddMovieView(QWidget):

    model=Movies

    def __init__(self):
        super().__init__()
        self.window_title = 'Add new Movie'
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
        list = ['normal','movie_is_star_name','add_movie_to_star','add_movie_to_series']
        self.add_type=self.base_view.form.combo_box(data, list)
        data_line = [100,100,400,50]
        self.dir_location=self.base_view.form.edit_line(data_line,'dir location')
        data_search_button = [300,150,200,50]
        data_button_info=['add_item','add']
        self.base_view.form.button(data_button_info,data_search_button,self.click_add_items)

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()

    def click_add_items(self):
        self.set_data()
        AddItems(self)
        print('run self.close()')

    def set_data(self):
        self.add_type_value=self.add_type.currentText()
        self.dir_location_value=self.dir_location.text()

    def initUI(self):
        self.title()
        self.form()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddMovieView()
    ex.run_window()
    sys.exit(app.exec_())
