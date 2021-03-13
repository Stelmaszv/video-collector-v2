from PyQt5.QtWidgets import QWidget

from core.BaseActions import FormSection,Submit
from core.rezolution import SetResolution
from app.db.models import Series
from app.forms import SetPhotoToSeriesForm
from app.model_view import SetPhotoToSetiesView
from core.BaseActions import ViewBaseAction
from core.view import AbstractBaseView

class SetPhotoToSeries(QWidget, AbstractBaseView):

    model = Series
    FormSchema = SetPhotoToSeriesForm
    reset_view = 'series'
    resolution_index = 'EditSeries'
    show_elemnts = ['Tags', 'Description', 'Galery', 'Nav','Info','Avatar']
    ModelView = SetPhotoToSetiesView

    def submit_click(self,values):
        print(values)
