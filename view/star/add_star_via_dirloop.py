from PyQt5.QtWidgets import QWidget,QApplication
from core.view import BaseView
from core.BaseActions import FormSection
from core.rezolution import SetResolution
from app.db.models import Stars
from core.dir import AddStarViaDirLoop

import sys

class AddStarViaDirViewLoop(QWidget):

    model = Stars

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
                'name'        : 'dir-location',
                'place_holder': 'Dir location',
                'grid_data'   : [0, 0, 1, 1]
            },
            {
                'type': 'edit_line',
                'name': 'name',
                'validation': "",
                'data_type': 'string',
                'DB': 'name',
                'place_holder': '',
                'grid_data': [0, 1, 1, 1]
            },
            {
                'type': 'button_submit',
                'obj_name': 'submit',
                'name': 'Submit',
                'place_holder': 'Submit',
                'grid_data': [1, 1, 1, 1],
                'click': self.submit_click
            },
        ]
        self.FormSection.form_section(data_line, buttons)

    def submit_click(self,values):
        ASVDL = AddStarViaDirLoop(values[0]['value'])
        ASVDL.add_files()
        self.close()

    def set_title(self):
        title = 'New star  via dir loop'
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

    def run_window(self):
        self.set_title()
        self.setWindowTitle(self.window_title)
        self.form_section()
        self.show()
        self.setGeometry(self.left, self.top, self.width, self.height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddStarViaDirViewLoop()
    ex.run_window()
    sys.exit(app.exec_())