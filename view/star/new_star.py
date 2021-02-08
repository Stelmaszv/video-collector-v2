from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from core.rezolution import SetResolution
from app.db.models import Stars
from app.forms import StarsForm
from core.BaseActions import FormSection,Submit
from app.model_view import StarModelView
from app.db.models import session

class NewStarView(QWidget):

    model= Stars

    def __init__(self):
        super().__init__()
        self.BaseView= BaseView([], self)
        self.FormSection = FormSection(self)
        self.SetResolution = SetResolution()
        self.left =   self.SetResolution.menu_set['EditStars']['position']['left']
        self.top =    self.SetResolution.menu_set['EditStars']['position']['top']
        self.width =  self.SetResolution.menu_set['EditStars']['position']['width']
        self.height = self.SetResolution.menu_set['EditStars']['position']['height']
        self.WindowSize=self.SetResolution.menu_set['EditStars']['window']

    def form_section(self):
        data_line = [
            self.WindowSize['form_section'][0],
            self.WindowSize['form_section'][1],
            self.WindowSize['form_section'][2],
            self.WindowSize['form_section'][3],
        ]
        buttons = self.FormSchema.return_from_section()
        self.FormSection.form_section(data_line, buttons)

    def add_via_dir(self, values):
        self.BaseView.load_view('add_star_via_dir')

    def add_via_dir_loop(self, values):
        self.BaseView.load_view('add_star_via_dirLoop')

    def set_title(self):
        title = 'New star'
        self.window_title = title
        data = [
            self.WindowSize['title_size'][0],
            self.WindowSize['title_size'][1],
            self.WindowSize['title_size'][2],
            self.WindowSize['title_size'][3]
        ]

        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">"+title+"</span></p></body></html>"
        self.BaseView.title(data, text)

    def submit_click(self, values):
        self.Submit.set_data(values)
        self.Submit.run()

    def run_window(self):
        self.set_title()
        self.data = None
        self.FormSchema = StarsForm(self)
        self.Submit = Submit(StarModelView, self.data, self)
        self.setWindowTitle(self.window_title)
        self.form_section()
        self.show()
        self.setGeometry(self.left, self.top, self.width, self.height)