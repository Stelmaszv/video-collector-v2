from PyQt5.QtWidgets import QWidget
from core.view import AbstractBaseView
from app.forms import TagsForm
from app.db.models import Tags
class AddTagAdvnaceSearchView(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add tag advance search view'
    show_elemnts = ['Info','Galery','Nav','Avatar','Description','Tags']
    FormSchema   = TagsForm
    list_view = 'Tags'
    reset_view ='add_tag_advnace_search_view'
    tags      = []
    list_model_off = True
    model_view_off = True

    def  set_up(self):
        self.set_list_view_data(self.tags[1:])

    def reset(self):
        self.close()
        ATASV = AddTagAdvnaceSearchView()
        ATASV.tags = self.tags
        ATASV.run_window()

    def submit_click(self,values):
        def add_tag():
            self.tags.append(values[0]['value'])
            self.reset()

        def errr(mess):
            data = [
                mess,
                '',
                ''
            ]
            self.BaseView.Massage.show(data)

        data=self.session.query(Tags).filter(Tags.name==values[0]['value']).all()
        if len(values[0]['value']) == 0:
            errr('Please enter tag name !')
        else:
            if values[0]['value'] in self.tags:
                errr('Tag ' + values[0]['value'] + ' already exist in list !')
            else:
                if len(data) == 0:
                    errr('Tag '+values[0]['value']+' not found in DB !')
                else:
                    add_tag()

    def delete(self,Tag):
        self.tags.remove(Tag)
        self.reset()

    def closeEvent(self, QCloseEvent):
        from .advande_search import AdvanceSearch
        AS=AdvanceSearch()
        AS.criterions['Tags']=self.tags
        AS.run_window()
