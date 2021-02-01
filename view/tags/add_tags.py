from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from core.BaseActions import FormSection,AddTag,ViewBaseAction
from core.rezolution import SetResolution
class AddTagView(QWidget):

    reset_view='edit_star'

    def init(self):
        self.model=self.obj.model
        self.BaseView = BaseView([], self)
        self.FormSection = FormSection(self)
        self.BaseActions = ViewBaseAction(self)
        self.SetResolution = SetResolution()
        self.left =   self.SetResolution.menu_set['add_tag']['position']['left']
        self.top =    self.SetResolution.menu_set['add_tag']['position']['top']
        self.width =  self.SetResolution.menu_set['add_tag']['position']['width']
        self.height = self.SetResolution.menu_set['add_tag']['position']['height']
        self.WindowSize=self.SetResolution.menu_set['add_tag']['window']
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data

    def run_window(self):
        self.init()
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.set_title()
        self.add_tags_form()
        self.tags_list()
        self.show()

    def delete(self,tag):
        AT=AddTag([],self)
        AT.remove_tag(tag)
        self.BaseActions.reset()
        return True


    def tags_list(self):
        self.BaseView.listView([
            self.WindowSize['list_view_size'][0],
            self.WindowSize['list_view_size'][1],
            self.WindowSize['list_view_size'][2],
            self.WindowSize['list_view_size'][3]
        ], self.data.tags, 'Tags',False,False)

    def add_tags_form(self):

        data_line = [
            self.WindowSize['form_section'][0],
            self.WindowSize['form_section'][1],
            self.WindowSize['form_section'][2],
            self.WindowSize['form_section'][3]
        ]

        buttons = [
            {
                'type': 'label',
                'name': 'name',
                'place_holder': 'Tag Name',
                'grid_data': [0, 0, 1, 1]
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
                'type': 'button_submit',
                'obj_name': 'submit',
                'name': 'Submit',
                'place_holder': 'Submit',
                'grid_data': [0, 2, 1, 1],
                'click': self.submit_click
            },
        ]
        self.FormSection.form_section(data_line, buttons)

    def submit_click(self,values):
        AT=AddTag(values,self)
        AT.add()

    def set_title(self):
        title = 'Add tags to '+self.data.name
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

