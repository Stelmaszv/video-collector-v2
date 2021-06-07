import json
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import JSONDataConfigForm
from app.model_view import ConfigAddDataModel
from view.menu.menu import Menu
class JSONConfigView(QWidget,AbstractBaseView):
    FormSchema = JSONDataConfigForm
    ModelView  = ConfigAddDataModel
    search_in='search_in'
    window_title = 'JSON data config'
    resolution_index   = 'Menu'
    show_elemnts = ['Title','Info','Galery','Nav','Avatar','List']

    def submit_click(self,values):
        self.Submit.auto_model=False
        self.Submit.set_data(values)
        self.Submit.run()
        if len(self.Submit.error)==0:
            array = {
                "dirs": [{
                        "type": "stars",
                        "dir": values[0]['value']
                    },
                    {
                        "type": "series",
                        "dir": values[1]['value']
                    }
                ],
                "movies_photos": values[2]['value'],
            }
            json_array = json.dumps(array)
            f = open('data.JSON', "x")
            f.write(json_array)
            f.close()
            self.close()
            M = Menu(0)
            M.run_window()
