from PyQt5.QtWidgets import QWidget
from app.db.models import Stars
from core.view import BaseView
from core.BaseActions import FormSection,Submit

class AddStarModel:

    def __init__(self,data):
        self.data=data

    def add_data(self,data):
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

    def __init__(self):
        super().__init__()
        self.BaseView= BaseView([], self)
        self.FormSection = FormSection(self)

    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.Submit = Submit(AddStarModel,self.data)
        self.set_title();
        self.setWindowTitle(self.window_title)
        self.form_section()
        self.show()
        return True

    def valid_name(self):
        return True

    def form_section(self):
        data_line = [50, 50, 400, 250]

        buttons = [
            {
                'type'        : 'label',
                'name'        : 'name',
                'place_holder': 'Name',
                'grid_data'   : [0, 0, 1, 1]
            },
            {
                'type': 'edit_line',
                'name': 'name',
                'validation': "[A-Z]+.?[a-z]+.?[a-z]+.?[A-Z]+.?[a-z]+.?",
                'data_type': 'string',
                'DB': 'name',
                'place_holder': self.data.name,
                'grid_data': [0, 1, 1, 1]
            },
            {
                'type': 'label',
                'name': 'height',
                'place_holder': 'height',
                'grid_data': [1, 0, 1, 1]
            },
            {
                'type': 'edit_line',
                'name': 'height',
                'data_type': 'int',
                'validation': "[0-9][0-9][0-9]",
                'DB': 'height',
                'place_holder': str(self.data.height) + ' cm',
                'grid_data': [1, 1, 1, 1]
            },
            {
                'type': 'label',
                'name': 'weight',
                'place_holder': 'Weight',
                'grid_data': [2, 0, 1, 1]
            },
            {
                'type': 'edit_line',
                'name': 'weight',
                'data_type': 'int',
                'DB': 'weight',
                'validation': "[0-9][0-9][0-9]",
                'place_holder': str(self.data.weight) + ' kg',
                'grid_data': [2, 1, 1, 1]
            },
            {
                'type': 'label',
                'name': 'ethnicity',
                'place_holder': 'Ethnicity',
                'grid_data': [3, 0, 1, 1]
            },
            {
                'type': 'edit_line',
                'name': 'ethnicity',
                'data_type': 'int',
                'DB': 'ethnicity',
                'validation': "[a-z]+.?[a-z]+.?[A-Z]+.?[A-Z]{,2}",
                'place_holder': str(self.data.ethnicity),
                'grid_data': [3, 1, 1, 1]
            },
            {
                'type': 'label',
                'name': 'hair_color',
                'place_holder': 'Hair color',
                'grid_data': [4, 0, 1, 1]
            },
            {
                'type': 'edit_line',
                'name': 'hair_color',
                'data_type': 'string',
                'DB': 'hair_color',
                'validation': "[a-z]+.?[a-z]+.?[A-Z]+.?[A-Z]{,2}",
                'place_holder': str(self.data.hair_color),
                'grid_data': [4, 1, 1, 1]
            },
            {
                'type': 'label',
                'name': 'date_of_birth',
                'place_holder': 'Date of birth',
                'grid_data': [5, 0, 1, 1]
            },
            {
                'type': 'edit_line',
                'name': 'date_of_birth',
                'data_type': 'data',
                'DB': 'date_of_birth',
                'validation': "[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]",
                'place_holder': str(self.data.date_of_birth),
                'grid_data': [5, 1, 1, 1]
            },
            {
                'type': 'button_submit',
                'name': 'submit',
                'place_holder': 'submit',
                'grid_data': [6, 1, 1, 1],
                'click': self.submit_click
            },
        ]
        self.FormSection.form_section(data_line, buttons)
    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()

    def set_title(self):
        title = 'Edit star '+self.data.name
        self.window_title = title
        data = [0, 0, 500, 50]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">"+title+"</span></p></body></html>"
        self.BaseView.title(data, text)

    def click_add_items(self):
        print('edit');
