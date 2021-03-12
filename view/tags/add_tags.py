from PyQt5.QtWidgets import QWidget
from core.view import AbstractBaseView
from core.BaseActions import AddTag
from app.forms import TagsForm
from app.db.models import Series,Movies

class AddTagView(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add tag'
    show_elemnts = ['Info','Galery','Nav','Avatar','Description','Tags']
    model_view_off = True
    FormSchema   = TagsForm
    list_view = 'Tags'
    methods = ['submit_click']

    def  set_up(self):
        self.model=self.obj.model
        self.set_list_view_data(self.data.tags)

    def submit_click(self,values):
        AT=AddTag(values,self)
        AT.add()

    def delete(self,tag):
        AT=AddTag([],self)
        AT.remove_tag(tag)
        self.BaseActions.reset()
        return True

class MoviesAddTagView(AddTagView):
    model = Movies
    reset_view = 'movies'

class SeriesAddTagView(AddTagView):
    model = Series
    reset_view = 'series'


