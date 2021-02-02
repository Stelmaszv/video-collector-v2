from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from core.BaseActions import FormSection
from core.rezolution import SetResolution
from app.db.models import Stars
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
                'place_holder': '',
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
                'place_holder': '',
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
                'place_holder': '',
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
                'place_holder': '',
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
                'place_holder': '',
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
                'place_holder': '',
                'grid_data': [5, 1, 1, 1]
            },
            {
                'type': 'button',
                'obj_name': 'add_tags',
                'name': 'Add Tags',
                'place_holder': 'Tags',
                'grid_data': [6, 1, 1, 1],
                'click': self.add_tag
            },

            {
                'type': 'button_submit',
                'obj_name': 'submit',
                'name': 'Submit',
                'place_holder': 'Submit',
                'grid_data': [7, 1, 1, 1],
                'click': self.submit_click
            },
            {
                'type': 'button',
                'obj_name': 'via_dir',
                'name': 'Dir',
                'place_holder': 'Via dir',
                'grid_data': [8, 1, 1, 1],
                'click': self.add_via_dir
            },
            {
                'type': 'button',
                'obj_name': 'via_dir_loop',
                'name': 'Dir loop',
                'place_holder': 'Via dir loop',
                'grid_data': [9, 1, 1, 1],
                'click': self.add_via_dir_loop
            },
        ]
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
        print(values)

    def add_tag(self, values):
        print('add tags')

    def run_window(self):
        self.set_title()
        self.setWindowTitle(self.window_title)
        self.form_section()
        self.show()
        self.setGeometry(self.left, self.top, self.width, self.height)