
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import TagsForm
from view.menu.advande_search import AdvanceSearch
class CriterionSearch(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add tag for search criterion'
    show_elemnts = ['Info','Galery','Nav','Avatar','Description','Tags','List']
    FormSchema = TagsForm
    model_view_off = True
    criterions=[]

    def set_up(self):
        print(self.criterions)

    def submit_click(self,values):
        pass

    def if_empty_value(self,value):
        if len(value)==0:
            data = [
                'Errors in form',
                'Please enter data',
                ''
            ]
            self.BaseView.Massage.show(data)
            return False
        return True
    def if_value_exist_in_model(self,model,value):
        Obj = self.session.query(model).filter(model.name == value).first()
        if Obj is None:
            data = [
                'Errors in form',
                str(value)+' not exist in model '+str(model.__tablename__ ),
                ''
            ]
            self.BaseView.Massage.show(data)
            return False
        return True
    def add_data(self,obj,place,value):
        self.close()
        ATNS = AdvanceSearch()
        self.criterions[place].append(value)
        ATNS.criterions = self.criterions
        ATNS.run_window()


