from PyQt5.QtWidgets import QWidget
from app.db.models import Stars
from core.view import BaseView
from core.BaseActions import FormSection,Submit
from core.rezolution import SetResolution
from app.forms import StarsForm

class AddStarModel:

    def __init__(self,data):
        self.data=data

    def add_data(self,data):
        print(data)
        if data[0]['value']:
            self.data.name           =  data[0]['value']
        if data[1]['value']:
            self.data.height         =  data[1]['value']
        if data[2]['value']:
            self.data.weight         =  data[2]['value']
        if data[3]['value']:
            self.data.ethnicity      =  data[3]['value']
        if data[4]['value']:
            self.data.hair_color     =  data[4]['value']
        if data[5]['value']:
            self.data.date_of_birth  =  data[5]['value']

class EditStarView(QWidget):

    model = Stars
    FormSchema = []
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

    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.Submit = Submit(AddStarModel,self.data,self)
        self.FormSchema = StarsForm(self)
        self.set_title();
        self.setWindowTitle(self.window_title)
        self.form_section()
        self.show()
        self.setGeometry(self.left , self.top, self.width, self.height)
        return True

    def form_section(self):
        data_line = [
            self.WindowSize['form_section'][0],
            self.WindowSize['form_section'][1],
            self.WindowSize['form_section'][2],
            self.WindowSize['form_section'][3],
        ]

        buttons = self.FormSchema.return_from_section()
        self.FormSection.form_section(data_line, buttons)

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

    def add_tag(self,values):
        self.close()
        self.BaseView.load_view('add_tags', self.data)

    def set_title(self):
        title = 'Edit star '+self.data.name
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
