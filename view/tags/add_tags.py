from PyQt5.QtWidgets import QWidget
from core.view import AbstractBaseView
from core.BaseActions import AddTag,AddStar
from app.forms import TagsForm
from app.db.models import Series,Movies,Stars

class AddTagView(QWidget,AbstractBaseView):
    resolution_index = 'add_tag'
    window_title = 'Add tag'
    show_elemnts = ['Info','Galery','Nav','Avatar','Description','Tags']
    model_view_off = True
    FormSchema   = TagsForm
    list_view = 'Tags'


    def  set_up(self):
        self.model=self.obj.model
        self.set_list_view_data(self.data.tags)

    def submit_click(self,values):
        AT=AddTag(values,self)
        AT.add()

    def delete(self,Tag):
        AT=AddTag([],self)
        AT.remove(Tag)
        self.BaseActions.reset()
        return True

class MoviesAddTagView(AddTagView):
    model = Movies
    reset_view = 'movies_add_tag_view'

class SeriesAddTagView(AddTagView):
    model = Series
    reset_view = 'series_add_tag_view'

class StarsAddTagView(AddTagView):
    model = Stars
    reset_view = 'stars_add_tag_view'


