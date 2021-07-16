from PyQt5.QtWidgets import QWidget
from core.view import AbstractBaseView
from app.forms import TagsFormAddToSearch
from app.db.models import Tags,Stars
class AbstractAdd(AbstractBaseView):

    resolution_index = 'add_tag'
    window_title = ''
    show_elemnts = ['Info','Galery','Nav','Avatar','Description','Tags']
    FormSchema   = TagsFormAddToSearch
    list_view = 'Tags'
    reset_view ='add_tag_advnace_search_view'
    data_array      = []
    list_model_off = True
    model_view_off = True
    errr =  ''
    AddModel =  None
    index=''

    def save_click(self,values):
        from .advande_search import AdvanceSearch
        self.close()
        AS = AdvanceSearch()
        AS.criterions[self.index] = self.data_array
        AS.run_window()

    def delete(self,Tag):
        for el in self.data_array:
            if el == Tag:
                self.data_array.remove(el)
        self.reset()

    def set_up(self):
        self.set_list_view_data(self.data_array)

    def base_reset(self,Obj):
        ATASV = Obj()
        ATASV.data_array = self.data_array
        ATASV.run_window()

    def submit_click(self,values):
        def add_tag():
            for el in values:
                self.data_array.append(el['value'])
            self.reset()

        def errr(mess):
            data = [
                mess,
                '',
                ''
            ]
            self.BaseView.Massage.show(data)

        data = self.session.query(self.AddModel).filter(self.AddModel.name == values[0]['value']).all()
        if len(values[0]['value']) == 0:
            errr('Please enter '+self.errr+' name !')
        else:
            if values[0]['value'] in self.data_array:
                errr(self.errr+' '+values[0]['value'] + ' already exist in list !')
            else:
                if len(data) == 0:
                    errr(self.errr+' '+values[0]['value'] + ' not found in DB !')
                else:
                    add_tag()

    def reset(self):
        pass

class AddTagAdvnaceSearchView(QWidget,AbstractAdd):

    window_title = 'Add tag advance search view'
    errr =  'Tag'
    AddModel =  Tags
    index = 'Tags'

    def reset(self):
        self.close()
        ATASV = AddTagAdvnaceSearchView()
        ATASV.data_array = self.data_array
        ATASV.run_window()

class AddStarsAdvnaceSearchView(QWidget,AbstractAdd):

    window_title = 'Add star advance search view'
    errr =  'Star'
    AddModel =  Stars
    index='Stars'

    def reset(self):
        self.close()
        ATASV = AddStarsAdvnaceSearchView()
        ATASV.data_array = self.data_array
        ATASV.run_window()
