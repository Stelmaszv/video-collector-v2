from PyQt5.QtWidgets import QWidget
from app.db.models import Stars
from core.view import BaseView
from core.BaseActions import FormSection
class EditStarView(QWidget):

    model = Stars

    def __init__(self):
        super().__init__()
        self.window_title = 'Edit star window'
        self.BaseView= BaseView([], self)
        self.FormSection = FormSection(self)

    def run_window(self):
        """
        self.setWindowTitle(self.window_title)
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        data_search_button = [300, 150, 200, 50]
        data_button_info = ['add_item', 'add']
        self.BaseView.Form.button(data_button_info, data_search_button, self.click_add_items)
        data_line = [100,100,400,50]
        self.dir_location=self.BaseView.Form.edit_line(data_line, 'dir location')
        self.show()
        """
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.set_title();

        data_line = [50, 50, 400, 250]

        buttons=[
            {
                'type'          :  'label',
                'name'          :  'name',
                'place_holder'  :  'Name',
                'grid_data'     :  [0,0,1,1]
            },
            {
                'type'          : 'edit_line',
                'name'          : 'name',
                'place_holder'  :  self.data.name,
                'grid_data'     :  [0,1,1,1]
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
                'place_holder': str(self.data.weight)+' kg',
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
                'place_holder': str(self.data.date_of_birth),
                'grid_data': [5, 1, 1, 1]
            },
            {
                'type': 'button_submit',
                'name': 'submit',
                'place_holder': 'submit',
                'grid_data': [6, 1, 1, 1],
                'click'    : self.submit_click
            },
        ]
        self.FormSection.form_section(data_line,buttons)
        self.show()
        return True
    def submit_click(self,values):
        print(values)

    def set_title(self):
        title = 'Edit star '+self.data.name
        data = [0, 0, 500, 50]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">"+title+"</span></p></body></html>"
        self.BaseView.title(data, text)

    def click_add_items(self):
        print('edit');
