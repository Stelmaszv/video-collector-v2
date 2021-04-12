from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import MenuFormSchena,JSONDataConfigForm
from app.model_view import ConfigAddDataModel
class JSONConfigView(QWidget,AbstractBaseView):
    FormSchema = JSONDataConfigForm
    ModelView  = ConfigAddDataModel
    search_in='search_in'
    window_title = 'JSON data config'
    resolution_index   = 'Menu'
    show_elemnts = ['Title','Info','Galery','Nav','Avatar','List']

    def submit_click(self,values):
        self.Submit.set_data(values)
        self.Submit.run()
