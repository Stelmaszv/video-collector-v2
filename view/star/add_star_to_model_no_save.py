from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import TagsForm
from app.db.models import Stars
from view.menu.advande_search import AdvanceSearch
class AddStarToModelNoSave(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add Star for search criterion'
    show_elemnts = ['Info','Galery','Nav','Avatar','Description','Tags','List']
    FormSchema = TagsForm
    model_view_off = True
    methods = ['submit_click']
    criterions=[]

    def set_up(self):
        print(self.criterions)

    def submit_click(self, values):

        if len(values[0]['value'])>0:
            Obj = self.session.query(Stars).filter(Stars.name == values[0]['value']).first()
            if Obj is not None:
                self.close()
                ATNS = AdvanceSearch()
                self.criterions['Stars'].append(values[0]['value'])
                ATNS.criterions = self.criterions
                ATNS.run_window()
            else:
                data = [
                    'Errors in form',
                     'star '+str(values[0]['value'])+' not exist',
                    ''
                ]
                self.BaseView.Massage.show(data)
        else:
            data = [
                'Errors in form',
                'Please enter data',
                ''
            ]
            self.BaseView.Massage.show(data)