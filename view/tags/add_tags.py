from PyQt5.QtWidgets import QWidget
from core.view import BaseView
from core.BaseActions import FormSection,AddTag,ViewBaseAction
class AddTagView(QWidget):

    reset_view='edit_star'

    def run_window(self):
        self.init()
        self.set_title()
        self.add_tags_form()
        self.tags_list()
        self.show()

    def delete(self,tag):
        AT=AddTag([],self.data)
        AT.remove_tag(tag)
        self.BaseActions.reset()
        return True


    def tags_list(self):
        self.BaseView.listView([500, 100, 1200, 900], self.data.tags, 'Tags',False,False)

    def add_tags_form(self):

        data_line = [
            200,
            200,
            200,
            200,
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
                'grid_data': [2, 1, 1, 1],
                'click': self.submit_click
            },
        ]
        self.FormSection.form_section(data_line, buttons)

    def submit_click(self,values):
        AT=AddTag(values,self.data)
        AT.add()

    def init(self):
        self.model=self.obj.model
        self.BaseView = BaseView([], self)
        self.FormSection = FormSection(self)
        self.BaseActions = ViewBaseAction(self)
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data

    def set_title(self):
        title = 'Add tags to '+self.data.name
        self.window_title = title
        data = [
            100,
            100,
            1000,
            100
        ]


        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:20pt;font-weight:600; " \
               "text-decoration: none;\">"+title+"</span></p></body></html>"
        self.BaseView.title(data, text)

