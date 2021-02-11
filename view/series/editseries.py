from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from core.BaseActions import FormSection,Submit
from core.rezolution import SetResolution
from app.db.models import Series
from app.forms import SeriesForm
from app.model_view import StarModelView,SeriesModelView

class EditSeries(QWidget):

    model = Series
    submit_view = 'series'

    def __init__(self):
        super().__init__()
        self.BaseView = BaseView([], self)
        self.SetResolution = SetResolution()
        self.FormSection = FormSection(self)
        self.left =   self.SetResolution.menu_set['EditSeries']['position']['left']
        self.top =    self.SetResolution.menu_set['EditSeries']['position']['top']
        self.width =  self.SetResolution.menu_set['EditSeries']['position']['width']
        self.height = self.SetResolution.menu_set['EditSeries']['position']['height']
        self.WindowSize=self.SetResolution.menu_set['EditSeries']['window']

    def form_section(self):
        data_line = self.WindowSize['form_section']

        buttons = self.FormSchema.return_from_section()
        self.FormSection.form_section(data_line, buttons)

    def set_title(self):
        title = 'Edit series '+self.data.name
        self.window_title = title
        data = self.WindowSize['title_size']

        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">"+title+"</span></p></body></html>"
        self.BaseView.title(data, text)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

    def add_star(self,values):
        self.close()
        print('add star')

    def set_photo_for_series(self,values):
        self.close()
        print('set photo')

    def add_tag(self,values):
        self.BaseView.load_view('add_tags', self.data)

    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.Submit = Submit(SeriesModelView,self.data,self)
        self.FormSchema = SeriesForm(self)
        self.form_section()
        self.set_title();
        self.setWindowTitle(self.window_title)
        self.show()
        self.setGeometry(self.left, self.top, self.width, self.height)
        return True