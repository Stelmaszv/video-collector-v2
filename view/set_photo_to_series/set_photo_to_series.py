from PyQt5.QtWidgets import QWidget

from app.db.models import Series
from app.forms import SetPhotoToSeriesForm
from app.model_view import SetPhotoToSetiesView
from core.view import AbstractBaseView


class SetPhotoToSeries(QWidget, AbstractBaseView):

    model = Series
    FormSchema = SetPhotoToSeriesForm
    reset_view = 'edit_series'
    submit_view = 'edit_series'
    resolution_index = 'SetPhotoToSeries'
    show_elemnts = ['Tags', 'Description', 'Galery', 'Nav','Info','Avatar']
    ModelView = SetPhotoToSetiesView

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()
